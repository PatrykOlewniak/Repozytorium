# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dodanie_nowego.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.Qt import QDialog

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

class Ui_Okno_Dodaj(QDialog):
    def setupUi(self, GlowneOkno):
        GlowneOkno.setObjectName(_fromUtf8("GlowneOkno"))
        GlowneOkno.setWindowModality(QtCore.Qt.WindowModal)
        GlowneOkno.resize(663, 382)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(GlowneOkno.sizePolicy().hasHeightForWidth())
        GlowneOkno.setSizePolicy(sizePolicy)
        GlowneOkno.setMaximumSize(QtCore.QSize(1024, 768))
        #GlowneOkno.setFocusPolicy(QtCore.Qt.NoFocus)
        self.gridLayoutWidget = QtGui.QWidget(GlowneOkno)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 60, 411, 276))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_3.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout_3.setContentsMargins(-1, -1, -1, 5)
        self.gridLayout_3.setHorizontalSpacing(1)
        self.gridLayout_3.setVerticalSpacing(5)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.comboBox_2 = QtGui.QComboBox(self.gridLayoutWidget)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.gridLayout_3.addWidget(self.comboBox_2, 2, 1, 1, 1)
        self.comboBox = QtGui.QComboBox(self.gridLayoutWidget)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.gridLayout_3.addWidget(self.comboBox, 1, 1, 1, 1)
        self.PodkategoriaLabel = QtGui.QLabel(self.gridLayoutWidget)
        self.PodkategoriaLabel.setObjectName(_fromUtf8("PodkategoriaLabel"))
        self.gridLayout_3.addWidget(self.PodkategoriaLabel, 2, 0, 1, 1)
        self.OpisTextEdit = QtGui.QPlainTextEdit(self.gridLayoutWidget)
        self.OpisTextEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        #self.OpisTextEdit.setTabChangesFocus(True)
        self.OpisTextEdit.setObjectName(_fromUtf8("OpisTextEdit"))
        self.gridLayout_3.addWidget(self.OpisTextEdit, 3, 1, 1, 1)
        self.OpisLabel = QtGui.QLabel(self.gridLayoutWidget)
        self.OpisLabel.setObjectName(_fromUtf8("OpisLabel"))
        self.gridLayout_3.addWidget(self.OpisLabel, 3, 0, 1, 1)
        self.NazwaLabel = QtGui.QLabel(self.gridLayoutWidget)
        self.NazwaLabel.setObjectName(_fromUtf8("NazwaLabel"))
        self.gridLayout_3.addWidget(self.NazwaLabel, 0, 0, 1, 1)
        self.Data_wydaniaLabel = QtGui.QLabel(self.gridLayoutWidget)
        self.Data_wydaniaLabel.setObjectName(_fromUtf8("Data_wydaniaLabel"))
        self.gridLayout_3.addWidget(self.Data_wydaniaLabel, 4, 0, 1, 1)
        self.KategoriaLabel = QtGui.QLabel(self.gridLayoutWidget)
        self.KategoriaLabel.setObjectName(_fromUtf8("KategoriaLabel"))
        self.gridLayout_3.addWidget(self.KategoriaLabel, 1, 0, 1, 1)
        self.NazwaLineEdit = QtGui.QLineEdit(self.gridLayoutWidget)
        self.NazwaLineEdit.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.NazwaLineEdit.setObjectName(_fromUtf8("NazwaLineEdit"))
        self.gridLayout_3.addWidget(self.NazwaLineEdit, 0, 1, 1, 1)
        self.ZrodloLineEdit_2 = QtGui.QLineEdit(self.gridLayoutWidget)
        self.ZrodloLineEdit_2.setInputMask(_fromUtf8(""))
        self.ZrodloLineEdit_2.setText(_fromUtf8(""))
        self.ZrodloLineEdit_2.setEchoMode(QtGui.QLineEdit.Normal)
        self.ZrodloLineEdit_2.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.ZrodloLineEdit_2.setPlaceholderText(_fromUtf8(""))
        self.ZrodloLineEdit_2.setObjectName(_fromUtf8("ZrodloLineEdit_2"))
        self.gridLayout_3.addWidget(self.ZrodloLineEdit_2, 5, 1, 1, 1)
        self.ZrodloLabel = QtGui.QLabel(self.gridLayoutWidget)
        self.ZrodloLabel.setObjectName(_fromUtf8("ZrodloLabel"))
        self.gridLayout_3.addWidget(self.ZrodloLabel, 5, 0, 1, 1)
        self.ZrodloLabel_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.ZrodloLabel_2.setObjectName(_fromUtf8("ZrodloLabel_2"))
        self.gridLayout_3.addWidget(self.ZrodloLabel_2, 6, 0, 1, 1)
        self.AutorLineEdit_3 = QtGui.QLineEdit(self.gridLayoutWidget)
        self.AutorLineEdit_3.setInputMask(_fromUtf8(""))
        self.AutorLineEdit_3.setText(_fromUtf8(""))
        self.AutorLineEdit_3.setEchoMode(QtGui.QLineEdit.Normal)
        self.AutorLineEdit_3.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.AutorLineEdit_3.setPlaceholderText(_fromUtf8(""))
        self.AutorLineEdit_3.setObjectName(_fromUtf8("AutorLineEdit_3"))
        self.gridLayout_3.addWidget(self.AutorLineEdit_3, 6, 1, 1, 1)
        self.Data_wydaniaLineEdit = QtGui.QLineEdit(self.gridLayoutWidget)
        self.Data_wydaniaLineEdit.setInputMask(_fromUtf8(""))
        self.Data_wydaniaLineEdit.setText(_fromUtf8(""))
        self.Data_wydaniaLineEdit.setEchoMode(QtGui.QLineEdit.Normal)
        self.Data_wydaniaLineEdit.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.Data_wydaniaLineEdit.setObjectName(_fromUtf8("Data_wydaniaLineEdit"))
        self.gridLayout_3.addWidget(self.Data_wydaniaLineEdit, 4, 1, 1, 1)
        self.naglowekLabel = QtGui.QLabel(GlowneOkno)
        self.naglowekLabel.setGeometry(QtCore.QRect(160, 0, 320, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.naglowekLabel.setFont(font)
        self.naglowekLabel.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.naglowekLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.naglowekLabel.setTextFormat(QtCore.Qt.AutoText)
        self.naglowekLabel.setObjectName(_fromUtf8("naglowekLabel"))
        self.line = QtGui.QFrame(GlowneOkno)
        self.line.setWindowModality(QtCore.Qt.WindowModal)
        self.line.setGeometry(QtCore.QRect(20, 30, 621, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayoutWidget_2 = QtGui.QWidget(GlowneOkno)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(460, 60, 158, 271))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.ZalaczButton = QtGui.QPushButton(self.verticalLayoutWidget_2)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/rozne/filenew.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        #self.ZalaczButton.setIcon(icon)
        self.ZalaczButton.setObjectName(_fromUtf8("ZalaczButton"))
        self.verticalLayout_2.addWidget(self.ZalaczButton)
        self.line_3 = QtGui.QFrame(self.verticalLayoutWidget_2)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.verticalLayout_2.addWidget(self.line_3)
        self.UtworzPButton = QtGui.QPushButton(self.verticalLayoutWidget_2)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/rozne/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        #self.UtworzPButton.setIcon(icon1)
        self.UtworzPButton.setObjectName(_fromUtf8("UtworzPButton"))
        self.verticalLayout_2.addWidget(self.UtworzPButton)
        self.line_6 = QtGui.QFrame(self.verticalLayoutWidget_2)
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.verticalLayout_2.addWidget(self.line_6)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.DodajButton = QtGui.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.DodajButton.setFont(font)
        self.DodajButton.setObjectName(_fromUtf8("DodajButton"))
        self.verticalLayout_2.addWidget(self.DodajButton)
        icon1= QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/rozne/add.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon1=QtGui.QIcon()
        self.DodajButton.setIcon(icon1)
        self.retranslateUi(GlowneOkno)
        QtCore.QMetaObject.connectSlotsByName(GlowneOkno)

    def retranslateUi(self, GlowneOkno):
        GlowneOkno.setWindowTitle(_translate("GlowneOkno", "Repozytorium plików PDF", None))
        self.PodkategoriaLabel.setText(_translate("GlowneOkno", "Poddziedzina:", None))
        self.OpisLabel.setText(_translate("GlowneOkno", "Opis:", None))
        self.NazwaLabel.setText(_translate("GlowneOkno", "Nazwa:", None))
        self.Data_wydaniaLabel.setText(_translate("GlowneOkno", "Rok wydania:", None))
        self.KategoriaLabel.setText(_translate("GlowneOkno", "Dziedzina:", None))
        self.ZrodloLabel.setText(_translate("GlowneOkno", "Źródło:", None))
        self.ZrodloLabel_2.setText(_translate("GlowneOkno", "Autor:", None))
        self.Data_wydaniaLineEdit.setPlaceholderText(_translate("GlowneOkno", "YYYY", None))
        self.naglowekLabel.setText(_translate("GlowneOkno", "Dodanie nowego pliku", None))
        self.ZalaczButton.setText(_translate("GlowneOkno", "Załącz plik pdf", None))
        self.UtworzPButton.setText(_translate("GlowneOkno", "Utwórz nowy plik PDF", None))
        self.DodajButton.setText(_translate("GlowneOkno", "Dodaj nowy wpis", None))

import zasoby
