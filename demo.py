import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget

class SignalManager(QObject):
    button_added = pyqtSignal()

    def emit_button_added(self):
        self.button_added.emit()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('主窗口')
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.addButton = QPushButton('增加按钮')
        self.layout.addWidget(self.addButton)

        # 创建信号管理器实例
        self.signal_manager = SignalManager()

        # 连接按钮的 clicked 信号到槽函数
        self.addButton.clicked.connect(self.emit_button_added)

    def emit_button_added(self):
        # 发射自定义信号，通知另一个窗口增加按钮
        self.signal_manager.emit_button_added()


class AnotherWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('另一个窗口')
        self.setGeometry(500, 100, 400, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        # 初始化时没有按钮，等待信号触发后增加按钮
        self.buttons = []

        # 创建信号管理器实例
        self.signal_manager = SignalManager()
        # 连接信号管理器的信号到槽函数
        self.signal_manager.button_added.connect(self.add_button)

    def add_button(self):
        # 增加按钮的方法
        new_button = QPushButton(f'按钮 {len(self.buttons) + 1}')
        self.layout.addWidget(new_button)
        self.buttons.append(new_button)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow()
    another_window = AnotherWindow()

    # 将信号管理器实例传递给主窗口和另一个窗口
    main_window.signal_manager.button_added.connect(another_window.add_button)

    main_window.show()
    another_window.show()

    sys.exit(app.exec_())
