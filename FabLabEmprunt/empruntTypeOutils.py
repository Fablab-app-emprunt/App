from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QMessageBox
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from FabLabEmprunt.empruntajout import *
from FabLabEmprunt.pageAccueil import *

# importation de la classe pyqtSignal afin de permettre à la fenêtre d'envoyer des données vers une autre fenêtre
from PyQt5.QtCore import pyqtSignal

class EmpruntTypeOutils(QWidget):
    signal = pyqtSignal(str)
    def __init__(self):
        super(EmpruntTypeOutils, self).__init__()
        loadUi('empruntTypeOutils.ui', self)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('Capture d’écran 2022-04-14 153417.png'))
        self.boutonaccueil.setIcon(icon)
        self.bouton_electronique.clicked.connect(self.elec)
        self.bouton_bois.clicked.connect(self.bois)
        self.bouton_usinage.clicked.connect(self.usinage)
        self.boutonaccueil.clicked.connect(self.accueil)
        # self.fenetre_choix_outils = EmpruntAjout()
        # self.page_accueil = PageAccueil()

    def accueil(self):
        print(self.boutonaccueil.text())
        self.signal.emit(self.boutonaccueil.text())
        self.close()


    def bois(self):
        # self.fenetre_choix_outils.show()
        # self.hide()
        pass

    def elec(self):
        # self.fenetre_choix_outils.show()
        # self.hide()
        pass

    def usinage(self):
        # self.fenetre_choix_outils.show()
        # self.hide()
        pass










if __name__== "__main__":
    app = QApplication([])
    empruntTypeOutils = EmpruntTypeOutils()
    empruntTypeOutils.show()
    app.exec_()

