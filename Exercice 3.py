from PySide2.QtWidgets import *
from PySide2.QtCore import *

class Test(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("IHM")
        self.setMinimumSize(500, 300)
        self.layout = QHBoxLayout()
        self.compteur = 0
        self.label = "Changer mon texte ! "
        self.button = QPushButton(self.label)

        self.layout.addWidget(self.button)
        self.button.clicked.connect(self.ButtonClicked)
        self.setLayout(self.layout)


    #def ButtonClicked (self) :
        #self.close()

    def ButtonClicked(self):
        self.compteur += 1
        newlabel = str(self.compteur)
        self.button.setText("Click " + newlabel)


if __name__ == "__main__":
    app = QApplication([])
    win = Test()
    win.show()
    app.exec_()
