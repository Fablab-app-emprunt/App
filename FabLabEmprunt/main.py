# import os
# os.system('pip install -r requirements.txt')


if __name__ == "__main__":
    import sys
    from PyQt5 import QtWidgets
    from PyQt5.QtWidgets import QApplication

    requete_Outils = ''
    Requete_Outils = ['ELEC', 'BOIS', 'USINAGE']
    page_choix_outils = ['page_choix_outils_elec', 'page_choix_outils_bois', 'page_choix_outils_usinage']
    Data = []
    Lelec = []
    Lbois = []
    Lusinage = []
    Lfinal = []

    app = QApplication(sys.argv)

    from FabLabEmprunt.pageAccueil import PageAccueil
    from FabLabEmprunt.empruntTypeOutils import EmpruntTypeOutils

    widget = QtWidgets.QStackedWidget()

    page_accueil = PageAccueil()
    page_choix_type_outils = EmpruntTypeOutils()

    widget.addWidget(page_accueil)
    widget.addWidget(page_choix_type_outils)

    widget.setFixedHeight(700)
    widget.setFixedWidth(1000)
    widget.show()

    print("Index Accueil : ", widget.indexOf(page_accueil))

    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")
