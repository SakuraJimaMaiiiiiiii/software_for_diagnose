# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window_suanfaguanli.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class suanfaguanli(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(412, 304)
        Dialog.setStyleSheet("QDialog{\n"
"    background-color:rgb(234, 242, 255)\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    background-color:rgb(238, 238, 238);\n"
"}\n"
"QTableWidget::item {\n"
"    color: transparent;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.frame_menu = QtWidgets.QFrame(Dialog)
        self.frame_menu.setGeometry(QtCore.QRect(0, 0, 411, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_menu.sizePolicy().hasHeightForWidth())
        self.frame_menu.setSizePolicy(sizePolicy)
        self.frame_menu.setStyleSheet("QFrame{\n"
"    background-color:rgb(226, 226, 226)\n"
"}")
        self.frame_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_menu.setObjectName("frame_menu")
        self.label = QtWidgets.QLabel(self.frame_menu)
        self.label.setGeometry(QtCore.QRect(160, 10, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setGeometry(QtCore.QRect(0, 70, 411, 241))
        self.frame_2.setStyleSheet("QFrame{\n"
"    background-color:rgb(203, 203, 203)\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton_yucesuanfaguanli = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_yucesuanfaguanli.setGeometry(QtCore.QRect(100, 130, 201, 71))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(13)
        self.pushButton_yucesuanfaguanli.setFont(font)
        self.pushButton_yucesuanfaguanli.setStyleSheet("QPushButton::hover{\n"
"    background-color:rgb(220, 255, 46);\n"
"}\n"
"")
        self.pushButton_yucesuanfaguanli.setObjectName("pushButton_yucesuanfaguanli")
        self.pushButton_zhenduanguanli = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_zhenduanguanli.setGeometry(QtCore.QRect(100, 30, 201, 81))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(13)
        self.pushButton_zhenduanguanli.setFont(font)
        self.pushButton_zhenduanguanli.setStyleSheet("QPushButton::hover{\n"
"    background-color:rgb(220, 255, 46);\n"
"}\n"
"")
        self.pushButton_zhenduanguanli.setObjectName("pushButton_zhenduanguanli")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "算法管理"))
        self.pushButton_yucesuanfaguanli.setText(_translate("Dialog", "预测算法管理"))
        self.pushButton_zhenduanguanli.setText(_translate("Dialog", "系统诊断算法管理"))
