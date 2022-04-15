from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.uic import loadUi

class pageAccueil(QWidget):
    def __init__(self):
        super(pageAccueil,self).__init__()
        loadUi('pageAccueil.ui',self)
        self.rendreOutils.clicked.connect(self.rendreOutils)
    def rendreOutils(self):
        return "rendre outils"


#     def emprunterOutils(self):
#         return "emprunter outils"
#
#
# class empruntTypeOutils(QWidget):
#     def __init__(self):
#         super(empruntTypeOutils,self).__init__()
#         loadUi('pageAccueil.ui',self)

app = QApplication([])
monIHM = pageAccueil()
monIHM.show()
app.exec_()