from PySide2.QtWidgets import *
from PySide2.QtCore import *

class Test(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("IHM")
        self.setMinimumSize(500, 300)

        self.layout = QHBoxLayout()
        self.Barre = QProgressBar()
        self.Curseur = QSlider(Qt.Vertical)
        self.layout.addWidget(self.Barre)
        self.layout.addWidget(self.Curseur)
        self.Curseur.valueChanged.connect(self.Changeprogressbar)
        self.setLayout(self.layout)

    def Changeprogressbar(self):
        self.Barre.setValue(self.Curseur.value())
        return

if __name__ == "__main__":
    app = QApplication([])
    win = Test()
    win.show()
    app.exec_()
