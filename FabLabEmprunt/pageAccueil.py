import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QLabel, QWidget, QMessageBox

# from FabLabEmprunt.empruntTypeOutils import EmpruntTypeOutils

class PageAccueil(QDialog):
    def __init__(self):
        from PyQt5.uic import loadUi
        super(PageAccueil,self).__init__()
        loadUi('pageAccueil.ui',self)
        self.rendreoutils.clicked.connect(self.goToRendreOutils)
        self.emprunteroutils.clicked.connect(self.goToEmprunterOutils)

    def goToRendreOutils(self):
        widget.setCurrentIndex(1)

    def goToEmprunterOutils(self):
        # rendreoutils = EmpruntTypeOutils()
        # widget.addWidget(rendreoutils)
        # widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setCurrentIndex(1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    page_accueil = PageAccueil()
    widget.addWidget(page_accueil)
    widget.setFixedHeight(700)
    widget.setFixedWidth(1000)
    widget.show()

    try:
        sys.exit(app.exec_())
    except :
        print("Exiting")