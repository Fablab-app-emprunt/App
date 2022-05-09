import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtWidgets import QDialog, QApplication, QLabel, QWidget, QMessageBox

# from FabLabEmprunt.empruntajout import EmpruntAjout
# from FabLabEmprunt.pageAccueil import PageAccueil

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

    def conn_BDD(self, requete_Outils):
        #---------BDD----------------

        #-----------Déclaration de la connexion---------
        connection = mysql.connector.connect(user='u556968436_LaTeamDeLoick', password='LoickRaison2022',
                                             host='145.14.151.101',
                                             database='u556968436_fablab')
        # sql_select_Query = "select * from Personnes"
        # cursor = connection.cursor()
        # cursor.execute(sql_select_Query)
        # # get all records
        # records = cursor.fetchall()
        # print("Total number of rows in table: ", cursor.rowcount)
        #
        # print("\nPrinting each row")
        # for row in records:
        #     print("Id = ", row[1], )
        #
        # connection.close()
        count_tools = "select count(*) from Outils where departOutils_Outils = '" + requete_Outils + "'"
        cursor = connection.cursor()
        cursor.execute(count_tools)
        outils = cursor.fetchall()
        for row in outils:
            print("Id = ", row[0], )
            self.tableWidget.setRowCount(row[0])

        connection.close()
        #----------Requêtes de modification------------

        # query = QSqlQuery("insert into Utilisateur (login) values ('david')")

        #                OU

        #         # query = QSqlQuery()
        #         # query.exec_("insert into Utilisateur (login) values ('david')")
        #
        #     #----------Requêtes préparées------------ (utile lorsqu'on utilise des variables)
        #
        #         # query = QSqlQuery()
        #         # query.prepare("insert into Utilisateur (login) values (:nom)")
        # query.bindValue(":nom", "david")
        # query.exec_()

        #-----------Gestion des erreurs---------------

        # db.open("login", "motdepasse")
        # if db.isOpenError():
        #     error = db.lastError()


    def bois(self):
        widget.setCurrentIndex(2)
        requete_Outils = 'BOIS'
        self.conn_BDD(requete_Outils)

    def elec(self):
        widget.setCurrentIndex(2)
        requete_Outils = 'ELEC'
        self.conn_BDD(requete_Outils)

    def usinage(self):
        widget.setCurrentIndex(2)
        requete_Outils = 'USINAGE'
        self.conn_BDD(requete_Outils)


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

