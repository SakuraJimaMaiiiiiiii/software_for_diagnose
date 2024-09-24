from PyQt5.QtWidgets import QPushButton, QFileDialog,  QTableWidgetItem, QMessageBox, QVBoxLayout
from PyQt5 import QtCore, QtGui, QtWidgets
import os
from datetime import datetime
import subprocess
from shared_data import SharedData
import pandas as pd
import globals

class shujuguanli(object):
    def __init__(self):
        super().__init__()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1554, 865)
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
        self.label.setGeometry(QtCore.QRect(700, 30, 141, 41))
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

        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(13)

        self.pushButton_duquwenjian = QtWidgets.QPushButton(self.frame)
        self.pushButton_duquwenjian.setGeometry(QtCore.QRect(1300, 120, 120, 55))
        self.pushButton_duquwenjian.setObjectName("pushButton_duquwenjian")
        self.pushButton_duquwenjian.setFont(font)
        self.pushButton_jinrushujuku = QtWidgets.QPushButton(self.frame)
        self.pushButton_jinrushujuku.setGeometry(QtCore.QRect(1300, 600, 120, 55))
        self.pushButton_jinrushujuku.setObjectName("pushButton_jinrushujuku")
        self.pushButton_jinrushujuku.clicked.connect(self.open_SQL)
        self.pushButton_jinrushujuku.setFont(font)

        self.pushButton_chakanshuju = QtWidgets.QPushButton(self.frame)
        self.pushButton_chakanshuju.setGeometry(QtCore.QRect(1300,360, 120, 55))
        self.pushButton_chakanshuju.setObjectName("pushButton_chakanshuju")
        self.pushButton_chakanshuju.setFont(font)


        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(190, 40, 900, 700))
        self.tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget.setAutoFillBackground(True)
        self.tableWidget.setStyleSheet("QtableWidget\n"
"{\n"
"    background-color:white\n"
"}\n"
"\n"
"\n"
"QTableWidget::item {\n"
"    color: black;\n"
"}\n"
"")
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.frame.raise_()
        self.frame_menu.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # 初始化

        self.selectedFile = None


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "数据库管理"))
        self.pushButton_fanhui.setText(_translate("Dialog", "返回"))
        self.pushButton_duquwenjian.setText(_translate("Dialog", "读取文件"))
        self.pushButton_jinrushujuku.setText(_translate("Dialog", "进入MySQL"))
        self.pushButton_chakanshuju.setText(_translate("Dialog", "查看数据"))
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setHorizontalHeaderLabels(['编号', '文件路径', '添加日期', '操作', '选择'])
        self.pushButton_duquwenjian.clicked.connect(self.openFileDialog)




    def openFileDialog(self):
        # 打开文件对话框，选择文件
        options = QFileDialog.Options()
        fileNames, _ = QFileDialog.getOpenFileName(self, "选择Excel文件", "", "Excel文件 (*.xlsx *.xls)", options=options)
        if fileNames:
            self.selectedFile = fileNames
            globals.filepaths.append(fileNames)
            rowPosition = self.tableWidget.rowCount()
            file_path = os.path.abspath(fileNames)


            # 插入一行
            self.tableWidget.insertRow(rowPosition)

            # 编号
            item = QTableWidgetItem(str(rowPosition + 1))
            self.tableWidget.setItem(rowPosition, 0, item)

            # 文件路径
            self.tableWidget.setItem(rowPosition, 1, QTableWidgetItem(file_path))

            # 添加日期
            self.current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.tableWidget.setItem(rowPosition, 2, QTableWidgetItem(self.current_time))

            # 删除操作按钮
            deleteButton = QPushButton('删除')
            deleteButton.clicked.connect(lambda _, row=rowPosition: self.deleteRow(row))
            self.tableWidget.setCellWidget(rowPosition, 3, deleteButton)

            # 选择文件按钮
            Button_chakan = QPushButton('选择')
            Button_chakan.clicked.connect(lambda _, row=rowPosition: self.remember_choose_filepath(row))
            self.tableWidget.setCellWidget(rowPosition, 4, Button_chakan)




    def deleteRow(self, row):
        # 删除指定行
        self.tableWidget.removeRow(row)
        globals.filepaths.pop(row-1)

    def open_SQL(self):
        # 打开SQL管理程序
        SQL_path = r'D:\MySQL\sqlyog\SQLyog.exe'
        if SQL_path:
           subprocess.Popen(SQL_path)
        else:
           self.showMessage("错误", f"未找到程序")


    def remember_choose_filepath(self, row):
        filePath = self.tableWidget.item(row, 1).text()  # 获取当前行文件路径列的值
        SharedData().set_file_path(filePath)
        try:
            pd.read_excel(filePath)
            self.showMessage("成功", f"读取文件成功")
        except Exception as e:
            self.showMessage("错误", f"未选择到文件")


    def showMessage(self, title, message):
        # 显示消息框
        msgBox = QMessageBox()
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = shujuguanli()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())






