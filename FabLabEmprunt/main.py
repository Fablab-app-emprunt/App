import sys
from PyQt5 import QtGui
from PyQt5 import QtWidgets, QtSql
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QWidget, QMessageBox
from PyQt5.QtSql import QSql, QSqlQuery, QSqlDatabase
import mysql.connector

global requete_Outils
global widget

# class MainApp(QWidget):
#     def __init__(self):
#         super(MainApp, self).__init__()
#         self.Stack = QtWidgets.QStackedWidget()
#         widget = QtWidgets.QStackedWidget()
#
#         self.page_accueil = PageAccueil()
#         self.page_choix_type_outils = EmpruntTypeOutils()
#         self.page_choix_outils = EmpruntAjout()
#
#         self.widget.addWidget(self.page_accueil)
#         self.widget.addWidget(self.page_choix_type_outils)
#         self.widget.addWidget(self.page_choix_outils)
#
#         widget.setFixedHeight(700)
#         widget.setFixedWidth(1000)
#         widget.show()
# if __name__ == "__main__":

app = QApplication(sys.argv)
# IHM = MainApp()

from FabLabEmprunt.pageAccueil import PageAccueil
from FabLabEmprunt.empruntTypeOutils import EmpruntTypeOutils
from FabLabEmprunt.empruntajout import EmpruntAjout

widget = QtWidgets.QStackedWidget()

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