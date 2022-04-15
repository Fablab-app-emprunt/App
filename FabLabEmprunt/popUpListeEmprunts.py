from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QRadioButton, QPushButton
from PyQt5.uic import loadUi

from FabLabEmprunt.pageAccueil import PageAccueil


class PopUpListeEmpruntsWidget(QWidget):
    def __init__(self):
        super(PopUpListeEmpruntsWidget, self).__init__()
        loadUi('popUpListeEmprunts.ui', self)
        self.boutoncroix.clicked.connect(self.reponseCroix)
        self.boutonconfirmer.clicked.connect(self.reponseConfirmer)
        self.pageAccueil = PageAccueil()


    def reponseConfirmer(self):

        self.pageAccueil.show()
        self.close()

    def reponseCroix(self):
        self.close()








if __name__== "__main__":
    app = QApplication([])
    popUpListeEmprunts = PopUpListeEmpruntsWidget()
    popUpListeEmprunts.show()
    app.exec_()