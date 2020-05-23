from PySide2.QtWidgets import *
from PySide2.QtCore import *

class Test(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("IHM")
        self.setMinimumSize(500, 300)
        self.layout = QHBoxLayout()
        self.button = QPushButton("Changer mon texte ! ")

        self.layout.addWidget(self.button)
        self.button.clicked.connect(self.ButtonClicked)
        self.setLayout(self.layout)


    def ButtonClicked (self) :
        self.close()

if __name__ == "__main__":
    app = QApplication([])
    win = Test()
    win.show()
    app.exec_()
