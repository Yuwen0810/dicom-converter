import json

import pydicom
import cv2
import numpy as np
import sys
import os
from glob import glob

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QFileSystemModel

from qt_main_window import Ui_MainWindow
from PathSettingWIndow import PathSettingWindow

import cgitb

cgitb.enable(format='text')

# https://iter01.com/535584.html

class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)

		# initial file browser (About list view)
		self.setting = Setting()

		# initial the setting window
		self.setting_window = PathSettingWindow({
			"main_item_remove": self.main_item_remove,
			"main_item_add": self.main_item_add,
			"main_item_up": self.main_item_up,
			"main_item_down": self.main_item_down,
			"main_item_set_home": self.main_item_set_home
		})

		#
		self.source_model = QFileSystemModel()
		self.output_model = QFileSystemModel()
		self.source_model.setNameFilters(['*.dcm', '*.mp4', '*.avi', '*.mov'])
		self.output_model.setNameFilters(['*.dcm', '*.mp4', '*.avi', '*.mov'])

		self.home_path = "D:/" if os.path.isdir("D:/") else "C:/"
		self.source_current_path = ""
		self.output_current_path = ""

		if len(self.setting.source_save_path) == 0:
			self.source_current_path = self.home_path
		else:
			self.source_current_path = self.setting.source_save_path[0]
			self.comboBoxSourcePath.addItems(self.setting.source_save_path)

		if len(self.setting.output_save_path) == 0:
			self.output_current_path = self.home_path
		else:
			self.output_current_path = self.setting.output_save_path[0]
			self.comboBoxOutputPath.addItems(self.setting.output_save_path)

		self.update_model_path("source", self.source_current_path)
		self.update_model_path("output", self.output_current_path)

		self.listViewSource.doubleClicked.connect(self.listViewSource_clicked)
		self.listViewOutput.doubleClicked.connect(self.listViewOutput_clicked)

		# initial button click event
		self.pushButtonSourceBack.clicked.connect(lambda: self.btn_back_clicked("source"))
		self.pushButtonOutputBack.clicked.connect(lambda: self.btn_back_clicked("output"))
		self.pushButtonSourceSave.clicked.connect(lambda: self.btn_save_clicked("source"))
		self.pushButtonOutputSave.clicked.connect(lambda: self.btn_save_clicked("output"))

		self.pushButtonSourceBrowse.clicked.connect(lambda: self.btn_browse_clicked('source'))
		self.pushButtonOutputBrowse.clicked.connect(lambda: self.btn_browse_clicked('output'))

		self.pushButtonSourceExplorer.clicked.connect(lambda: os.startfile(self.source_current_path))
		self.pushButtonOutputExplorer.clicked.connect(lambda: os.startfile(self.output_current_path))

		self.pushButtonPathSetting.clicked.connect(lambda: self.open_setting_window())

		# convert button click
		self.pushButtonConvert.clicked.connect(lambda: self.btn_convert_clicked())

		# Swap button click
		self.pushButtonSwap.clicked.connect(lambda: self.btn_swap_clicked())

		# CheckBox Change
		self.checkBoxAuto.stateChanged.connect(lambda: self.checkbox_auto_change())

		# ComboBox Change
		self.comboBoxSourcePath.activated.connect(lambda: self.comboBox_clicked('source'))
		self.comboBoxOutputPath.activated.connect(lambda: self.comboBox_clicked('output'))


	# update the list view path
	def update_model_path(self, target, new_path):
		if os.path.isdir(new_path):
			if target == "source":
				self.comboBoxSourcePath.clear()
				if new_path not in self.setting.source_save_path:
					self.comboBoxSourcePath.addItems([new_path] + self.setting.source_save_path)
					self.comboBoxSourcePath.setCurrentIndex(0)
				else:
					self.comboBoxSourcePath.addItems(self.setting.source_save_path)
					self.comboBoxSourcePath.setCurrentIndex(self.setting.source_save_path.index(new_path))

				self.source_current_path = new_path
				self.source_model.setRootPath(self.source_current_path)
				self.listViewSource.setModel(self.source_model)
				self.listViewSource.setRootIndex(self.source_model.index(self.source_current_path))

			elif target == "output":
				self.comboBoxOutputPath.clear()
				if new_path not in self.setting.output_save_path:
					self.comboBoxOutputPath.addItems([new_path] + self.setting.output_save_path)
					self.comboBoxOutputPath.setCurrentIndex(0)
				else:
					self.comboBoxOutputPath.addItems(self.setting.output_save_path)
					self.comboBoxOutputPath.setCurrentIndex(self.setting.output_save_path.index(new_path))

				self.output_current_path = new_path
				self.output_model.setRootPath(self.output_current_path)
				self.listViewOutput.setModel(self.output_model)
				self.listViewOutput.setRootIndex(self.output_model.index(self.output_current_path))




	# Open the directory when double click list item
	def listViewSource_clicked(self, Qmodelidx):
		self.update_model_path("source", self.source_model.filePath(Qmodelidx))

	def listViewOutput_clicked(self, Qmodelidx):
		self.update_model_path("output", self.output_model.filePath(Qmodelidx))

	### Button click event ###
	# back directory
	def btn_back_clicked(self, target):
		# target: {'source', 'output'}
		# action: {'last', 'next'}
		if target == 'source':
			self.update_model_path(target, os.path.split(self.source_current_path)[0])
		elif target == 'output':
			self.update_model_path(target, os.path.split(self.output_current_path)[0])

	# save as home directory
	def btn_save_clicked(self, target):
		# target: {'source', 'output'}
		# action: {'last', 'next'}
		if target == 'source' and self.source_current_path not in self.setting.source_save_path:
			self.setting.source_save_path.append(self.source_current_path)
			self.comboBoxSourcePath.addItem(self.source_current_path)
			self.comboBoxSourcePath.removeItem(0)
			self.comboBoxSourcePath.setCurrentIndex(len(self.setting.source_save_path) - 1)
			self.setting.save()
		elif target == 'output' and self.output_current_path not in self.setting.output_save_path:
			self.setting.output_save_path.append(self.output_current_path)
			self.comboBoxOutputPath.addItem(self.output_current_path)
			self.comboBoxOutputPath.removeItem(0)
			self.comboBoxOutputPath.setCurrentIndex(len(self.setting.output_save_path) - 1)
			self.setting.save()


	# browse directory
	def btn_browse_clicked(self, target):
		file_path = ""
		if target == 'source':
			file_path = QFileDialog.getExistingDirectory(self, "Please select a directory", self.source_current_path)
		elif target == 'output':
			file_path = QFileDialog.getExistingDirectory(self, "Please select a directory", self.output_current_path)

		if file_path != "":
			self.update_model_path(target, file_path)

	# Swap Path
	def btn_swap_clicked(self):
		source_path = self.source_current_path
		output_path = self.output_current_path
		self.update_model_path("source", output_path)
		self.update_model_path("output", source_path)


	def checkbox_auto_change(self):
		# 自動命名模式，可以複選
		if self.checkBoxAuto.isChecked():
			self.listViewSource.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
			self.textBrowserOutName.setStyleSheet("background-color: rgba(200, 200, 200);")
			self.textBrowserOutName.setReadOnly(True)
			self.textBrowserOutName.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
		# 手動命名模式，只能單選
		else:
			self.listViewSource.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
			self.textBrowserOutName.setStyleSheet("")
			self.textBrowserOutName.setReadOnly(False)
			self.textBrowserOutName.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))


	def comboBox_clicked(self, target):
		if os.path.isdir(self.comboBoxSourcePath.currentText()):
			if target == "source":
				self.update_model_path(target, self.comboBoxSourcePath.currentText())
			elif target == "output":
				self.update_model_path(target, self.comboBoxOutputPath.currentText())
		else:
			QtWidgets.QMessageBox.warning(None, "Warning", f'The directory "{self.comboBoxSourcePath.currentText()}" does not exist.')


	# Convert file
	def btn_convert_clicked(self):
		selected_index = self.listViewSource.selectionModel().selectedIndexes()
		self.progressBarAllFile.setMaximum(len(selected_index))
		self.progressBarAllFile.setValue(0)

		# get selected item path, and convert them
		for index in selected_index:
			source_path = self.source_model.filePath(index)
			filename = os.path.split(source_path)[-1] if os.path.isdir(source_path) else os.path.split(source_path)[-1].split('.')[0]
			self.labelProgressAllFile.setText(filename)

			self.convert_file(source_path, self.output_current_path)
			self.progressBarAllFile.setValue(self.progressBarAllFile.value() + 1)

		self.labelProgressAllFile.setText('Progress Bar')


	### Convert Function ###
	def convert_file(self, source_path, output_path):
		output_file_name = ""
		# Get output filename and filepath
		if self.checkBoxAuto.isChecked():
			if os.path.isdir(source_path):
				output_file_name = os.path.split(source_path)[-1]
			else:
				output_file_name = os.path.split(source_path)[-1].split('.')[0]
		else:
			output_file_name = self.textBrowserOutName.toPlainText()

		# 輸出的路徑（不包含附檔名）
		# 如果輸出是圖片，以 output_path 建立資料夾；
		# 如果輸出是影片，以 output_path + extension name 當作檔名
		output_path = os.path.join(output_path, output_file_name)

		# Step 1. 判斷輸出類型
		output_ext = ""
		if self.radioButtonPng.isChecked():
			output_ext = '.png'
		elif self.radioButtonJpg.isChecked():
			output_ext = '.jpg'
		elif self.radioButtonJpeg.isChecked():
			output_ext = '.jpeg'
		elif self.radioButtonMp4.isChecked():
			output_ext = '.mp4'
		elif self.radioButtonAvi.isChecked():
			output_ext = '.avi'
		elif self.radioButtonMov.isChecked():
			output_ext = '.mov'


		# Step 2. 讀取檔案並存檔，使用 SaveHelper 協助
		# 設定 Progress bar
		self.progressBarOneFile.setValue(0)

		# 如果讀到資料夾，預期裡面是圖片
		if os.path.isdir(source_path):
			# 整理要抓的副檔名（資料夾內最多的檔案）
			files = os.listdir(source_path)
			files_extension = np.array([os.path.splitext(file)[-1] for file in files])
			arr, res = np.unique(files_extension, return_counts=True)
			source_extenstion = arr[np.argmax(res)]

			if source_extenstion in ['.png', '.jpg', '.jpeg']:
				imgs_path = sorted(glob(f"{source_path}/*{source_extenstion}"))
				self.progressBarOneFile.setMaximum(len(imgs_path))

				if output_ext in ['.png', '.jpg', '.jpeg']:
					saver = ImageSaveHelper(output_ext, output_path, len(imgs_path))
				elif output_ext in ['.mp4', '.avi', '.mov']:
					saver = VideoSaveHelper(
						output_ext, output_path,
						cv2.imdecode(np.fromfile(imgs_path[0], dtype=np.uint8), -1),
						self.spinBoxFPS.value()
					)
				else:
					print("[Error] Not support extension")
					return

				for path in imgs_path:
					saver.save(cv2.imdecode(np.fromfile(path, dtype=np.uint8), -1))
					self.progressBarOneFile.setValue(self.progressBarOneFile.value() + 1)

		# 如果讀到影片
		elif source_path.split('.')[-1].lower() in ['mp4', 'avi', 'mov']:
			video = cv2.VideoCapture(source_path)
			frame_num = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
			self.progressBarOneFile.setMaximum(frame_num)

			ret, frame = video.read()

			if output_ext in ['.png', '.jpg', '.jpeg']:
				saver = ImageSaveHelper(output_ext, output_path, frame_num)
			elif output_ext in ['.mp4', '.avi', '.mov']:
				saver = VideoSaveHelper(output_ext, output_path, frame, self.spinBoxFPS.value())
			else:
				print("[Error] Not support extension")
				return

			while ret:
				saver.save(frame)
				ret, frame = video.read()
				self.progressBarOneFile.setValue(self.progressBarOneFile.value() + 1)

		# 如果讀到 Dicom
		elif source_path.split('.')[-1].lower() in ['dcm']:
			imgs = pydicom.read_file(source_path).pixel_array
			self.progressBarOneFile.setMaximum(len(imgs))

			if output_ext in ['.png', '.jpg', '.jpeg']:
				saver = ImageSaveHelper(output_ext, output_path, len(imgs))
			elif output_ext in ['.mp4', '.avi', '.mov']:
				saver = VideoSaveHelper(
					output_ext, output_path,
					imgs[0],
					self.spinBoxFPS.value()
				)
			else:
				print("[Error] Not support extension")
				return

			for img in imgs:
				saver.save(img)
				self.progressBarOneFile.setValue(self.progressBarOneFile.value() + 1)

	# About Setting Window
	def open_setting_window(self):
		self.setting_window.show(self.setting.source_save_path, self.setting.output_save_path)


	def main_item_remove(self, target, selected_idx):
		if target == "source":
			self.setting.source_save_path.pop(selected_idx)
			self.setting.save()
			self.update_model_path(target, self.source_current_path)
		elif target == "output":
			self.setting.output_save_path.pop(selected_idx)
			self.setting.save()
			self.update_model_path(target, self.output_current_path)
		return self.setting.source_save_path, self.setting.output_save_path

	def main_item_add(self, target, file_path):
		if target == "source":
			self.setting.source_save_path.append(file_path)
			self.setting.save()
			self.update_model_path(target, self.source_current_path)
		elif target == "output":
			self.setting.output_save_path.append(file_path)
			self.setting.save()
			self.update_model_path(target, self.output_current_path)
		return self.setting.source_save_path, self.setting.output_save_path

	def main_item_up(self, target, selected_idx):
		if target == "source":
			self.setting.source_save_path[selected_idx - 1], self.setting.source_save_path[selected_idx] = \
				self.setting.source_save_path[selected_idx], self.setting.source_save_path[selected_idx - 1]
			self.setting.save()
			self.update_model_path(target, self.source_current_path)
		elif target == "output":
			self.setting.output_save_path[selected_idx - 1], self.setting.output_save_path[selected_idx] = \
				self.setting.output_save_path[selected_idx], self.setting.output_save_path[selected_idx - 1]
			self.setting.save()
			self.update_model_path(target, self.output_current_path)

	def main_item_down(self, target, selected_idx):
		if target == "source":
			self.setting.source_save_path[selected_idx], self.setting.source_save_path[selected_idx + 1] = \
				self.setting.source_save_path[selected_idx + 1], self.setting.source_save_path[selected_idx]
			self.setting.save()
			self.update_model_path(target, self.source_current_path)
		elif target == "output":
			self.setting.output_save_path[selected_idx], self.setting.output_save_path[selected_idx + 1] = \
				self.setting.output_save_path[selected_idx + 1], self.setting.output_save_path[selected_idx]
			self.setting.save()
			self.update_model_path(target, self.output_current_path)

	def main_item_set_home(self, target):
		if target == "source":
			pass
		elif target == "output":
			pass


class ImageSaveHelper:
	def __init__(self, output_ext, output_path, num_of_image):
		self.output_ext = output_ext
		self.output_path = output_path
		self.num_of_digits = len(f"{num_of_image - 1}")
		self.counter = 0

		if not os.path.isdir(output_path):
			os.makedirs(output_path)

	def save(self, image):
		cv2.imencode(self.output_ext, image)[1].tofile(
			os.path.join(self.output_path, f"{str(self.counter).zfill(self.num_of_digits)}{self.output_ext}")
		)
		self.counter += 1


class VideoSaveHelper:
	def __init__(self, output_ext, output_path, temp_img, FPS):
		h, w, _ = temp_img.shape

		fourcc = ""
		if output_ext == '.mp4':
			fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
		elif output_ext == '.avi':
			fourcc = cv2.VideoWriter_fourcc('F', 'M', 'P', '4')
		elif output_ext == '.mov':
			fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')

		self.videowriter = cv2.VideoWriter(f"{output_path}{output_ext}", fourcc, FPS, (w, h))

	def save(self, image):
		self.videowriter.write(image)

	def __del__(self):
		self.videowriter.release()


class Setting:
	def __init__(self):
		self.setting_file = "setting.json"

		try:
			with open(self.setting_file, 'r', encoding='utf-8') as file:
				temp = json.loads(file.read())
				self.source_save_path = temp["source_save_path"]
				self.output_save_path = temp["output_save_path"]
		# else:
		except:
			self.source_save_path = []
			self.output_save_path = []
			with open(self.setting_file, 'w', encoding='utf-8') as file:
				print(json.dumps({
					"source_save_path": self.source_save_path,
					"output_save_path": self.output_save_path,
				}, indent=4), file=file)

	def save(self):
		with open(self.setting_file, 'w', encoding='utf-8') as file:
			print(json.dumps({
				"source_save_path": self.source_save_path,
				"output_save_path": self.output_save_path,
			}, indent=4), file=file)



if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec())
