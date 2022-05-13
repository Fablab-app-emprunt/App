# import os
# os.system('pip install -r requirements.txt')
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication#, QMainWindow
# from PyQt5.uic import loadUi


# class MainScreen(QMainWindow):
#
#     def __init__(self):
#         super().__init__()
#         loadUi('AppScreen.ui', self)
#         self.setCentralWidget(widget)
# #
# if __name__ == "__main__":


requete_Outils = ''
Requete_Outils = ['ELEC', 'BOIS', 'USINAGE']
page_choix_outils = ['page_choix_outils_elec', 'page_choix_outils_bois', 'page_choix_outils_usinage']
Data = []
Lelec = []
Lbois = []
Lusinage = []
Lfinal = []

app = QApplication(sys.argv)

widget = QtWidgets.QStackedWidget()

# mainwindow = MainScreen()

from FabLabEmprunt.pageAccueil import PageAccueil
from FabLabEmprunt.empruntTypeOutils import EmpruntTypeOutils

page_accueil = PageAccueil()
page_choix_type_outils = EmpruntTypeOutils()

widget.addWidget(page_accueil)
widget.addWidget(page_choix_type_outils)

# widget.setCurrentWidget(page_accueil  )

widget.setFixedHeight(700)
widget.setFixedWidth(1000)
widget.show()
# mainwindow.show()

print("Index Accueil : ", widget.indexOf(page_accueil))

try:
    sys.exit(app.exec_())
except:
    print("Exiting")
