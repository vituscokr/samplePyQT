# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QWidget , QPushButton, QMainWindow
from PySide6.QtCore import QSize, Qt
from random import choice


#https://www.pythonguis.com/tutorials/pyside6-creating-your-first-window/

window_titles = [
    '갑',
    '을',
    '병',
    '정',
    '무',
    '기',
    '경',
    '신',
    '임',
    '계',
]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.button = QPushButton("Press Me!")
#        self.button.setCheckable(True)
        self.button.clicked.connect(self.clicked_button)
        self.windowTitleChanged.connect(self.changed_window_title)
#        self.button.clicked.connect(self.toggled_button)
        self.setFixedSize(QSize(400, 300))
        self.setCentralWidget(self.button)


    def clicked_button(self):
#        self.button.setText('이미 클릭했습니다.')
#        self.button.setEnabled(False)
#        self.setWindowTitle("My Oneshot App")
#        print('clicked')
        new_window_title = choice(window_titles)
        self.setWindowTitle(new_window_title)

    def toggled_button(self, checked):
        print("checked: ", checked)

    def changed_window_title(self, window_title):
        print(f"Window title Changed : {window_title}")
        if window_title =='계' :
            self.button.setDisabled(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
#    loader = QUiLoader()
#    window = loader.load('ui/mainwindow.ui', None)
#    window.show()

    window = MainWindow()
    window.show()

    app.exec()

    # ...
    # sys.exit(app.exec())
