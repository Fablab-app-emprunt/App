import sys
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QApplication, QLabel, QWidget, QMessageBox

class PageAccueil(QWidget):
    def __init__(self):
        super(PageAccueil,self).__init__()
        loadUi('pageAccueil.ui',self)
        self.rendreoutils.clicked.connect(self.goToRendreOutils)
        self.emprunteroutils.clicked.connect(self.goToEmprunterOutils)

    def goToRendreOutils(self):
        widget.setCurrentIndex(1)

    def goToEmprunterOutils(self):
        widget.setCurrentIndex(1)


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
        self.boutonaccueil.clicked.connect(self.accueil)


    def accueil(self):
        widget.setCurrentIndex(0)


    def bois(self):
        widget.setCurrentIndex(2)

    def elec(self):
        widget.setCurrentIndex(2)

    def usinage(self):
        widget.setCurrentIndex(2)

# from pageAccueil import PageAccueil
# from empruntTypeOutils import EmpruntTypeOutils
# from empruntajout import EmpruntAjout

class EmpruntAjout(QWidget):
    def __init__(self):
        super(EmpruntAjout, self).__init__()
        loadUi('empruntAjout.ui',self)
        self.boutonaccueil.clicked.connect(self.accueil)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('Capture d’écran 2022-04-14 153417.png'))
        self.boutonaccueil.setIcon(icon)
        self.today.clicked.connect(self.date)
        self.dateemprunt.clicked.connect(self.date)

    def accueil(self):
       widget.setCurrentIndex(0)

    def date(self):
        value = self.today.selectedDate()
        return value


if __name__ == "__main__":

    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()

    # from FabLabEmprunt.pageAccueil import PageAccueil
    # from FabLabEmprunt.empruntTypeOutils import EmpruntTypeOutils
    # from FabLabEmprunt.empruntajout import EmpruntAjout

    page_accueil = PageAccueil()
    page_choix_type_outils = EmpruntTypeOutils()
    page_choix_outils = EmpruntAjout()

    widget.addWidget(page_accueil)
    widget.addWidget(page_choix_type_outils)
    widget.addWidget(page_choix_outils)

    widget.setFixedHeight(700)
    widget.setFixedWidth(1000)
    widget.show()

    try:
        sys.exit(app.exec_())
    except :
        print("Exiting")