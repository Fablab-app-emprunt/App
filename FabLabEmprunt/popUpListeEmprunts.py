
from PyQt5.QtWidgets import  QWidget
from PyQt5.QtSql import QSqlDatabase

class PopUpListeEmpruntsWidget(QWidget, QSqlDatabase):
    def __init__(self):
        from PyQt5 import QtWidgets
        from PyQt5.uic import loadUi
        from main import Lfinal
        from PyQt5.QtWidgets import QTableWidgetItem
        super(PopUpListeEmpruntsWidget, self).__init__()
        loadUi('popUpListeEmprunts.ui', self)
        self.boutoncroix.clicked.connect(self.reponseCroix)
        self.boutonconfirmer.clicked.connect(self.reponseConfirmer)
        self.table_Recap.setColumnCount(2)
        self.table_Recap.rowCount()
        self.table_Recap.setHorizontalHeaderLabels(["Nom de l'outils",'Quantité'])
        row = self.table_Recap.rowCount()
        self.table_Recap.setRowCount(len(Lfinal))
        col = 0
        header = self.table_Recap.horizontalHeader()
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

        #------------------------------------REMPLIR LES TABLEAUX------------------------------------------------------------
        for item in range(0,len(Lfinal),2):
            print("row",row)
            print("item", item)
            cell = QTableWidgetItem(str(Lfinal[item]))
            self.table_Recap.setItem(row, col, cell)
            cell = QTableWidgetItem(str(Lfinal[item+1]))
            self.table_Recap.setItem(row, col+1, cell)
            row+=1


    def reponseConfirmer(self):
        from main import Lfinal
        import mysql.connector
        from main import widget
        connection = mysql.connector.connect(user='u556968436_LaTeamDeLoick', password='LoickRaison2022',
                                             host='145.14.151.101',
                                             database='u556968436_fablab')
        print("rep confirmer",len(Lfinal))
        for i in range(1,len(Lfinal),2):
            req = "UPDATE Outils SET quantiteEmprunte_Outils = "+Lfinal[i]+" WHERE nomOutils_outils ="+ Lfinal[i-1]
            cursor = connection.cursor()
            cursor.execute(req)
        connection.close()
        widget.setCurrentIndex(0)

    def reponseCroix(self):
        from main import widget
        widget.setCurrentIndex(1)