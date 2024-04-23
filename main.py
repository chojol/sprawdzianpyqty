import sys
from PyQt6.QtWidgets import QApplication, QDialog, QListView
from layout import Ui_Dialog


class MyForm(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()
        self.sumkalori = 0.00
        self.maxkalori = 0.00
        self.ui.buttDodaj.clicked.connect(self.dodawanieKalorii)



    def dodawanieKalorii(self):
        self.kalorie()
        kalorie = self.ui.linePosilek.text()
        kalorie = self.ui.kalorie_posilek.text()
        kalorie = float(kalorie.replace('',''))
        self.sumkalori += float(kalorie)
        print(self.maxkalori)

        self.ui.listView.addItem(f'{self.maxkalori}')
        self.ui.sumkalori.setText(f'{self.sumkalori}')




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyForm()
    window.setWindowTitle('Kalkulator kalorii')
    window.show()
    sys.exit(app.exec())