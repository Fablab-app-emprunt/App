from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QMessageBox
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
# importation de la classe pyqtSignal afin de permettre à la fenêtre d'envoyer des données vers une autre fenêtre
from PyQt5.QtCore import pyqtSignal
from FabLabEmprunt.empruntTypeOutils import *

class PageAccueil(QWidget):
    def __init__(self, second):
        super(PageAccueil,self).__init__()
        self.second = second
        loadUi('pageAccueil.ui',self)
        self.rendreoutils.clicked.connect(self.rendreOutils)
        self.emprunteroutils.clicked.connect(self.emprunterOutils)


    def rendreOutils(self):
        self.close() # ferme la première fenêtre
        self.second.show() # Affiche la deuxième fenêtre



    def emprunterOutils(self):
        self.close() # ferme la première fenêtre
        self.second.show() # Affiche la deuxième fenêtre





if __name__ == "__main__":
    app = QApplication([])
    monIHM = PageAccueil()
    monIHM.show()
    app.exec_()