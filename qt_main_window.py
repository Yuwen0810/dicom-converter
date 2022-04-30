# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VideoConverter.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1085, 748)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/vector/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBoxSourceFile = QtWidgets.QGroupBox(self.frame)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.groupBoxSourceFile.setFont(font)
        self.groupBoxSourceFile.setObjectName("groupBoxSourceFile")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBoxSourceFile)
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_4 = QtWidgets.QFrame(self.groupBoxSourceFile)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.frame_4.setFont(font)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelSourcePath = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.labelSourcePath.setFont(font)
        self.labelSourcePath.setObjectName("labelSourcePath")
        self.horizontalLayout_2.addWidget(self.labelSourcePath, 0, QtCore.Qt.AlignVCenter)
        self.comboBoxSourcePath = QtWidgets.QComboBox(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxSourcePath.sizePolicy().hasHeightForWidth())
        self.comboBoxSourcePath.setSizePolicy(sizePolicy)
        self.comboBoxSourcePath.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBoxSourcePath.setMaximumSize(QtCore.QSize(16777215, 30))
        self.comboBoxSourcePath.setStyleSheet("")
        self.comboBoxSourcePath.setObjectName("comboBoxSourcePath")
        self.horizontalLayout_2.addWidget(self.comboBoxSourcePath)
        self.pushButtonSourceBrowse = QtWidgets.QPushButton(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.pushButtonSourceBrowse.setFont(font)
        self.pushButtonSourceBrowse.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/folder.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonSourceBrowse.setIcon(icon1)
        self.pushButtonSourceBrowse.setObjectName("pushButtonSourceBrowse")
        self.horizontalLayout_2.addWidget(self.pushButtonSourceBrowse)
        self.verticalLayout_2.addWidget(self.frame_4, 0, QtCore.Qt.AlignTop)
        self.frame_12 = QtWidgets.QFrame(self.groupBoxSourceFile)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.frame_12.setFont(font)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_8.setContentsMargins(5, 0, 5, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pushButtonPathSetting = QtWidgets.QPushButton(self.frame_12)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.pushButtonPathSetting.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/settings.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonPathSetting.setIcon(icon2)
        self.pushButtonPathSetting.setObjectName("pushButtonPathSetting")
        self.horizontalLayout_8.addWidget(self.pushButtonPathSetting, 0, QtCore.Qt.AlignLeft)
        self.frame_5 = QtWidgets.QFrame(self.frame_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.frame_5.setFont(font)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButtonSourceSave = QtWidgets.QPushButton(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.pushButtonSourceSave.setFont(font)
        self.pushButtonSourceSave.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/save.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonSourceSave.setIcon(icon3)
        self.pushButtonSourceSave.setObjectName("pushButtonSourceSave")
        self.horizontalLayout_4.addWidget(self.pushButtonSourceSave)
        self.pushButtonSourceExplorer = QtWidgets.QPushButton(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.pushButtonSourceExplorer.setFont(font)
        self.pushButtonSourceExplorer.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/external-link.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonSourceExplorer.setIcon(icon4)
        self.pushButtonSourceExplorer.setObjectName("pushButtonSourceExplorer")
        self.horizontalLayout_4.addWidget(self.pushButtonSourceExplorer)
        self.pushButtonSourceBack = QtWidgets.QPushButton(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.pushButtonSourceBack.setFont(font)
        self.pushButtonSourceBack.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons/corner-up-left.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonSourceBack.setIcon(icon5)
        self.pushButtonSourceBack.setCheckable(False)
        self.pushButtonSourceBack.setObjectName("pushButtonSourceBack")
        self.horizontalLayout_4.addWidget(self.pushButtonSourceBack)
        self.horizontalLayout_8.addWidget(self.frame_5, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.verticalLayout_2.addWidget(self.frame_12)
        self.frame_8 = QtWidgets.QFrame(self.groupBoxSourceFile)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.frame_8.setFont(font)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_8)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.listViewSource = QtWidgets.QListView(self.frame_8)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.listViewSource.setFont(font)
        self.listViewSource.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listViewSource.setObjectName("listViewSource")
        self.gridLayout_3.addWidget(self.listViewSource, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_8)
        self.gridLayout.addWidget(self.groupBoxSourceFile, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.frame, 0, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.frame_2.setFont(font)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButtonSwap = QtWidgets.QPushButton(self.frame_2)
        self.pushButtonSwap.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.pushButtonSwap.setFont(font)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/icons/repeat.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonSwap.setIcon(icon6)
        self.pushButtonSwap.setObjectName("pushButtonSwap")
        self.verticalLayout_3.addWidget(self.pushButtonSwap)
        spacerItem = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_3.addItem(spacerItem)
        self.pushButtonConvert = QtWidgets.QPushButton(self.frame_2)
        self.pushButtonConvert.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButtonConvert.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.pushButtonConvert.setFont(font)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/icons/chevrons-right.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonConvert.setIcon(icon7)
        self.pushButtonConvert.setObjectName("pushButtonConvert")
        self.verticalLayout_3.addWidget(self.pushButtonConvert, 0, QtCore.Qt.AlignBottom)
        self.groupBoxImage = QtWidgets.QGroupBox(self.frame_2)
        self.groupBoxImage.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.groupBoxImage.setFont(font)
        self.groupBoxImage.setObjectName("groupBoxImage")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBoxImage)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.radioButtonJpg = QtWidgets.QRadioButton(self.groupBoxImage)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.radioButtonJpg.setFont(font)
        self.radioButtonJpg.setObjectName("radioButtonJpg")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.radioButtonJpg)
        self.gridLayout_5.addWidget(self.radioButtonJpg, 1, 0, 1, 1)
        self.radioButtonPng = QtWidgets.QRadioButton(self.groupBoxImage)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.radioButtonPng.setFont(font)
        self.radioButtonPng.setObjectName("radioButtonPng")
        self.buttonGroup.addButton(self.radioButtonPng)
        self.gridLayout_5.addWidget(self.radioButtonPng, 0, 0, 1, 1)
        self.radioButtonJpeg = QtWidgets.QRadioButton(self.groupBoxImage)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.radioButtonJpeg.setFont(font)
        self.radioButtonJpeg.setObjectName("radioButtonJpeg")
        self.buttonGroup.addButton(self.radioButtonJpeg)
        self.gridLayout_5.addWidget(self.radioButtonJpeg, 2, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBoxImage, 0, QtCore.Qt.AlignVCenter)
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.labelFPS = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.labelFPS.setFont(font)
        self.labelFPS.setObjectName("labelFPS")
        self.gridLayout_6.addWidget(self.labelFPS, 3, 0, 1, 1)
        self.spinBoxFPS = QtWidgets.QSpinBox(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBoxFPS.sizePolicy().hasHeightForWidth())
        self.spinBoxFPS.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.spinBoxFPS.setFont(font)
        self.spinBoxFPS.setMinimum(1)
        self.spinBoxFPS.setMaximum(1000)
        self.spinBoxFPS.setProperty("value", 20)
        self.spinBoxFPS.setObjectName("spinBoxFPS")
        self.gridLayout_6.addWidget(self.spinBoxFPS, 3, 1, 1, 1)
        self.radioButtonMov = QtWidgets.QRadioButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.radioButtonMov.setFont(font)
        self.radioButtonMov.setObjectName("radioButtonMov")
        self.buttonGroup.addButton(self.radioButtonMov)
        self.gridLayout_6.addWidget(self.radioButtonMov, 2, 0, 1, 2)
        self.radioButtonAvi = QtWidgets.QRadioButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.radioButtonAvi.setFont(font)
        self.radioButtonAvi.setObjectName("radioButtonAvi")
        self.buttonGroup.addButton(self.radioButtonAvi)
        self.gridLayout_6.addWidget(self.radioButtonAvi, 1, 0, 1, 2)
        self.radioButtonMp4 = QtWidgets.QRadioButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.radioButtonMp4.setFont(font)
        self.radioButtonMp4.setChecked(True)
        self.radioButtonMp4.setObjectName("radioButtonMp4")
        self.buttonGroup.addButton(self.radioButtonMp4)
        self.gridLayout_6.addWidget(self.radioButtonMp4, 0, 0, 1, 2)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.gridLayout_7.addWidget(self.frame_2, 0, 1, 1, 1, QtCore.Qt.AlignVCenter)
        self.frame_13 = QtWidgets.QFrame(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.frame_13.setFont(font)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_13)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.labelProgressAllFile = QtWidgets.QLabel(self.frame_13)
        self.labelProgressAllFile.setMinimumSize(QtCore.QSize(120, 0))
        self.labelProgressAllFile.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.labelProgressAllFile.setFont(font)
        self.labelProgressAllFile.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelProgressAllFile.setObjectName("labelProgressAllFile")
        self.gridLayout_8.addWidget(self.labelProgressAllFile, 0, 0, 1, 1)
        self.progressBarAllFile = QtWidgets.QProgressBar(self.frame_13)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.progressBarAllFile.setFont(font)
        self.progressBarAllFile.setProperty("value", 0)
        self.progressBarAllFile.setObjectName("progressBarAllFile")
        self.gridLayout_8.addWidget(self.progressBarAllFile, 0, 1, 1, 1)
        self.labelProgressOneFile = QtWidgets.QLabel(self.frame_13)
        self.labelProgressOneFile.setMinimumSize(QtCore.QSize(120, 0))
        self.labelProgressOneFile.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.labelProgressOneFile.setFont(font)
        self.labelProgressOneFile.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelProgressOneFile.setObjectName("labelProgressOneFile")
        self.gridLayout_8.addWidget(self.labelProgressOneFile, 1, 0, 1, 1)
        self.progressBarOneFile = QtWidgets.QProgressBar(self.frame_13)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.progressBarOneFile.setFont(font)
        self.progressBarOneFile.setMaximum(100)
        self.progressBarOneFile.setProperty("value", 0)
        self.progressBarOneFile.setObjectName("progressBarOneFile")
        self.gridLayout_8.addWidget(self.progressBarOneFile, 1, 1, 1, 1)
        self.gridLayout_7.addWidget(self.frame_13, 1, 0, 1, 3)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.frame_3.setFont(font)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBoxOutputFile = QtWidgets.QGroupBox(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.groupBoxOutputFile.setFont(font)
        self.groupBoxOutputFile.setObjectName("groupBoxOutputFile")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBoxOutputFile)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_6 = QtWidgets.QFrame(self.groupBoxOutputFile)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.frame_6.setFont(font)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labelOutputPath = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.labelOutputPath.setFont(font)
        self.labelOutputPath.setObjectName("labelOutputPath")
        self.horizontalLayout_3.addWidget(self.labelOutputPath, 0, QtCore.Qt.AlignVCenter)
        self.comboBoxOutputPath = QtWidgets.QComboBox(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxOutputPath.sizePolicy().hasHeightForWidth())
        self.comboBoxOutputPath.setSizePolicy(sizePolicy)
        self.comboBoxOutputPath.setObjectName("comboBoxOutputPath")
        self.horizontalLayout_3.addWidget(self.comboBoxOutputPath)
        self.pushButtonOutputBrowse = QtWidgets.QPushButton(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonOutputBrowse.sizePolicy().hasHeightForWidth())
        self.pushButtonOutputBrowse.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.pushButtonOutputBrowse.setFont(font)
        self.pushButtonOutputBrowse.setText("")
        self.pushButtonOutputBrowse.setIcon(icon1)
        self.pushButtonOutputBrowse.setObjectName("pushButtonOutputBrowse")
        self.horizontalLayout_3.addWidget(self.pushButtonOutputBrowse)
        self.verticalLayout.addWidget(self.frame_6, 0, QtCore.Qt.AlignTop)
        self.frame_9 = QtWidgets.QFrame(self.groupBoxOutputFile)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.frame_9.setFont(font)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_9)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.listViewOutput = QtWidgets.QListView(self.frame_9)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.listViewOutput.setFont(font)
        self.listViewOutput.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listViewOutput.setObjectName("listViewOutput")
        self.gridLayout_4.addWidget(self.listViewOutput, 1, 0, 1, 1)
        self.frame_10 = QtWidgets.QFrame(self.frame_9)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.frame_10.setFont(font)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_6.setContentsMargins(5, 0, 5, 0)
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_11 = QtWidgets.QFrame(self.frame_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.frame_11.setFont(font)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.labelOutName = QtWidgets.QLabel(self.frame_11)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.labelOutName.setFont(font)
        self.labelOutName.setObjectName("labelOutName")
        self.horizontalLayout_7.addWidget(self.labelOutName)
        self.textBrowserOutName = QtWidgets.QTextBrowser(self.frame_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowserOutName.sizePolicy().hasHeightForWidth())
        self.textBrowserOutName.setSizePolicy(sizePolicy)
        self.textBrowserOutName.setMinimumSize(QtCore.QSize(0, 25))
        self.textBrowserOutName.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.textBrowserOutName.setFont(font)
        self.textBrowserOutName.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.textBrowserOutName.setStyleSheet("background-color: rgba(200,200,200);")
        self.textBrowserOutName.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowserOutName.setReadOnly(False)
        self.textBrowserOutName.setObjectName("textBrowserOutName")
        self.horizontalLayout_7.addWidget(self.textBrowserOutName)
        self.checkBoxAuto = QtWidgets.QCheckBox(self.frame_11)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.checkBoxAuto.setFont(font)
        self.checkBoxAuto.setChecked(True)
        self.checkBoxAuto.setObjectName("checkBoxAuto")
        self.horizontalLayout_7.addWidget(self.checkBoxAuto)
        self.horizontalLayout_6.addWidget(self.frame_11)
        self.frame_7 = QtWidgets.QFrame(self.frame_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.frame_7.setFont(font)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButtonOutputSave = QtWidgets.QPushButton(self.frame_7)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.pushButtonOutputSave.setFont(font)
        self.pushButtonOutputSave.setText("")
        self.pushButtonOutputSave.setIcon(icon3)
        self.pushButtonOutputSave.setObjectName("pushButtonOutputSave")
        self.horizontalLayout_5.addWidget(self.pushButtonOutputSave)
        self.pushButtonOutputExplorer = QtWidgets.QPushButton(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonOutputExplorer.sizePolicy().hasHeightForWidth())
        self.pushButtonOutputExplorer.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.pushButtonOutputExplorer.setFont(font)
        self.pushButtonOutputExplorer.setText("")
        self.pushButtonOutputExplorer.setIcon(icon4)
        self.pushButtonOutputExplorer.setObjectName("pushButtonOutputExplorer")
        self.horizontalLayout_5.addWidget(self.pushButtonOutputExplorer)
        self.pushButtonOutputBack = QtWidgets.QPushButton(self.frame_7)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.pushButtonOutputBack.setFont(font)
        self.pushButtonOutputBack.setText("")
        self.pushButtonOutputBack.setIcon(icon5)
        self.pushButtonOutputBack.setObjectName("pushButtonOutputBack")
        self.horizontalLayout_5.addWidget(self.pushButtonOutputBack, 0, QtCore.Qt.AlignVCenter)
        self.horizontalLayout_6.addWidget(self.frame_7, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.gridLayout_4.addWidget(self.frame_10, 0, 0, 1, 1, QtCore.Qt.AlignTop)
        self.verticalLayout.addWidget(self.frame_9)
        self.gridLayout_2.addWidget(self.groupBoxOutputFile, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.frame_3, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(6)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout_7.addWidget(self.label, 2, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1085, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dicom Converter"))
        self.groupBoxSourceFile.setTitle(_translate("MainWindow", "Source File"))
        self.labelSourcePath.setText(_translate("MainWindow", "Path :"))
        self.pushButtonSourceBrowse.setToolTip(_translate("MainWindow", "Browse"))
        self.pushButtonPathSetting.setToolTip(_translate("MainWindow", "Set current directory as home directory (Source)"))
        self.pushButtonPathSetting.setText(_translate("MainWindow", " Path Setting"))
        self.pushButtonSourceSave.setToolTip(_translate("MainWindow", "Set current directory as home directory (Source)"))
        self.pushButtonSourceExplorer.setToolTip(_translate("MainWindow", "Open in Explorer"))
        self.pushButtonSourceBack.setToolTip(_translate("MainWindow", "Back"))
        self.pushButtonSwap.setText(_translate("MainWindow", "Swap"))
        self.pushButtonConvert.setText(_translate("MainWindow", "Convert"))
        self.groupBoxImage.setTitle(_translate("MainWindow", "Image"))
        self.radioButtonJpg.setText(_translate("MainWindow", ".JPG"))
        self.radioButtonPng.setText(_translate("MainWindow", ".PNG"))
        self.radioButtonJpeg.setText(_translate("MainWindow", ".JPEG"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Video"))
        self.labelFPS.setText(_translate("MainWindow", "FPS :"))
        self.radioButtonMov.setText(_translate("MainWindow", ".MOV"))
        self.radioButtonAvi.setText(_translate("MainWindow", ".AVI"))
        self.radioButtonMp4.setText(_translate("MainWindow", ".MP4"))
        self.labelProgressAllFile.setText(_translate("MainWindow", "Progress Bar"))
        self.labelProgressOneFile.setText(_translate("MainWindow", "-"))
        self.groupBoxOutputFile.setTitle(_translate("MainWindow", "Output"))
        self.labelOutputPath.setText(_translate("MainWindow", "Path :"))
        self.pushButtonOutputBrowse.setToolTip(_translate("MainWindow", "Browse"))
        self.labelOutName.setText(_translate("MainWindow", "Out name :"))
        self.checkBoxAuto.setText(_translate("MainWindow", "Auto"))
        self.pushButtonOutputSave.setToolTip(_translate("MainWindow", "Set current directory as home directory (Output)"))
        self.pushButtonOutputExplorer.setToolTip(_translate("MainWindow", "Open in Explorer"))
        self.pushButtonOutputBack.setToolTip(_translate("MainWindow", "Back"))
        self.label.setText(_translate("MainWindow", "© 2022 | Yuwen Huang | NTU BEBI Ultrasonic Imaging Laboratory (MD731)"))
import icons_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
