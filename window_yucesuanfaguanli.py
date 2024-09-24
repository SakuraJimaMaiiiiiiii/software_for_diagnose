from PyQt5.QtWidgets import QMessageBox, QGraphicsScene,QDialog,QLabel,QVBoxLayout
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton
import matplotlib
from PyQt5.QtGui import QPixmap
matplotlib.use('Qt5Agg')



class yuceguanli(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1554, 865)
        Dialog.setStyleSheet("QDialog{\n"
"    background-color:white\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    color:black;\n"
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
        self.label_biaoti = QtWidgets.QLabel(self.frame_menu)
        self.label_biaoti.setGeometry(QtCore.QRect(700, 20, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label_biaoti.setFont(font)
        self.label_biaoti.setObjectName("label_biaoti")
        self.pushButton_fanhui = QtWidgets.QPushButton(self.frame_menu)
        self.pushButton_fanhui.setGeometry(QtCore.QRect(50, 30, 81, 41))
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
        self.frame.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setStyleSheet("QFrame{\n"
"    background-color:rgb(203, 203, 203)\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(0, 0, 1001, 16))
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(110, 30,1300, 250))
        self.tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
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
        self.label_suanfaxiangqing = QtWidgets.QLabel(self.frame)
        self.label_suanfaxiangqing.setGeometry(QtCore.QRect(110, 330, 140, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_suanfaxiangqing.setFont(font)
        self.label_suanfaxiangqing.setObjectName("label_suanfaxiangqing")
        self.QTextEdit = QtWidgets.QTextEdit(self)
        self.QTextEdit.setGeometry(QtCore.QRect(105, 480, 1300, 300))
        self.QTextEdit.setStyleSheet(f"QTextEdit {{ font-size: {25}px; }}")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        for row in range(self.tableWidget.rowCount()):
            btn = QPushButton('查看')
            btn.clicked.connect(self.viewButtonClicked)
            self.tableWidget.setCellWidget(row, 4, btn)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_biaoti.setText(_translate("Dialog", "预测算法管理"))
        self.pushButton_fanhui.setText(_translate("Dialog", "返回"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "卷积神经网络"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "算法2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Dialog", "算法3"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "版本号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "导入人"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "导入日期"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "推荐程度"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "算法查看"))
        self.label_suanfaxiangqing.setText(_translate("Dialog", "算法详情："))


        item = QtWidgets.QTableWidgetItem("V1.0")
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem("小谢")
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem("2024/6/24")
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem("⭐⭐⭐⭐⭐")
        self.tableWidget.setItem(0, 3, item)



    def viewButtonClicked(self):
        # 获取按钮所在的行
        button = self.sender()
        if button:
            index = self.tableWidget.indexAt(button.pos())
            if index.isValid():
                row = index.row()
                QMessageBox.information(self, '算法查看', f'查看算法：{self.tableWidget.verticalHeaderItem(row).text()}')
                if row == 0:
                    pixmap = QPixmap("pic/CNN.png")
                    if not pixmap.isNull():
                        scene = QGraphicsScene()
                        scene.addPixmap(pixmap)
                        self.QTextEdit.setText('卷积块参数:Conv1d(64,64,kernel_size=3，stride=1，padding=1，bias=False)\n'
                                               '全连接层参数：Dropout(p=0.5,inplace=False)，Linear(in_features=512, out_features=1024, bias=True)')

                        self.image_dialog = QDialog()
                        self.image_dialog.setWindowTitle("故障示意图")
                        layout = QVBoxLayout()
                        label = QLabel(self.image_dialog)
                        pic_path = pixmap
                        pixmap = QPixmap(pic_path)  # 替换为你的图片路径
                        label.setPixmap(pixmap)
                        layout.addWidget(label)
                        self.image_dialog.setLayout(layout)
                        self.image_dialog.exec_()