from PyQt5.QtWidgets import QWidget #,QApplication


class EmpruntTypeOutils(QWidget):

    def __init__(self):
        from PyQt5 import QtGui
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
        self.rendreOutils_4.clicked.connect(self.validate)

    def accueil(self):
        from main import widget
        widget.setCurrentIndex(0)

    def elec(self):
        from main import widget, requete_Outils
        print(requete_Outils)
        requete_Outils = 'ELEC'
        widget.setCurrentIndex(2)

    def bois(self):
        from main import widget
        widget.setCurrentIndex(3)
        global requete_Outils
        requete_Outils = 'BOIS'

    def usinage(self):
        from main import widget
        widget.setCurrentIndex(4)
        global requete_Outils
        requete_Outils = 'USINAGE'

    def validate(self):
        from popUpListeEmprunts import PopUpListeEmpruntsWidget
        from main import widget, Lelec, Lbois, Lusinage
        Lfinal = []
        for i in range(len(Lelec)):
            Lfinal.append(Lelec[i])
        for i in range(len(Lbois)):
            Lfinal.append(Lbois[i])
        for i in range(len(Lusinage)):
            Lfinal.append(Lusinage[i])
        print("Lfinal", Lfinal)
        pop_up = PopUpListeEmpruntsWidget()
        widget.insertWidget(5, pop_up)
        print("Index of : pop up is ", widget.indexOf(pop_up))
        widget.setCurrentIndex(5)


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     widget = QtWidgets.QStackedWidget()
#
#     emprunt_type_outils = EmpruntTypeOutils()
#
#     widget.addWidget(emprunt_type_outils)
#     widget.setFixedHeight(700)
#     widget.setFixedWidth(1000)
#     widget.show()
#
#     try:
#         sys.exit(app.exec_())
#     except:
#         print("Exiting")
