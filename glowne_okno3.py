# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'glowne1.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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






class Ui_GlowneOkno(object):
    def setupglowneUi(self, GlowneOkno):
        GlowneOkno.setObjectName(_fromUtf8("Repozytorium"))
        GlowneOkno.resize(1353, 843)
        self.label = QtGui.QLabel(GlowneOkno)
        self.label.setGeometry(QtCore.QRect(30, 70, 61, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.treeView = QtGui.QTreeView(GlowneOkno)
        self.treeView.setGeometry(QtCore.QRect(30, 90, 155, 651))
        self.treeView.setObjectName(_fromUtf8("treeView"))
        self.tableView = QtGui.QTableView(GlowneOkno)
        self.tableView.setGeometry(QtCore.QRect(190, 90, 1131, 651))
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.label_2 = QtGui.QLabel(GlowneOkno)
        self.label_2.setGeometry(QtCore.QRect(190, 70, 61, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.line = QtGui.QFrame(GlowneOkno)
        self.line.setGeometry(QtCore.QRect(30, 60, 1291, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayoutWidget = QtGui.QWidget(GlowneOkno)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 10, 1301, 51))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_6 = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.horizontalLayout.addWidget(self.pushButton_6)
        self.pushButton_2 = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_7 = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.horizontalLayout.addWidget(self.pushButton_7)
        self.pushButton_4 = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_3 = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.label_3 = QtGui.QLabel(GlowneOkno)
        self.label_3.setGeometry(QtCore.QRect(320, 780, 91, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayoutWidget_2 = QtGui.QWidget(GlowneOkno)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(430, 760, 891, 51))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lineEdit = QtGui.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_8 = QtGui.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit.setText(_fromUtf8(""))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.horizontalLayout_2.addWidget(self.lineEdit_8)
        self.lineEdit_4 = QtGui.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_4.setAccessibleDescription(_fromUtf8(""))
        self.lineEdit_4.setText(_fromUtf8(""))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.horizontalLayout_2.addWidget(self.lineEdit_4)
        self.lineEdit_3 = QtGui.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_3.setAccessibleDescription(_fromUtf8(""))
        self.lineEdit_3.setText(_fromUtf8(""))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.horizontalLayout_2.addWidget(self.lineEdit_3)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.line_2 = QtGui.QFrame(self.horizontalLayoutWidget_2)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.horizontalLayout_2.addWidget(self.line_2)
        self.pushButton_5 = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.line_3 = QtGui.QFrame(GlowneOkno)
        self.line_3.setGeometry(QtCore.QRect(170, 740, 1151, 20))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.pushButton_8 = QtGui.QPushButton(GlowneOkno)
        self.pushButton_8.setGeometry(QtCore.QRect(50, 750, 93, 28))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))

        self.retranslateUi(GlowneOkno)
        QtCore.QMetaObject.connectSlotsByName(GlowneOkno)
        
        #icony
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/rozne/add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1=QtGui.QIcon()
        icon2=QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/rozne/delete.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/rozne/filesave.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/rozne/kwin.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/rozne/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/rozne/filenew.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon3)
        self.pushButton_3.setIcon(icon5)
        self.pushButton_4.setIcon(icon4)
        self.pushButton.setIcon(icon2)
        self.pushButton_7.setIcon(icon1)
        self.pushButton_2.setIcon(icon)
    def retranslateUi(self, GlowneOkno):
        GlowneOkno.setWindowTitle(_translate("GlowneOkno", "Repozytorium", None))
        self.label.setText(_translate("GlowneOkno", "Dziedziny:", None))
        self.label_2.setText(_translate("GlowneOkno", "Pliki:", None))
        self.pushButton_6.setText(_translate("GlowneOkno", "Otwórz plik PDF", None))
        self.pushButton_2.setText(_translate("GlowneOkno", "Dodaj nowy", None))
        self.pushButton.setText(_translate("GlowneOkno", "Włącz edytowanie", None))
        self.pushButton_7.setText(_translate("GlowneOkno", "Usuń", None))
        self.pushButton_4.setText(_translate("GlowneOkno", "Zmień dziedziny", None))
        self.pushButton_3.setText(_translate("GlowneOkno", "Edytor PDF", None))
        self.label_3.setText(_translate("GlowneOkno", "Wyszukiwanie:", None))
        self.lineEdit.setPlaceholderText(_translate("GlowneOkno", "Nazwa pliku", None))
        self.lineEdit_4.setPlaceholderText(_translate("GlowneOkno", "Źródło", None))
        self.lineEdit_8.setPlaceholderText(_translate("GlowneOkno", "Autor", None))
        self.lineEdit_3.setPlaceholderText(_translate("GlowneOkno", "Rok wydania", None))
        self.pushButton_5.setText(_translate("GlowneOkno", "Wyczyść wyszukiwanie", None))
        self.pushButton_8.setText(_translate("GlowneOkno", "Rozwiń/Zwiń", None))

import zasoby
