from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QSizePolicy

class Mainwindow(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1554, 865)
        Dialog.setStyleSheet("QDialog{\n"
"    background-color:rgb(234, 242, 255)\n"
"}")
        self.frame_menu = QtWidgets.QFrame(Dialog)
        self.frame_menu.setGeometry(QtCore.QRect(0, 0, 1561, 90))
        sizePolicy = QtWidgets.QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_menu.sizePolicy().hasHeightForWidth())
        self.frame_menu.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.frame_menu.setStyleSheet("QFrame{\n"
"    background-color:rgb(226, 226, 226)\n"
"}")
        self.frame_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_menu.setObjectName("frame_menu")
        self.pushButton_shujuku = QtWidgets.QPushButton(self.frame_menu)
        self.pushButton_shujuku.setGeometry(QtCore.QRect(340, 20, 160, 50))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(13)
        self.pushButton_shujuku.setFont(font)
        self.pushButton_shujuku.setStyleSheet("QPushButton{\n"
"    background-color:rgb(194, 194, 194);\n"
"    border:none\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    background-color:rgb(218, 255, 212);\n"
"}\n"
"")
        self.pushButton_shujuku.setObjectName("pushButton_shujuku")
        self.pushButton_suanfa = QtWidgets.QPushButton(self.frame_menu)
        self.pushButton_suanfa.setGeometry(QtCore.QRect(740, 20, 160, 50))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(13)
        self.pushButton_suanfa.setFont(font)
        self.pushButton_suanfa.setStyleSheet("QPushButton{\n"
"    background-color:rgb(194, 194, 194);\n"
"    border:none\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    background-color:rgb(218, 255, 212);\n"
"}\n"
"")
        self.pushButton_suanfa.setObjectName("pushButton_suanfa")
        self.pushButton_zhenduan = QtWidgets.QPushButton(self.frame_menu)
        self.pushButton_zhenduan.setGeometry(QtCore.QRect(1140, 20, 160, 50))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(13)
        self.pushButton_zhenduan.setFont(font)
        self.pushButton_zhenduan.setStyleSheet("QPushButton{\n"
"    background-color:rgb(194, 194, 194);\n"
"    border:none\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    background-color:rgb(218, 255, 212);\n"
"}\n"
"")
        self.pushButton_zhenduan.setObjectName("pushButton_zhenduan")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(-10, 90, 1571, 771))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 1571, 771))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap('pic/mainpic.jpg'))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_title = QtWidgets.QLabel(self.frame)
        self.label_title.setGeometry(QtCore.QRect(20, 20, 581, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(245, 245, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 245, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_title.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(24)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.frame.raise_()
        self.frame_menu.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)




    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_shujuku.setText(_translate("Dialog", "数据库管理"))
        self.pushButton_suanfa.setText(_translate("Dialog", "算法管理"))
        self.pushButton_zhenduan.setText(_translate("Dialog", "故障诊断及预测"))
        self.label_title.setText(_translate("Dialog", "飞机座舱压力调节地面维护系统"))


