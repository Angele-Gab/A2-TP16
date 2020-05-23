from PySide2.QtWidgets import *
from PySide2.QtCore import *

class Test(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("IHM")
        self.setMinimumSize(500, 300)
        self.layout = QVBoxLayout()
        self.compteur = 0
        self.label = "Changer mon texte ! "
        self.button = QPushButton(self.label)

        self.notificationPanel = QTextEdit("Le nombre de clic va être affiché ici")


        self.layout.addWidget(self.button)
        self.layout.addWidget(self.notificationPanel)
        self.button.clicked.connect(self.ButtonClicked)
        self.layout.addWidget(self.notificationPanel)

        self.setLayout(self.layout)


    #def ButtonClicked (self) :
        #self.close()

    def ButtonClicked(self):
        self.compteur += 1
        newlabel = str(self.compteur)
        self.notificationPanel.setText("Clic " + newlabel)
        self.button.setText("Clic " + newlabel)




if __name__ == "__main__":
    app = QApplication([])
    win = Test()
    win.show()
    app.exec_()
