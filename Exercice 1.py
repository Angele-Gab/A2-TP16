from PySide2.QtWidgets import *
from random import *

class Test (QWidget) :
    def __init__(self):
        QWidget.__init__(self)
        self.setFixedSize(500,300)
        self.setWindowTitle("Cycles de l'ISEN Yncrea Ouest")

        self.layout = QVBoxLayout()
        self.label = QLabel()
        self.button = QPushButton("Changer le cycle")

        self.liste =["CSI", "CIR", "BIOST", "CENT", "BIAST", "EST"]



        self.button.clicked.connect(self.buttonClicked)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)

    def buttonClicked(self):
        self.label.setText(choice(self.liste))
        self.show()

if __name__ == "__main__":
   app = QApplication([])
   win = Test()
   win.show()
   app.exec_()



