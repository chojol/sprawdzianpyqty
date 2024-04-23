# Form implementation generated from reading ui file 'layout.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1076, 871)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setKerning(False)
        Dialog.setFont(font)
        self.gridLayoutWidget = QtWidgets.QWidget(parent=Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(160, 40, 792, 661))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.radioKob = QtWidgets.QRadioButton(parent=self.gridLayoutWidget)
        self.radioKob.setObjectName("radioKob")
        self.horizontalLayout_3.addWidget(self.radioKob)
        self.radioMez = QtWidgets.QRadioButton(parent=self.gridLayoutWidget)
        self.radioMez.setObjectName("radioMez")
        self.horizontalLayout_3.addWidget(self.radioMez)
        self.gridLayout.addLayout(self.horizontalLayout_3, 7, 0, 1, 2)
        self.kalorie_posilek = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setItalic(True)
        font.setKerning(True)
        self.kalorie_posilek.setFont(font)
        self.kalorie_posilek.setStyleSheet("background-color: rgb(56, 140, 11);")
        self.kalorie_posilek.setObjectName("kalorie_posilek")
        self.gridLayout.addWidget(self.kalorie_posilek, 1, 0, 1, 1)
        self.buttDodaj = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.buttDodaj.setFont(font)
        self.buttDodaj.setStyleSheet("background-color: rgb(110, 255, 48);")
        self.buttDodaj.setObjectName("buttDodaj")
        self.gridLayout.addWidget(self.buttDodaj, 2, 0, 1, 2)
        self.listView = QtWidgets.QListView(parent=self.gridLayoutWidget)
        self.listView.setObjectName("listView")
        self.gridLayout.addWidget(self.listView, 3, 0, 1, 2)
        self.costam = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.costam.setFont(font)
        self.costam.setStyleSheet("background-color: rgb(144, 255, 110);\n"
"color: rgb(255, 255, 255);")
        self.costam.setObjectName("costam")
        self.gridLayout.addWidget(self.costam, 4, 0, 1, 1)
        self.linePosilek = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.linePosilek.setObjectName("linePosilek")
        self.gridLayout.addWidget(self.linePosilek, 0, 1, 1, 1)
        self.podany_pos = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.podany_pos.setFont(font)
        self.podany_pos.setStyleSheet("background-color: rgb(56, 140, 11);")
        self.podany_pos.setObjectName("podany_pos")
        self.gridLayout.addWidget(self.podany_pos, 0, 0, 1, 1)
        self.image = QtWidgets.QGraphicsView(parent=self.gridLayoutWidget)
        self.image.setObjectName("image")
        self.gridLayout.addWidget(self.image, 5, 0, 1, 2)
        self.line = QtWidgets.QFrame(parent=self.gridLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 6, 0, 1, 2)
        self.spinkaloryka = QtWidgets.QDoubleSpinBox(parent=self.gridLayoutWidget)
        self.spinkaloryka.setObjectName("spinkaloryka")
        self.gridLayout.addWidget(self.spinkaloryka, 1, 1, 1, 1)
        self.liczbaKalor = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.liczbaKalor.setText("")
        self.liczbaKalor.setObjectName("liczbaKalor")
        self.gridLayout.addWidget(self.liczbaKalor, 4, 1, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(170, 720, 790, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lowActivity = QtWidgets.QRadioButton(parent=self.horizontalLayoutWidget)
        self.lowActivity.setObjectName("lowActivity")
        self.horizontalLayout_2.addWidget(self.lowActivity)
        self.medActivity = QtWidgets.QRadioButton(parent=self.horizontalLayoutWidget)
        self.medActivity.setObjectName("medActivity")
        self.horizontalLayout_2.addWidget(self.medActivity)
        self.highActivity = QtWidgets.QRadioButton(parent=self.horizontalLayoutWidget)
        self.highActivity.setObjectName("highActivity")
        self.horizontalLayout_2.addWidget(self.highActivity)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.radioKob.setText(_translate("Dialog", "Kobieta"))
        self.radioMez.setText(_translate("Dialog", "Mężczyzna"))
        self.kalorie_posilek.setText(_translate("Dialog", "Kalorie w posilku"))
        self.buttDodaj.setText(_translate("Dialog", "Dodaj"))
        self.costam.setText(_translate("Dialog", "Liczba sporzytych kalorii"))
        self.podany_pos.setText(_translate("Dialog", "Podaj swoj posilek"))
        self.lowActivity.setText(_translate("Dialog", "mała aktywnosc fizyczna"))
        self.medActivity.setText(_translate("Dialog", "średnia aktywnosc fizyczna"))
        self.highActivity.setText(_translate("Dialog", "duża aktywnosc fizyczna"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
