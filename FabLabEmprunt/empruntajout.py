from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QMessageBox
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
# importation de la classe pyqtSignal afin de permettre à la fenêtre d'envoyer des données vers une autre fenêtre
from PyQt5.QtCore import pyqtSignal
class EmpruntAjout(QWidget):
    def __init__(self):
        super(EmpruntAjout, self).__init__()
        loadUi('empruntAjout.ui',self)
        # self.boutonaccueil.clicked.connect(self.accueil)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('Capture d’écran 2022-04-14 153417.png'))
        self.boutonaccueil.setIcon(icon)
        self.today.clicked.connect(self.date)
        self.dateemprunt.clicked.connect(self.date)
    #     self.page_accueil = PageAccueil()
    #
    # def accueil(self):
    #     self.page_accueil.show()
    #     self.hide()

    def date(self):
        value = self.today.selectedDate()
        return value

if __name__ == "__main__":
    app = QApplication([])
    emprunt = EmpruntAjout()
    emprunt.show()
    app.exec_()