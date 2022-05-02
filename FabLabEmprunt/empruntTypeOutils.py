import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtWidgets import QDialog, QApplication, QLabel, QWidget, QMessageBox

# from FabLabEmprunt.empruntajout import EmpruntAjout
# from FabLabEmprunt.pageAccueil import PageAccueil

class EmpruntTypeOutils(QDialog):
    def __init__(self):
        from PyQt5.uic import loadUi
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
        # page_accueil = PageAccueil()
        # widget.addWidget(page_accueil)
        # print(widget.currentIndex())
        # widget.setCurrentIndex(widget.currentIndex()+1)
        # print(widget.currentIndex())

        widget.setCurrentIndex(0)


    def bois(self):
        # outils_bois = EmpruntAjout()
        # widget.addWidget(outils_bois)
        # widget.setCurrentIndex(widget.currentIndex()+1)

        widget.setCurrentIndex(2)

    def elec(self):
        # outils_elec = EmpruntAjout()
        # widget.addWidget(outils_elec)
        # widget.setCurrentIndex(widget.currentIndex()+1)

        widget.setCurrentIndex(2)

    def usinage(self):
        # outils_usinage = EmpruntAjout()
        # widget.addWidget(outils_usinage)
        # widget.setCurrentIndex(widget.currentIndex()+1)

        widget.setCurrentIndex(2)


if __name__== "__main__":
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()

    emprunt_type_outils = EmpruntTypeOutils()

    widget.addWidget(emprunt_type_outils)
    widget.setFixedHeight(700)
    widget.setFixedWidth(1000)
    widget.show()

    try:
        sys.exit(app.exec_())
    except :
        print("Exiting")

