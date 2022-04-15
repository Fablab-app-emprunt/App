from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QMessageBox
from PyQt5.uic import loadUi

class pageAccueil(QWidget):
    def __init__(self):
        super(pageAccueil,self).__init__()
        loadUi('pageAccueil.ui',self)
        self.rendreoutils.clicked.connect(self.rendreOutils)
        self.emprunteroutils.clicked.connect(self.emprunterOutils)

    def rendreOutils(self):
        print("rendre outils")
        type_outils = empruntTypeOutils()


    def emprunterOutils(self):
        print("emprunter outils")

class empruntTypeOutils(QWidget):
    def __init__(self):
        super(empruntTypeOutils,self).__init__()
        loadUi('empruntTypeOutils.ui',self)

app = QApplication([])
monIHM = pageAccueil()
monIHM.show()
app.exec_()