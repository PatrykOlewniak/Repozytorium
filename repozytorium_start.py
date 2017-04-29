# -*- coding: utf-8 -*-
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger
import PyPDF2
import subprocess
import os
import sys
import PyQt4
from glowne_okno3 import Ui_GlowneOkno
from dodanie_nowego import Ui_Okno_Dodaj
from edycjakat_podkat2 import Ui_Dialog

from PyQt4.QtCore import (Qt, QString, QFileInfo, QRect, QRegExp, QVariant)
from PyQt4.QtCore import pyqtSignal as Signal
from PyQt4.QtGui import (QAbstractItemView, QStandardItem, QApplication, QMenu, QComboBox, QDataWidgetMapper, QDialog,
                         QGridLayout,
                         QHBoxLayout, QLabel, QLineEdit, QFileDialog, QPlainTextEdit, QMessageBox, QTableView,
                         QFormLayout, QPushButton, QVBoxLayout, QTableWidget, QWidget, QSpinBox, QCheckBox,
                         QDialogButtonBox, QFont, QSortFilterProxyModel, QStandardItemModel, QFileSystemModel)
from PyQt4.QtSql import (QSqlDatabase, QSqlRelation,
                         QSqlRelationalDelegate, QSqlRelationalTableModel, QSqlTableModel, QSqlQuery)
from PyQt4.Qt import QModelIndex, QTreeView, QTableView
import sqlite3 as lite

"""
    
"""
id_pliki = 0
nazwa_pliku = 1
opis = 2
data_wydania = 3
lokalizacja = 4
kategorie = 5
podkategoria = 6
autor = 7
zrodlo = 8
id_kat = 0
id_parent = 1
nazwa_kat = 2

index_ck = 0
nawa_ck = ""

reload(sys)  # rozwiązuje problemy kodowania polskich znaków
sys.setdefaultencoding('utf8')


class Repozytorium(QDialog):
    def __init__ (self, parent=None):
        super(Repozytorium, self).__init__(parent)
        self.ui_glowne = Ui_GlowneOkno()
        self.ui_glowne.setupglowneUi(self)
        self.Ui_Okno_Dodaj = Ui_Okno_Dodaj()
        self.setWindowFlags(self.windowFlags() ^ Qt.WindowContextHelpButtonHint)  # usuniecie "?"
        self.model_glowny()
        self.model_menu()
        self.polaczenia()
        self.model_szukaj()
        self.wyswtablicy()

    def polaczenia (self):
        self.ui_glowne.pushButton_2.clicked.connect(self.otworz_okno_dodawania)
        self.ui_glowne.lineEdit.textChanged.connect(self.wyszukaj_nazwa)
        self.ui_glowne.lineEdit_4.textChanged.connect(self.wyszukaj_zrodlo)
        self.ui_glowne.lineEdit_3.textChanged.connect(self.wyszukaj_rok_wydania)
        self.ui_glowne.lineEdit_8.textChanged.connect(self.wyszukaj_autor)
        self.ui_glowne.pushButton_5.clicked.connect(self.wyczyscwyszukiwanie)
        self.ui_glowne.tableView.clicked.connect(self.wskazniktabl)
        self.ui_glowne.pushButton_8.clicked.connect(self.zwijanie_listy_menu)
        self.ui_glowne.pushButton_4.clicked.connect(self.otworzdialogkatipodkat)
        self.ui_glowne.pushButton_7.clicked.connect(self.usunrecord)
        self.ui_glowne.pushButton.clicked.connect(self.wlacz_edytowanie)
        self.ui_glowne.pushButton_6.clicked.connect(self.otworz_plik)
        self.ui_glowne.pushButton_3.clicked.connect(self.otworz_edycje_PDF)

    def wskazniktabl (self, clickedIndex):
        index = self.proxyModel.index(clickedIndex.row(),
                                      0)  # wskazuje wartowsc [row=clickedIndex-tam gdzie click][columna=0]
        nazwa_index = self.proxyModel.index(clickedIndex.row(), 1)
        global nazwa_ck
        global index_ck
        index_ck = str(self.proxyModel.data(index).toString())
        nazwa_ck = str(self.proxyModel.data(nazwa_index).toString()).decode("utf-8")

    def otworz_plik (self):
        global nazwa_ck
        query = QSqlQuery()
        query.exec_("SELECT id_pliki FROM pliki where nazwa_pliku='" + nazwa_ck + "'")
        while (query.next()):
            plik = query.value(0).toString()

        con = lite.connect('repozytorium.db')

        with open("Plik_repozytorium.pdf", "wb") as output_file:
            cur = con.cursor()
            cur.execute("SELECT lokalizacja FROM pliki WHERE id_pliki ='" + str(plik) + "'")
            ablob = cur.fetchone()
            output_file.write(ablob[0])

            # obsluga na MAC I LINUX I WIN
            if sys.platform.startswith('darwin'):
                os.system("open" + "Plik_repozytorium.pdf")
            elif sys.platform.startswith('linux'):
                fileDir = os.path.dirname(os.path.realpath('__file__'))
                filename = os.path.join(fileDir, 'Plik_repozytorium.pdf')
                subprocess.call(["xdg-open", filename])
            elif sys.platform.startswith('win32'):
                os.startfile("Plik_repozytorium.pdf")

    def wyczyscwyszukiwanie (self):
        self.ui_glowne.lineEdit.clear()
        self.ui_glowne.lineEdit_3.clear()
        self.ui_glowne.lineEdit_4.clear()
        self.ui_glowne.lineEdit_8.clear()

    def model_glowny (self):
        self.model = QSqlRelationalTableModel(self)
        self.model.setTable("pliki")
        self.model.setRelation(5,
                               QSqlRelation("kategorie", "id_kat", "nazwa_kat"))
        self.model.setRelation(6,
                               QSqlRelation("kategorie", "id_kat", "nazwa_kat"))

        self.model.setSort(0, Qt.AscendingOrder)
        self.model.select()
        self.ui_glowne.tableView.setModel(self.model)
        self.mapper = QDataWidgetMapper(self)
        self.mapper.setSubmitPolicy(QDataWidgetMapper.ManualSubmit)
        self.mapper.setModel(self.model)
        self.mapper.setItemDelegate(QSqlRelationalDelegate(self))
        self.licznikclk = 0  # licznik klikniec zwiniecia

    def pobraniewartztree (self):
        index = self.ui_glowne.treeView.currentIndex()
        # print index.data().toString()
        wybrana_kat = index.data().toString()
        self.wyszukaj_kat(wybrana_kat)

    def model_menu (self):  # model lewego menu
        self.modelK = QStandardItemModel()

        self.ui_glowne.treeView.clicked.connect(self.pobraniewartztree)  # wyswietla klikniete menuopt
        self.ui_glowne.treeView.setModel(self.modelK)
        self.ui_glowne.treeView.setHeaderHidden(True)  # ukrycie nazwy naglowka

        listaKAT = []  # lista z nazwami roddzicow
        listanrKAT = []  # lista z numerami_kat rodzicow (w tej samej kolejnosci co listaKAT
        licznikclk = 0  # licznik klikniec zwiniecia
        query = QSqlQuery()

        ###pobierz liste rodzicow
        query.exec_("SELECT nazwa_kat from kategorie where id_parent =0")  # znajduje wszystkie kat ( parent=0)

        listaKAT = []  # lista z nazwami roddzicow

        while (query.next()):  # dodanie rodzicow do listy jako string
            listaKAT.append(str(query.value(0).toString()))

        # dodanie rodzicow jako QStandardItems
        for w in range(len(listaKAT)):
            rodzic = listaKAT[w]
            rodzic = QStandardItem(listaKAT[w])
            rodzic.setEditable(False)  # uniemozliwienie edycji pola
            self.modelK.appendRow(rodzic)

            # sprawdzenie jakie id_kat maja rodzice pokolei i dodanie w odpowiedniej kolejnosci do listy
            query.exec_("SELECT id_kat from kategorie where id_parent =0")
            listanrKAT = []
            while (query.next()):
                listanrKAT.append(str(query.value(0).toString()))

            podkatid1 = listanrKAT[w]
            query.exec_("SELECT nazwa_kat from kategorie WHERE id_parent = '" + podkatid1 + "'")
            # lista dzieci kat nr1 - znajdzuje podkat rodzica

            listapobranychpodkat = []  # lista robocza dla pobranych podkat
            while (query.next()):
                listapobranychpodkat.append(query.value(0).toString())

            for k in range(len(listapobranychpodkat)):
                dziecko = listapobranychpodkat[k]
                dziecko = QStandardItem(listapobranychpodkat[k])
                dziecko.setEditable(False)  # uniemozliwienie edycji pola
                rodzic.appendRow(dziecko)

    def zwijanie_listy_menu (self):

        if (self.licznikclk / 2 == 0):
            self.ui_glowne.treeView.expandAll()
            self.licznikclk += 1

        else:
            self.ui_glowne.treeView.collapseAll()
            self.licznikclk -= 1

    def model_szukaj (self):
        self.proxyModel = QSortFilterProxyModel(self)
        self.proxyModel.setSourceModel(self.model)
        self.proxyModel.setDynamicSortFilter(True)
        self.proxyModel.setFilterCaseSensitivity(Qt.CaseInsensitive)

    def wyszukaj_kat (self, text):
        # utworzenie pierw listy dziedzin by zmienic filter wyszukiwania dla dziedzin i podzdziedzin
        query = QSqlQuery()
        query.exec_("SELECT nazwa_kat from kategorie where id_parent =0")  # znajduje wszystkie kat ( parent=0)

        listaKATrobocza = []  # lista z nazwami roddzicow dla wyszukania

        while (query.next()):  # dodanie rodzicow do listy jako string
            listaKATrobocza.append(str(query.value(0).toString()))

        if (text in listaKATrobocza):
            self.proxyModel.setFilterKeyColumn(5)
        else:
            self.proxyModel.setFilterKeyColumn(6)

        self.ui_glowne.tableView.setModel(self.proxyModel)
        search = QRegExp(text, Qt.CaseInsensitive, QRegExp.RegExp)
        self.proxyModel.setFilterRegExp(search)
        self.ui_glowne.lineEdit_3.textChanged.connect(self.wyszukaj_rok_wydania)

    def wyszukaj_rok_wydania (self, text):
        self.ui_glowne.tableView.setModel(self.proxyModel)
        search = QRegExp(text, Qt.CaseInsensitive, QRegExp.RegExp)
        self.proxyModel.setFilterRegExp(search)
        self.proxyModel.setFilterKeyColumn(3)

    def wyszukaj_autor (self, text):
        self.ui_glowne.tableView.setModel(self.proxyModel)
        search = QRegExp(text, Qt.CaseInsensitive, QRegExp.RegExp)
        self.proxyModel.setFilterRegExp(search)
        self.proxyModel.setFilterKeyColumn(7)

    def wyszukaj_zrodlo (self, text):
        self.ui_glowne.tableView.setModel(self.proxyModel)
        search = QRegExp(text, Qt.CaseInsensitive, QRegExp.RegExp)
        self.proxyModel.setFilterRegExp(search)
        self.proxyModel.setFilterKeyColumn(8)

    def wyszukaj_nazwa (self, text):
        self.ui_glowne.tableView.setModel(self.proxyModel)
        search = QRegExp(text, Qt.CaseInsensitive, QRegExp.RegExp)
        self.proxyModel.setFilterRegExp(search)
        self.proxyModel.setFilterKeyColumn(1)

    def wlacz_edytowanie (self):
        self.ui_glowne.tableView.setEditTriggers(QAbstractItemView.DoubleClicked)

    def wyswtablicy (self):
        self.ui_glowne.tableView.setSelectionMode(QTableView.SingleSelection)
        self.ui_glowne.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui_glowne.tableView.setSelectionBehavior(QTableView.SelectRows)  # cale rows
        self.ui_glowne.tableView.setColumnHidden(id_pliki, True)
        self.ui_glowne.tableView.setColumnHidden(lokalizacja, True)
        self.model.setHeaderData(nazwa_pliku, Qt.Horizontal, QVariant("Nazwa"))
        self.model.setHeaderData(opis, Qt.Horizontal, QVariant("Opis"))
        self.model.setHeaderData(data_wydania, Qt.Horizontal, QVariant("Rok"))
        self.model.setHeaderData(5, Qt.Horizontal, QVariant("Dziedzina"))
        self.model.setHeaderData(6, Qt.Horizontal, QVariant("Poddziedzina"))
        self.model.setHeaderData(7, Qt.Horizontal, QVariant("Autor"))
        self.model.setHeaderData(8, Qt.Horizontal, QVariant(u"Źródło"))
        self.ui_glowne.tableView.setColumnWidth(1, 160)
        self.ui_glowne.tableView.setColumnWidth(2, 470)
        self.ui_glowne.tableView.setColumnWidth(3, 50)
        self.ui_glowne.tableView.setColumnWidth(5, 110)
        self.ui_glowne.tableView.setColumnWidth(6, 110)

    def usunrecord (self):
        query = QSqlQuery()
        query.exec_("SELECT nazwa_pliku FROM pliki WHERE id_pliki ='" + index_ck + "'")
        query.first()
        k = query.value(0).toString()
        # print k
        if (QMessageBox.question(self,
                                 ("Usunac"),
                                 ("Usunac wpis o nazwie: %s ?" % k),
                                 QMessageBox.Yes | QMessageBox.No) ==
                QMessageBox.No):
            return

        query = QSqlQuery()
        query.exec_("DELETE FROM pliki WHERE id_pliki ='" + index_ck + "'")
        self.mapper.submit()
        self.model.select()
        if not query.exec_(): QMessageBox.information(self, u"Błędne Dane", u"Wystąpił błąd, podaj poprawne dane")

    def otworz_okno_dodawania (self):  # otworz.
        dialog = okno_dodawania()
        dialog.exec_()
        if (dialog.close()):  # gdy zamknie s
            self.model.select()
            self.mapper.submit()

    def otworzdialogkatipodkat (self):  # otworz.
        dialog = okno_edycjiPiKat()
        dialog.exec_()
        if (dialog.close()):
            # gdy zamknie sie okno edycji
            self.model_menu()  # by odswiezyc menu
            self.model.select()
            self.mapper.submit()

    def otworz_edycje_PDF (self):  # otworz.
        dialog = edycjaPDF()
        dialog.exec_()


class okno_edycjiPiKat(QDialog):
    wybrana_kat = 0
    wybrana_podkat = 0

    def __init__ (self):
        QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.wyswedycjiKatkatmodel()
        self.wyswedycjiPodkatkatmodel()
        self.polaczenia_kat_podkat()
        self.setWindowFlags(self.windowFlags() ^ Qt.WindowContextHelpButtonHint)  # usuniecie "?"

    # edycja kategorii
    def wyswedycjiKatkatmodel (self):  # nadpisanie z ui + dodanie

        self.model2 = QSqlTableModel()
        self.model2.setTable("kategorie")
        self.model2.setFilter("id_parent=0")
        self.model2.setHeaderData(nazwa_kat, Qt.Horizontal, ("Dziedzina       "));
        self.model2.select()

        # kategorie
        self.ui.tableViewkat.setModel(self.model2)
        self.ui.tableViewkat.setColumnHidden(id_kat, True)
        self.ui.tableViewkat.setColumnHidden(id_parent, True)
        self.ui.tableViewkat.resizeColumnsToContents()
        # self.ui.tableViewkat.setDragDropMode(InternalMove)
        self.ui.tableViewkat.verticalHeader().setVisible(False)  # ukrycie numeracji (tej po lewej)
        self.ui.tableViewkat.setSelectionBehavior(QTableView.SelectRows)  # by caly rekord.
        self.ui.tableViewkat.setSelectionMode(QTableView.SingleSelection)  # by max jedna usuwac jednoczesnie

    def wyswedycjiPodkatkatmodel (self):

        self.model3 = QSqlTableModel()
        self.model3.setTable("kategorie")
        self.model3.setFilter(
            "id_parent < 0 ")  # by wyswietlic na poczatku pusta liste kat - brak mniejszych od zera id rodzicow
        self.model3.setHeaderData(nazwa_kat, Qt.Horizontal, ("Poddziedzina "));
        self.model3.select()
        self.ui.tableViewpodkat.setModel(self.model3)
        self.ui.tableViewpodkat.setColumnHidden(id_kat, True)
        self.ui.tableViewpodkat.setColumnHidden(id_parent, True)
        self.ui.tableViewpodkat.resizeColumnsToContents()
        self.ui.tableViewpodkat.verticalHeader().setVisible(False)  # ukrycie numeracji (tej po lewej)
        self.ui.tableViewpodkat.setSelectionMode(QTableView.SingleSelection)  # by 1 rekord wybieralo
        self.zapelnienieQBoxa()

    def zapelnienieQBoxa (self):
        query = QSqlQuery()
        query.exec_("SELECT nazwa_kat FROM kategorie WHERE id_parent =0")  # znajduje wszystkie kat ( parent=0)
        list = []
        self.ui.comboBoxwybkat.clear()
        while (query.next()):
            list.append(query.value(0).toString())
        self.ui.comboBoxwybkat.addItems(list)

    def wartosccombobox (self):
        query = QSqlQuery()
        query.exec_(
            "SELECT id_kat FROM kategorie WHERE nazwa_kat = '" + self.ui.comboBoxwybkat.currentText() + "'")  # wskazuje  id kat tam gdzie wystapila wartosc z qboxa
        # filtr = "id_parent != 0" #by podkategoria nie byla kat bo kategorie maja 0 # by byly tylko kat wyswietlane
        query.first()
        self.pobrana = query.value(0).toString()
        self.wyborkat = "id_parent = " + str(self.pobrana)
        self.model3.setFilter(self.wyborkat)

    def polaczenia_kat_podkat (self):

        self.ui.pushButton_2.clicked.connect(self.dodajkat)
        self.ui.pushButton_4.clicked.connect(self.dodajpodkat)
        self.ui.pushButton.clicked.connect(self.usunkat)
        self.ui.pushButton_6.clicked.connect(self.usunpodkat)
        self.ui.tableViewkat.clicked.connect(self.zapisz_wybr_kat)
        self.ui.tableViewpodkat.clicked.connect(self.zapisz_wybr_podkat)
        self.ui.comboBoxwybkat.currentIndexChanged.connect(self.wartosccombobox)

    def zapisz_wybr_kat (self,
                         clicked):  # po kliknieciu zapisuje aktualnie wybrany numer kategorii wyswietlanej w table i przypisuje do zmiennej globalnej
        numerwiersza = clicked.row()
        self.wybrana_kat = numerwiersza

    def zapisz_wybr_podkat (self,
                            clicked):  # po kliknieciu zapisuje aktualnie wybrany numer podkategorii wyswietlanej w table i przypisuje do zmiennej globalnej
        numerwiersza = clicked.row()
        self.wybrana_podkat = numerwiersza

    def dodajpodkat (self):

        self.wybranakat = self.ui.comboBoxwybkat.currentText()  # pobrana nazwa kategorii z listy

        # wyszukuje do jakie kat nalezy
        query = QSqlQuery()
        query.exec_("SELECT id_kat FROM kategorie WHERE nazwa_kat ='" + self.wybranakat + "'")
        query.first()
        self.pobraneidkat = query.value(0).toString()
        self.nazwa_nowej_podkat = str(self.ui.lineEdit_2.text())

        # jesli podkategoria nowa ma nazwe kategorii - wyswietl blad
        if (self.wybranakat == self.nazwa_nowej_podkat):
            self.komunikat_bledu = QMessageBox.question(self, 'Message', u"Błędna podkategoria! Popraw!",
                                                        QMessageBox.Ok)
            self.show()
        else:
            query = QSqlQuery()
            query.exec_(
                "INSERT INTO kategorie (id_parent, nazwa_kat) VALUES ('" + self.pobraneidkat + "','" + self.nazwa_nowej_podkat + "')")

            self.model3.select()

    def usunpodkat (self):
        self.numerrekordu = self.wybrana_podkat
        self.nazwa_podkat_del = self.ui.tableViewpodkat.model().record(self.numerrekordu).value(
            nazwa_kat).toString()  # wskazuje na wartosc komorki = wybranej kategorii (nazwe jej)
        # print(self.nazwa_podkat_del)
        query = QSqlQuery()
        query.exec_("DELETE FROM kategorie WHERE id_parent !=0 AND nazwa_kat ='" + self.nazwa_podkat_del + "'")
        if not query.exec_():
            QMessageBox.information(self, u"Błąd", u"Coś poszło nie tak, spróbuj ponownie")

        self.model3.select()

    def dodajkat (self):
        self.nazwa_nowej_kat = str(self.ui.lineEdit.text())

        query = QSqlQuery()
        query.exec_("INSERT INTO kategorie (id_parent, nazwa_kat) VALUES (0, '" + self.nazwa_nowej_kat + "')")
        query.next()

        self.model2.select()
        self.model3.select()

    def usunkat (self):

        self.numerrekordu = self.wybrana_kat
        self.nazwa_kat_del = self.ui.tableViewkat.model().record(self.numerrekordu).value(
            nazwa_kat).toString()  # wskazuje na wartosc komorki = wybranej kategorii (nazwe jej)
        # print(self.nazwa_kat_del)
        query = QSqlQuery()
        query.exec_("DELETE FROM kategorie WHERE id_parent = 0 AND nazwa_kat ='" + self.nazwa_kat_del + "'")
        if not query.exec_():
            QMessageBox.information(self, u"BŁĄ", u"Wpisz inne dane")
        self.model2.select()
        # self.zapelnienieQBoxa()


class okno_dodawania(Ui_Okno_Dodaj):
    def __init__ (self, parent=None):
        super(okno_dodawania, self).__init__(parent)
        self.setWindowFlags(self.windowFlags() ^ Qt.WindowContextHelpButtonHint)
        self.setupUi(self)
        self.model_dod()
        self.mapper2()
        self.katcombobox()
        # self.DodajButton.clicked.connect(self.dodajkkk)
        self.wysw_podkat_w_comboB()
        self.polaczenia_dod()

        sciezka = ""

    def polaczenia_dod (self):
        self.DodajButton.clicked.connect(self.dodajrecord)
        self.comboBox.currentIndexChanged.connect(self.wysw_podkat_w_comboB)
        self.ZalaczButton.clicked.connect(self.dodajplik_sciezka)
        self.UtworzPButton.clicked.connect(self.otworz_edycje_PDF)

    def otworz_edycje_PDF (self):  # otworz.
        dialog = edycjaPDF()
        dialog.exec_()

    def model_dod (self):
        self.modelD = QSqlRelationalTableModel(self)
        self.modelD.setTable("pliki")
        self.modelD.setRelation(5,
                                QSqlRelation("kategorie", "id_kat", "nazwa_kat"))
        self.modelD.setRelation(6,
                                QSqlRelation("kategorie", "id_kat", "nazwa_kat"))

        self.modelD.setSort(0, Qt.AscendingOrder)
        self.modelD.select()

    def dodajrecord (self):

        nazwapliku = self.NazwaLineEdit.text()
        # nazwapliku=nazwapliku.decode('UTF-8')
        opis = self.OpisTextEdit.toPlainText()
        rok_wydania = self.Data_wydaniaLineEdit.text()

        query = QSqlQuery()
        query.exec_(
            "SELECT id_kat FROM kategorie WHERE id_parent =0 AND nazwa_kat = '" + self.comboBox.currentText() + "'")
        while (query.next()):
            dziedzina = query.value(0).toString()

        query.exec_("SELECT id_kat FROM kategorie WHERE nazwa_kat = '" + self.comboBox_2.currentText() + "'")
        while (query.next()):
            poddziedzina = query.value(0).toString()

        autor = self.AutorLineEdit_3.text()
        zrodlo = self.ZrodloLineEdit_2.text()
        (nazwapliku, opis, rok_wydania, dziedzina, poddziedzina, autor, zrodlo)

        # print nazwapliku,opis,rok_wydania,autor,zrodlo,dziedzina,poddziedzina

        try:
            # query = QSqlQuery()
            query.exec_(
                "INSERT INTO pliki (nazwa_pliku, opis, rok_wydania,dziedzina,poddziedzina,autor,zrodlo) VALUES ('%s', '%s', '%s', '%s','%s','%s', '%s')" % (
                    nazwapliku, opis, rok_wydania, int(dziedzina), int(poddziedzina), autor, zrodlo))
            query.first()
        # if not query.exec_(): QMessageBox.information(self, u"Błędne Dane", u"Wystąpił błąd, podaj poprawne dane")
        except ValueError:
            QMessageBox.information(self, u"Błędne Dane", u"Wystąpił błąd, podaj poprawne dane")

        row_n = self.modelD.rowCount()

        if self.ZalaczButton.isEnabled():
            QMessageBox.information(self, u"Brak pliku", u"Musisz załączyć plik PDF")

        else:
            global sciezka

            fl = open(sciezka, 'rb')
            with fl:
                data = fl.read()
            con = lite.connect('repozytorium.db')

            with con:
                cur = con.cursor()
                sql = "UPDATE pliki set LOKALIZACJA = (?) WHERE id_pliki=(SELECT MAX(id_pliki) from pliki)"
                cur.execute(sql, (lite.Binary(data),))

            self.close()

    def dodajplik_sciezka (self):
        global sciezka
        fname = QFileDialog.getOpenFileName(self, 'Wybierz plik PDF do dodania', "*.pdf")
        sciezka = fname
        if len(fname) > 4: self.ZalaczButton.setEnabled(False)

    def mapper2 (self):

        self.mapper = QDataWidgetMapper(self)
        self.mapper.setSubmitPolicy(QDataWidgetMapper.ManualSubmit)
        self.mapper.setModel(self.modelD)
        self.mapper.setItemDelegate(QSqlRelationalDelegate(self))
        row = self.modelD.rowCount()
        self.mapper.submit()
        self.modelD.insertRow(row)
        self.mapper.setCurrentIndex(row)
        # self.katComboBox.setCurrentIndex(0) #by domyslnie zaczynalo od 1# kat
        # self.NazwaLineEdit.setFocus()

    def katcombobox (self):
        relationModel = self.modelD.relationModel(kategorie)
        relationModel.setFilter("id_parent = 0")
        self.comboBox.setModel(relationModel)

        self.comboBox.setModelColumn(
            relationModel.fieldIndex("nazwa_kat"))
        self.comboBox.setModel(relationModel)
        self.mapper.addMapping(self.comboBox, kategorie)

    def wysw_podkat_w_comboB (self):
        query = QSqlQuery()
        query.exec_(
            "SELECT id_kat FROM kategorie WHERE nazwa_kat = '" + self.comboBox.currentText() + "'")  # wskazuje  id kat tam gdzie wystapila wartosc z qboxa
        filtr = "id_parent != 0"  # by podkategoria nie byla kat bo kategorie maja 0 # by byly tylko kat wyswietlane

        while (query.next()):
            filtr = "id_parent = " + query.value(0).toString()

        self.relationModel1 = self.modelD.relationModel(podkategoria)
        self.relationModel1.setFilter(filtr)
        self.comboBox_2.setModel(self.relationModel1)
        self.comboBox_2.setModelColumn(
            self.relationModel1.fieldIndex("nazwa_kat"))
        self.mapper.addMapping(self.comboBox_2, podkategoria)


class edycjaPDF(QDialog):
    def __init__ (self, parent=None):
        super(edycjaPDF, self).__init__(parent)
        self.setWindowTitle("Edycja PDF")
        self.setWindowFlags(self.windowFlags() ^ Qt.WindowContextHelpButtonHint)  # usuniecie "?"
        self.layout = QVBoxLayout(self)
        self.labelnaglowek = QLabel("Utworzenie pliku PDF")
        font = QFont()
        font.setPointSize(9)
        self.labelnaglowek.setFont(font)
        self.przycisksciezki = QPushButton(u"Wybierz plik źródłowy")
        self.przycisksciezki.clicked.connect(self.pobraniesciezkizrodla)

        self.layout.addWidget(self.przycisksciezki)
        self.labeliloscstron = QLabel()
        self.labeliloscstron.setText("{Pusta}")
        self.labelN = QLabel("\n")
        self.labelN1 = QLabel("\n")
        self.layout.addWidget(self.labelN)
        self.label3 = QLabel()
        self.label3.setText(u"Ścieżka pliku źródłowego:")
        self.layout.addWidget(self.label3)
        self.layout.addWidget(self.label3)
        self.layout.addWidget(self.labeliloscstron)
        self.labelwyswstr = QLabel("0")
        self.layout.addWidget(self.labeliloscstron)
        self.layout.addWidget(self.labelwyswstr)
        self.layout.addWidget(self.labelN)
        self.docelowyB = QPushButton(u"Podaj miejsce zapisu")
        self.layout.addWidget(self.docelowyB)
        self.docelowyB.clicked.connect(self.docelowyplik_zapis)
        self.labelzapisz1 = QLabel(u"Ścieżka pliku docelowego:")
        self.layout.addWidget(self.labelzapisz1)
        self.labelzapisz2 = QLabel("{Pusta}")
        self.layout.addWidget(self.labelzapisz2)
        self.layout.addWidget(self.labelN1)
        self.labelstr = QLabel(u"Podaj numery stron \n[oddzielone przecinkiem]")
        self.layout.addWidget(self.labelstr)
        self.iloscstronedit = QLineEdit()
        self.layout.addWidget(self.iloscstronedit)
        self.zapiszbutton = QPushButton("ZAPISZ PLIK")
        self.layout.addWidget(self.zapiszbutton)
        self.zapiszbutton.clicked.connect(self.zapiszplik)

        self.polaczButton = QPushButton(u"Połącz dwa pliki PDF")
        self.polaczButton.clicked.connect(self.laczenieplikow)
        self.przerwa = QLabel()
        self.tekst3 = QLabel(u"Przycisk poniżej łączy dwa pliki PDF.")
        self.layout.addWidget(self.przerwa)
        self.layout.addWidget(self.przerwa)
        self.layout.addWidget(self.tekst3)
        self.layout.addWidget(self.polaczButton)

    def laczenieplikow (self):  ##uzycie pypdf do zlacznia 2 plikow
        pdfOne = QFileDialog.getOpenFileName(self, u'Wybierz pierwszy plik', "*.pdf")
        pdfTwo = QFileDialog.getOpenFileName(self, u'Wybierz drugi plik', "*.pdf")
        QMessageBox.information(self, u"Podaj miejsce zapisu",
                                u"W Następnym oknie podaj miejsce docelowe i nazwe złączonych plików")
        merged = QFileDialog.getSaveFileName(self, u'Docelowy plik', "*.pdf")

        if os.path.exists(pdfOne) and os.path.exists(pdfTwo):
            output = PdfFileWriter()
            pdfOne = PdfFileReader(open(pdfOne, "rb"))
            for page in range(pdfOne.getNumPages()):
                output.addPage(pdfOne.getPage(page))

            pdfTwo = PdfFileReader(open(pdfTwo, "rb"))
            for page in range(pdfTwo.getNumPages()):
                output.addPage(pdfTwo.getPage(page))

            outputStream = open(merged, "wb")
            output.write(outputStream)
            outputStream.close()

    def pobraniesciezkizrodla (self):
        self.sciezkazrodlowego = QFileDialog.getOpenFileName(self, u'Wybierz źródłowy plik PDF do dodania', "*.pdf")
        self.labeliloscstron.setText(self.sciezkazrodlowego)
        input1 = PdfFileReader(file(self.labeliloscstron.text(), "rb"))
        self.labelwyswstr.setText(u"Ilość stron pliku źródłowego : %s " % input1.getNumPages())

    def docelowyplik_zapis (self):
        self.sciezkadocelowego = QFileDialog.getSaveFileName(self, u'Docelowy', "*.pdf")
        self.labelzapisz2.setText(self.sciezkadocelowego)

    def zapiszplik (self):
        try:
            lista = str(self.iloscstronedit.text())
            lista = map(int, lista.split(','))
            # for a in lista: print a


            if str(self.labeliloscstron.text()) != "{Pusta}":
                input1 = PdfFileReader(file(self.labeliloscstron.text(), "rb"))
                output = PdfFileWriter()
                # wydruk ile stron ma zrodlo
                self.labelwyswstr.setText(u"Ilość stron pliku źródłowego :%s " % input1.getNumPages())

                for b in lista:
                    if b <= int(input1.getNumPages()):
                        output.addPage(input1.getPage(b - 1))  # -1 poniewaz zaczyna lista od 0  page(0)=1 str
                    else:
                        QMessageBox.information(self, u"Błąd!", u"Podałeś błędny numer strony")

                if str(self.labelzapisz2.text()) != "{Pusta}":
                    outputStream = file(self.labelzapisz2.text(), "wb")
                    output.write(outputStream)
                    outputStream.close()
                else:
                    QMessageBox.information(self, u"Błąd!", u"Nie podałeś pliku docelowego, popraw")
                    outputStream.close()

            else:
                QMessageBox.information(self, u"Błąd", u"Nie podałeś źródła, popraw")



        except ValueError:
            QMessageBox.information(self, u"Błąd!", u"Błędnedne strony, popraw")


def main ():
    app = QApplication(sys.argv)
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("repozytorium.db")
    form = Repozytorium()
    form.show()
    app.setQuitOnLastWindowClosed(
        False)  # by zamykalo okno w odp kolejnosci, likwiduje "QObject::startTimer: QTimer can only be used with threads started" ... blad
    sys.exit(app.exec_())


main()
