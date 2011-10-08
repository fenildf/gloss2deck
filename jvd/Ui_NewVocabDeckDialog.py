# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newVocabDeck.ui'
#
# Created: Mon Oct  3 03:58:27 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_NewVocabDeckDialog(object):
    def setupUi(self, NewVocabDeckDialog):
        NewVocabDeckDialog.setObjectName(_fromUtf8("NewVocabDeckDialog"))
        NewVocabDeckDialog.resize(663, 344)
        NewVocabDeckDialog.setWindowTitle(QtGui.QApplication.translate("NewVocabDeckDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label = QtGui.QLabel(NewVocabDeckDialog)
        self.label.setGeometry(QtCore.QRect(10, 50, 276, 16))
        self.label.setText(QtGui.QApplication.translate("NewVocabDeckDialog", "Deck:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.deckSelect = QtGui.QComboBox(NewVocabDeckDialog)
        self.deckSelect.setGeometry(QtCore.QRect(10, 70, 641, 24))
        self.deckSelect.setObjectName(_fromUtf8("deckSelect"))
        self.label_2 = QtGui.QLabel(NewVocabDeckDialog)
        self.label_2.setGeometry(QtCore.QRect(10, 110, 421, 16))
        self.label_2.setText(QtGui.QApplication.translate("NewVocabDeckDialog", "Model:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.modelSelect = QtGui.QComboBox(NewVocabDeckDialog)
        self.modelSelect.setEnabled(False)
        self.modelSelect.setGeometry(QtCore.QRect(10, 130, 191, 24))
        self.modelSelect.setObjectName(_fromUtf8("modelSelect"))
        self.label_3 = QtGui.QLabel(NewVocabDeckDialog)
        self.label_3.setGeometry(QtCore.QRect(10, 170, 421, 16))
        self.label_3.setText(QtGui.QApplication.translate("NewVocabDeckDialog", "Field", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.fieldSelect = QtGui.QComboBox(NewVocabDeckDialog)
        self.fieldSelect.setEnabled(False)
        self.fieldSelect.setGeometry(QtCore.QRect(10, 190, 191, 24))
        self.fieldSelect.setObjectName(_fromUtf8("fieldSelect"))
        self.newDeckName = QtGui.QLineEdit(NewVocabDeckDialog)
        self.newDeckName.setEnabled(False)
        self.newDeckName.setGeometry(QtCore.QRect(10, 260, 631, 23))
        self.newDeckName.setText(_fromUtf8(""))
        self.newDeckName.setObjectName(_fromUtf8("newDeckName"))
        self.label_4 = QtGui.QLabel(NewVocabDeckDialog)
        self.label_4.setGeometry(QtCore.QRect(10, 240, 421, 16))
        self.label_4.setText(QtGui.QApplication.translate("NewVocabDeckDialog", "Name of new deck:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(NewVocabDeckDialog)
        self.label_5.setGeometry(QtCore.QRect(50, 10, 571, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setText(QtGui.QApplication.translate("NewVocabDeckDialog", "Create a new deck from the vocabulary of an existing deck.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.widget = QtGui.QWidget(NewVocabDeckDialog)
        self.widget.setGeometry(QtCore.QRect(290, 310, 351, 26))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.cancelButton = QtGui.QPushButton(self.widget)
        self.cancelButton.setText(QtGui.QApplication.translate("NewVocabDeckDialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.horizontalLayout.addWidget(self.cancelButton)
        self.nextButton = QtGui.QPushButton(self.widget)
        self.nextButton.setEnabled(False)
        self.nextButton.setText(QtGui.QApplication.translate("NewVocabDeckDialog", "Next", None, QtGui.QApplication.UnicodeUTF8))
        self.nextButton.setObjectName(_fromUtf8("nextButton"))
        self.horizontalLayout.addWidget(self.nextButton)

        self.retranslateUi(NewVocabDeckDialog)
        QtCore.QMetaObject.connectSlotsByName(NewVocabDeckDialog)

    def retranslateUi(self, NewVocabDeckDialog):
        pass

