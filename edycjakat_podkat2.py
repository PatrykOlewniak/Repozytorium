# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edycjakat_podkat2.ui'
#
# Created: Sat Sep 19 16:54:53 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Okno edycji poddziedziny i dziedziny"))
        Dialog.resize(640, 480)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(-10, 430, 621, 32))
        self.buttonBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label_kat = QtGui.QLabel(Dialog)
        self.label_kat.setGeometry(QtCore.QRect(20, 10, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_kat.setFont(font)
        self.label_kat.setObjectName(_fromUtf8("label_kat"))
        self.label_podkat = QtGui.QLabel(Dialog)
        self.label_podkat.setGeometry(QtCore.QRect(350, 6, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_podkat.setFont(font)
        self.label_podkat.setObjectName(_fromUtf8("label_podkat"))
        self.verticalLayoutWidget = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(130, 90, 164, 241))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.lineEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout.addWidget(self.lineEdit)
        self.pushButton_2 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout.addWidget(self.pushButton_2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        self.verticalLayoutWidget_2 = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(460, 90, 160, 241))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_4 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_2.addWidget(self.label_4)
        self.lineEdit_2 = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.pushButton_4 = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.verticalLayout_2.addWidget(self.pushButton_4)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.pushButton_6 = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.verticalLayout_2.addWidget(self.pushButton_6)
        self.tableViewkat = QtGui.QTableView(Dialog)
        self.tableViewkat.setGeometry(QtCore.QRect(20, 90, 105, 241))
        self.tableViewkat.setObjectName(_fromUtf8("tableViewkat"))
        self.tableViewpodkat = QtGui.QTableView(Dialog)
        self.tableViewpodkat.setGeometry(QtCore.QRect(350, 90, 101, 241))
        self.tableViewpodkat.setObjectName(_fromUtf8("tableViewpodkat"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(350, 60, 171, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.comboBoxwybkat = QtGui.QComboBox(Dialog)
        self.comboBoxwybkat.setGeometry(QtCore.QRect(510, 60, 91, 22))
        self.comboBoxwybkat.setObjectName(_fromUtf8("comboBoxwybkat"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 360, 601, 41))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Okno edycji poddziedziny i dziedziny", None))
        self.label_kat.setText(_translate("Dialog", "Edycja Dziedziny", None))
        self.label_podkat.setText(_translate("Dialog", "Edycja Poddziedziny", None))
        self.label_2.setText(_translate("Dialog", "Wprowadz nazwę nowej \n"
" dziedziny:", None))
        self.pushButton_2.setText(_translate("Dialog", "Dodaj nową kategorie", None))
        self.pushButton.setText(_translate("Dialog", "Usuń kategorię", None))
        self.label_4.setText(_translate("Dialog", "Wprowadz nazwę nowej \n"
" poddziedziny:", None))
        self.pushButton_4.setText(_translate("Dialog", "Dodaj nową", None))
        self.pushButton_6.setText(_translate("Dialog", "Usuń poddziedzinę", None))
        self.label_3.setText(_translate("Dialog", "Podaj dziedzinę nadrzędną:", None))
        self.label.setText(_translate("Dialog", "Aby zmienić nazwę dziedziny lub poddziedziny wybierz odpowiedni element na liście dwukrotnie klikając\n"
"dwukrotne kliknięcie umożliwi edycję. Aby zatwierdzić zmianę kliknij ENTER", None))
