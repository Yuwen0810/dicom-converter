import sys
import os

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMainWindow

from qt_path_setting_window import Ui_MainWindowPathSetting

import cgitb

cgitb.enable(format='text')


class PathSettingWindow(QMainWindow, Ui_MainWindowPathSetting):
	def __init__(self, methods):
		super().__init__()
		self.setupUi(self)

		self.main_item_remove = methods["main_item_remove"]
		self.main_item_add = methods["main_item_add"]
		self.main_item_up = methods["main_item_up"]
		self.main_item_down = methods["main_item_down"]
		self.main_item_set_home = methods["main_item_set_home"]

		self.source_save_path = []
		self.output_save_path = []

		self.pushButtonSourceAdd.clicked.connect(lambda: self.item_add("source"))
		self.pushButtonSourceRemove.clicked.connect(lambda: self.item_remove("source"))
		self.pushButtonSourceUp.clicked.connect(lambda: self.item_up("source"))
		self.pushButtonSourceDown.clicked.connect(lambda: self.item_down("source"))

		self.pushButtonOutputAdd.clicked.connect(lambda: self.item_add("output"))
		self.pushButtonOutputRemove.clicked.connect(lambda: self.item_remove("output"))
		self.pushButtonOutputUp.clicked.connect(lambda: self.item_up("output"))
		self.pushButtonOutputDown.clicked.connect(lambda: self.item_down("output"))



	def update_list_widget(self, target, current_idx=-1):
		if target == "source":
			self.listWidgetSourcePath.clear()
			self.listWidgetSourcePath.addItems(self.source_save_path)
			if current_idx != -1:
				self.listWidgetSourcePath.setCurrentRow(current_idx)

		elif target == "output":
			self.listWidgetOutputPath.clear()
			self.listWidgetOutputPath.addItems(self.output_save_path)
			if current_idx != -1:
				self.listWidgetOutputPath.setCurrentRow(current_idx)

	def item_add(self, target):
		file_path = QFileDialog.getExistingDirectory(self, "Please select a directory", "D:/" if os.path.isdir("D:/") else "C:/")
		if file_path:
			if (target == "source" and file_path not in self.source_save_path) or \
				(target == "output" and file_path not in self.output_save_path):
				self.source_save_path, self.output_save_path = self.main_item_add(target, file_path)
				self.update_list_widget(target)

	def item_remove(self, target):
		selected_idx = -1
		combo_focus_idx = -1
		if target == "source":
			selected_idx = self.listWidgetSourcePath.currentRow()
			combo_focus_idx = selected_idx if selected_idx < len(self.source_save_path) - 1 else selected_idx - 1
		elif target == "output":
			selected_idx = self.listWidgetOutputPath.currentRow()
			combo_focus_idx = selected_idx if selected_idx < len(self.output_save_path) - 1 else selected_idx - 1

		if selected_idx == -1:
			return

		self.source_save_path, self.output_save_path = self.main_item_remove(target, selected_idx)
		self.update_list_widget(target, combo_focus_idx)

	def item_up(self, target):
		selected_idx = None
		if target == "source":
			selected_idx = self.listWidgetSourcePath.currentRow()
		elif target == "output":
			selected_idx = self.listWidgetOutputPath.currentRow()

		if selected_idx == -1 or selected_idx == 0:
			return

		self.main_item_up(target, selected_idx)
		self.update_list_widget(target, selected_idx - 1)

	def item_down(self, target):
		selected_idx = None
		if target == "source":
			selected_idx = self.listWidgetSourcePath.currentRow()
			if selected_idx == -1 or selected_idx == len(self.source_save_path) - 1:
				return

		elif target == "output":
			selected_idx = self.listWidgetOutputPath.currentRow()
			if selected_idx == -1 or selected_idx == len(self.output_save_path) - 1:
				return

		self.main_item_down(target, selected_idx)
		self.update_list_widget(target, selected_idx + 1)


	def show(self, source, output):
		super().show()
		print("Hello second window")

		self.source_save_path = source
		self.output_save_path = output
		self.update_list_widget("source")
		self.update_list_widget("output")

	def closeEvent(self, event):
		super().closeEvent(event)
		print("Bye-bye second window")


if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	window = PathSettingWindow()
	window.show()
	sys.exit(app.exec())
