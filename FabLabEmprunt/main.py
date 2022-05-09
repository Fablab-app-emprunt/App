import sys
from PyQt5 import QtGui
from PyQt5 import QtWidgets, QtSql
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QWidget, QMessageBox
from PyQt5.QtSql import QSql, QSqlQuery, QSqlDatabase
import mysql.connector

global requete_Outils

from FabLabEmprunt.pageAccueil import PageAccueil
from FabLabEmprunt.empruntTypeOutils import EmpruntTypeOutils
from FabLabEmprunt.empruntajout import EmpruntAjout


if __name__ == "__main__":

    app = QApplication(sys.argv)
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