from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QRadioButton, QPushButton
from PyQt5.uic import loadUi
from PyQt5 import QtGui,QtCore
# from FabLabEmprunt.empruntajout import EmpruntAjout
class EmpruntTypeOutils(QWidget):
    def __init__(self):
        super(EmpruntTypeOutils, self).__init__()
        loadUi('empruntTypeOutils.ui', self)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('Capture d’écran 2022-04-14 153417.png'))
        self.boutonaccueil.setIcon(icon)
        self.bouton_electronique.clicked.connect(self.elec)
        self.bouton_bois.clicked.connect(self.bois)
        self.bouton_usinage.clicked.connect(self.usinage)
        self.fenetre_choix_outils = EmpruntAjout()

    def bois(self):
        self.fenetre_choix_outils.show()
        self.close()

    def elec(self):
        self.fenetre_choix_outils.show()
        self.close()

    def usinage(self):
        self.fenetre_choix_outils.show()
        self.close()










if __name__== "__main__":
    app = QApplication([])
    empruntTypeOutils = EmpruntTypeOutils()
    empruntTypeOutils.show()
    app.exec_()

