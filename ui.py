# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\design4.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(415, 652)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(360, 475))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 20, 51, 21))
        self.label.setObjectName("label")
        self.lineEdit_room_id = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_room_id.setGeometry(QtCore.QRect(160, 20, 131, 20))
        self.lineEdit_room_id.setObjectName("lineEdit_room_id")
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.checkBox_paizi = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_paizi.setGeometry(QtCore.QRect(20, 30, 171, 21))
        self.checkBox_paizi.setObjectName("checkBox_paizi")
        self.lineEdit_paizi = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_paizi.setEnabled(False)
        self.lineEdit_paizi.setGeometry(QtCore.QRect(160, 30, 131, 19))
        self.lineEdit_paizi.setReadOnly(False)
        self.lineEdit_paizi.setObjectName("lineEdit_paizi")
        self.checkBox_keyword = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_keyword.setGeometry(QtCore.QRect(20, 60, 171, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_keyword.sizePolicy().hasHeightForWidth())
        self.checkBox_keyword.setSizePolicy(sizePolicy)
        self.checkBox_keyword.setObjectName("checkBox_keyword")
        self.lineEdit_keyword = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_keyword.setEnabled(False)
        self.lineEdit_keyword.setGeometry(QtCore.QRect(160, 60, 131, 19))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(6)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_keyword.sizePolicy().hasHeightForWidth())
        self.lineEdit_keyword.setSizePolicy(sizePolicy)
        self.lineEdit_keyword.setReadOnly(False)
        self.lineEdit_keyword.setObjectName("lineEdit_keyword")
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.pushButton_lottery = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_lottery.sizePolicy().hasHeightForWidth())
        self.pushButton_lottery.setSizePolicy(sizePolicy)
        self.pushButton_lottery.setObjectName("pushButton_lottery")
        self.horizontalLayout_2.addWidget(self.pushButton_lottery)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.textBrowser_viewers = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.textBrowser_viewers.sizePolicy().hasHeightForWidth())
        self.textBrowser_viewers.setSizePolicy(sizePolicy)
        self.textBrowser_viewers.setObjectName("textBrowser_viewers")
        self.verticalLayout_3.addWidget(self.textBrowser_viewers)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.lcdNumber_num_danmu = QtWidgets.QLCDNumber(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lcdNumber_num_danmu.sizePolicy().hasHeightForWidth())
        self.lcdNumber_num_danmu.setSizePolicy(sizePolicy)
        self.lcdNumber_num_danmu.setObjectName("lcdNumber_num_danmu")
        self.gridLayout.addWidget(self.lcdNumber_num_danmu, 2, 1, 1, 1)
        self.lcdNumber_num_viewer = QtWidgets.QLCDNumber(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lcdNumber_num_viewer.sizePolicy().hasHeightForWidth())
        self.lcdNumber_num_viewer.setSizePolicy(sizePolicy)
        self.lcdNumber_num_viewer.setObjectName("lcdNumber_num_viewer")
        self.gridLayout.addWidget(self.lcdNumber_num_viewer, 3, 1, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.textBrowser_lottery_result = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.textBrowser_lottery_result.sizePolicy().hasHeightForWidth())
        self.textBrowser_lottery_result.setSizePolicy(sizePolicy)
        self.textBrowser_lottery_result.setObjectName("textBrowser_lottery_result")
        self.verticalLayout_2.addWidget(self.textBrowser_lottery_result)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Bilibili 弹幕抽奖姬"))
        self.label.setText(_translate("MainWindow", "房间号："))
        self.groupBox.setTitle(_translate("MainWindow", "弹幕筛选"))
        self.checkBox_paizi.setText(_translate("MainWindow", "带牌子："))
        self.checkBox_keyword.setText(_translate("MainWindow", "包含以下关键词："))
        self.pushButton_lottery.setText(_translate("MainWindow", "开始统计"))
        self.label_6.setText(_translate("MainWindow", "参与观众："))
        self.label_2.setText(_translate("MainWindow", "弹幕数量："))
        self.label_3.setText(_translate("MainWindow", "观众数量："))
        self.label_5.setText(_translate("MainWindow", "统计结果："))
        self.label_4.setText(_translate("MainWindow", "by 养猫的小天使喵"))
