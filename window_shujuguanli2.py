# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window_shujuguanli2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5.QtWidgets import QMessageBox,  QGraphicsScene
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import  QPushButton, QFileDialog,  QTableWidgetItem
import os
import pandas as pd
from shared_data import SharedData
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import math


class shujuguanli2(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1554, 865)
        Dialog.setStyleSheet("QDialog{\n"
"    background-color:rgb(234, 242, 255)\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    background-color:white;\n"
"}\n"
"QTableWidget::item {\n"
"    color: black;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.frame_menu = QtWidgets.QFrame(Dialog)
        self.frame_menu.setGeometry(QtCore.QRect(0, 0, 1561, 90))
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
        self.label.setGeometry(QtCore.QRect(720, 30, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_fanhui = QtWidgets.QPushButton(self.frame_menu)
        self.pushButton_fanhui.setGeometry(QtCore.QRect(60, 30, 81, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.pushButton_fanhui.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_fanhui.setFont(font)
        self.pushButton_fanhui.setStyleSheet("QPushButton{\n"
"    border:none\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    background-color:rgb(189, 189, 189);\n"
"}\n"
"")
        self.pushButton_fanhui.setObjectName("pushButton_fanhui")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(-10, 90, 1571, 771))
        self.frame.setStyleSheet("QFrame{\n"
"    background-color:rgb(203, 203, 203)\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.tableWidget_excel = QtWidgets.QTableWidget(self.frame)
        self.tableWidget_excel.setGeometry(QtCore.QRect(20, 30, 911, 651))
        self.tableWidget_excel.setObjectName("tableWidget_excel")
        self.tableWidget_tezhengzhi = QtWidgets.QTableWidget(self.frame)
        self.tableWidget_tezhengzhi.setGeometry(QtCore.QRect(980, 30, 551, 651))
        self.tableWidget_tezhengzhi.setObjectName("tableWidget_tezhengzhi")
        self.tableWidget_tezhengzhi.setColumnCount(6)
        self.tableWidget_tezhengzhi.setRowCount(14)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_tezhengzhi.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_tezhengzhi.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_tezhengzhi.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_tezhengzhi.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_tezhengzhi.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_tezhengzhi.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_tezhengzhi.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_tezhengzhi.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_tezhengzhi.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_tezhengzhi.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_tezhengzhi.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_tezhengzhi.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_tezhengzhi.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_tezhengzhi.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_tezhengzhi.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_tezhengzhi.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_tezhengzhi.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_tezhengzhi.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_tezhengzhi.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_tezhengzhi.setHorizontalHeaderItem(5, item)
        self.tableWidget_tezhengzhi.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_tezhengzhi.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget_tezhengzhi.verticalHeader().setStretchLastSection(True)
        self.tableWidget_excel.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_excel.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget_excel.verticalHeader().setStretchLastSection(True)
        self.pushButton_huitu = QtWidgets.QPushButton(self.frame)
        self.pushButton_huitu.setGeometry(QtCore.QRect(720, 700, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_huitu.setFont(font)
        self.pushButton_huitu.setObjectName("pushButton_huitu")
        self.frame.raise_()
        self.frame_menu.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)




    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "数据库管理"))
        self.pushButton_fanhui.setText(_translate("Dialog", "返回"))
        item = self.tableWidget_tezhengzhi.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "均值"))
        item = self.tableWidget_tezhengzhi.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "方差"))
        item = self.tableWidget_tezhengzhi.verticalHeaderItem(2)
        item.setText(_translate("Dialog", "标准差"))
        item = self.tableWidget_tezhengzhi.verticalHeaderItem(3)
        item.setText(_translate("Dialog", "最大值"))
        item = self.tableWidget_tezhengzhi.verticalHeaderItem(4)
        item.setText(_translate("Dialog", "最小值"))
        item = self.tableWidget_tezhengzhi.verticalHeaderItem(5)
        item.setText(_translate("Dialog", "峰值"))
        item = self.tableWidget_tezhengzhi.verticalHeaderItem(6)
        item.setText(_translate("Dialog", "均方根值"))
        item = self.tableWidget_tezhengzhi.verticalHeaderItem(7)
        item.setText(_translate("Dialog", "方根幅值"))
        item = self.tableWidget_tezhengzhi.verticalHeaderItem(8)
        item.setText(_translate("Dialog", "波形指标"))
        item = self.tableWidget_tezhengzhi.verticalHeaderItem(9)
        item.setText(_translate("Dialog", "峰值指标"))
        item = self.tableWidget_tezhengzhi.verticalHeaderItem(10)
        item.setText(_translate("Dialog", "脉冲指标"))
        item = self.tableWidget_tezhengzhi.verticalHeaderItem(11)
        item.setText(_translate("Dialog", "裕度指标"))
        item = self.tableWidget_tezhengzhi.verticalHeaderItem(12)
        item.setText(_translate("Dialog", "偏斜度"))
        item = self.tableWidget_tezhengzhi.verticalHeaderItem(13)
        item.setText(_translate("Dialog", "峭度"))

        item = self.tableWidget_tezhengzhi.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "大气舱绝压(kPaA)\n"
""))
        item = self.tableWidget_tezhengzhi.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "高度(m)\n"
""))
        item = self.tableWidget_tezhengzhi.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "座舱绝压(kPaA)\n"
""))
        item = self.tableWidget_tezhengzhi.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "座舱余压(kPaA)\n"
""))
        item = self.tableWidget_tezhengzhi.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "总流量(kg/h)\n"
""))
        item = self.tableWidget_tezhengzhi.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "控制腔压力(kPaA)\n"
""))
        self.pushButton_huitu.setText(_translate("Dialog", "绘图"))



    def loadData(self):
        if SharedData().get_file_path():
            df = pd.read_excel(SharedData().get_file_path())
            if df is not None:
                self.tableWidget_excel.setRowCount(df.shape[0])
                self.tableWidget_excel.setColumnCount(df.shape[1])
                self.tableWidget_excel.setHorizontalHeaderLabels(df.columns)

                for i in range(df.shape[0]):
                    for j in range(df.shape[1]):
                        self.tableWidget_excel.setItem(i, j, QTableWidgetItem(str(df.iat[i, j])))


        else:
            self.showMessage("错误", f"未找到文件")


    def showMessage(self, title, message):
        # 显示消息框
        msgBox = QMessageBox()
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.exec_()

    def get_excel_feature(self,path):
        '''
        :param column: 需要读取的excel列
        :param data: excel表格数据
        :return:
        '''
        feature = []
        column = ['大气舱绝压(kPaA)', '高度(m)', '座舱绝压(kPaA)', '座舱余压(kPaA)', '总流量(kg/h)', '控制腔压力(kPaA)']

        # 定义获取某一列的时域特征的函数，输入为一维的Dataframe格式的数据
        def get_time_domain_features(data):
            '''data为一维振动信号'''
            fea = []
            len_ = len(data)
            mean_ = data.mean()  # 1.均值
            var_ = data.var()  # 2.方差
            std_ = data.std()  # 3.标准差
            max_ = data.max()  # 4.最大值
            min_ = data.min()  # 5.最小值
            x_p = max(abs(max_), abs(min_))  # 峰值
            x_rms = math.sqrt((data ** 2).sum() / len_)  # 均方根值
            x_r = ((abs(data) ** 0.5).sum() / len_) ** 2  # 方根幅值
            W = x_rms / mean_  # 波形指标
            C = x_p / x_rms  # 峰值指标
            I = x_p / mean_  # 脉冲指标
            L = x_p / x_r  # 裕度指标
            S = ((data - mean_) ** 3).sum() / ((len_ - 1) * std_ ** 3)  # 偏斜度
            K = ((data - mean_) ** 4).sum() / ((len_ - 1) * std_ ** 4)  # 峭度
            fea = [mean_, var_, std_, max_, min_, x_p, x_rms, x_r, W, C, I, L, S, K]
            return fea
        data = pd.read_excel(path)
        for i in column:
            feature.append(get_time_domain_features(data[i]))
        feature = np.concatenate(feature, axis=0)
        return feature.reshape(14, 6)



    def write_to_tezheng_table(self):
        if SharedData().get_file_path():
            data = self.get_excel_feature(SharedData().get_file_path())
            for i in range(self.tableWidget_tezhengzhi.rowCount()):
                for j in range(self.tableWidget_tezhengzhi.columnCount()):
                    if i < data.shape[0] and j < data.shape[1]:
                        item = QTableWidgetItem(str(data[i, j]))
                        self.tableWidget_tezhengzhi.setItem(i, j, item)


