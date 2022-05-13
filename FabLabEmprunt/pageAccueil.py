from PyQt5.QtWidgets import QWidget

class PageAccueil(QWidget):
    def __init__(self):
        from PyQt5.uic import loadUi
        super(PageAccueil, self).__init__()
        loadUi('pageAccueil.ui', self)
        self.rendreoutils.clicked.connect(self.goToRendreOutils)
        self.emprunteroutils.clicked.connect(self.goToEmprunterOutils)

    def goToRendreOutils(self):
        from rendreOutil import RendreOutils
        from main import widget, page_choix_type_outils
        print("Index rendreoutils : ", widget.indexOf(page_choix_type_outils))
        page_rendre_outils = RendreOutils()
        widget.addWidget(page_rendre_outils)
        widget.setCurrentWidget(page_rendre_outils)

    def goToEmprunterOutils(self):
        print("test")
        from FabLabEmprunt.main import page_choix_type_outils,widget
        widget.setCurrentWidget(page_choix_type_outils)
        # print("Index emprunteroutils : ", widget.indexOf(page_choix_type_outils))
        # self.creationPages()

    def creationPages(self):
        from empruntajout import EmpruntAjout
        from main import requete_Outils, Requete_Outils, page_choix_outils, widget
        # ----------------CREATION PAGES ELEC BOIS USINAGE--------------------------------
        print(requete_Outils)
        for i in range(3):
            requete_Outils = Requete_Outils[i]
            print(requete_Outils)
            page_choix_outils[i] = EmpruntAjout()
            widget.insertWidget(i + 2, page_choix_outils[i])
            # print("Index of : ", requete_Outils, ' is ', widget.indexOf(page_choix_outils[i]))

# if __name__ == "__main__":
#
#     app = QApplication(sys.argv)
#     widget = QtWidgets.QStackedWidget()
#
#     page_accueil = PageAccueil()
#     page_choix_type_outils = EmpruntTypeOutils()
#     # page_choix_outils = EmpruntAjout()
#
#     widget.addWidget(page_accueil)
#     widget.addWidget(page_choix_type_outils)
#     # widget.addWidget(page_choix_outils)
#
#     widget.setFixedHeight(700)
#     widget.setFixedWidth(1000)
#     widget.show()
#     print("Index Accueil : ", widget.indexOf(page_accueil))
#
#     try:
#         sys.exit(app.exec_())
#     except:
#         print("Exiting")
