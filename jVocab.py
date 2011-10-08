# -*- coding: utf-8 -*-
import os
import datetime
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from jvd.Ui_NewVocabDeckDialog import Ui_NewVocabDeckDialog

from ankiqt import mw
from anki.utils import stripHTML
from anki.hooks import addHook
from anki.facts import Fact, Field, FieldModel, Model
import anki.deck
import jvd.jGloss
import jvd.vocabModel

impendingFacts = {}

class ImpendingFact():
    
    allOrder = 0
    
    def __init__(self, gloss, origSentence):
        self.gloss = gloss #key
        self.addSentence(origSentence)
        self.order = ImpendingFact.allOrder
        ImpendingFact.allOrder = ImpendingFact.allOrder +1


    def addSentence(self, s):
        self.origSentences = [s]
        pass


class NewDeckDiag(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self)

        #I'm storing state in instance variables. I'll figure out the 
        #proper Qt4 way to do it later.

        # Set up the user interface from Designer.
        self.ui = Ui_NewVocabDeckDialog()
        self.ui.setupUi(self)

        self.deckObj = None
        self.modelId = None
        self.fieldModelId = None
        self.fieldModelId = None
        self.outputName = None

        
        deckList = QStringList()
        deckList.append(QString())
        #Fill in deck choices
        self.ui.deckSelect.addItem('')
        for deck in mw.browserDecks:
            self.ui.deckSelect.addItem(deck['name'],
                                       userData=deck['path'])
            
        QObject.connect(self.ui.deckSelect,
                        SIGNAL("activated(QString)"),
                        self.onDeckChosen)
        
        QObject.connect(self.ui.modelSelect,
                        SIGNAL("activated(QString)"),
                        self.onModelChosen)
        
        QObject.connect(self.ui.fieldSelect,
                        SIGNAL("activated(QString)"),
                        self.onFieldModelChosen)  
        
        QObject.connect(self.ui.nextButton,
                        SIGNAL("clicked()"),
                        self.onMakeDeck)  
        


    def resetState(self):
        if self.deckObj is not None:       
            self.deckObj.close()
        self.ui.modelSelect.setEnabled(False)
        self.ui.modelSelect.clear()
        self.ui.fieldSelect.setEnabled(False)
        self.ui.fieldSelect.clear()
        self.ui.nextButton.setEnabled(False)
        self.ui.newDeckName.setText(QString())

    def onDeckChosen(self, deckName):
        self.resetState()
        if self.ui.deckSelect.currentIndex() == 0:
            
            return
        selectionIndex = self.ui.deckSelect.currentIndex()
        deckPath = self.ui.deckSelect.itemData(selectionIndex).toString()
        #Still a QString, make python string
        deckPath = str(deckPath)
        
        print 'jVocab: Using: ' + deckPath
        
        #Open the deck
        self.deckObj = anki.deck.DeckStorage.Deck(deckPath)
        
        self.ui.modelSelect.clear()
        self.ui.modelSelect.addItem('')
        for model in self.deckObj.s.query(Model).all():
            self.ui.modelSelect.addItem(model.name, str(model.id))
            
        self.ui.modelSelect.setEnabled(True)
        
    
    def onModelChosen(self):
        if self.ui.modelSelect.currentIndex() == 0:
            return
        
        selectionIndex = self.ui.modelSelect.currentIndex()
        self.modelId = self.ui.modelSelect.itemData(selectionIndex).toString()
        print self.modelId
        self.modelId = int(self.modelId)
        
        self.ui.fieldSelect.clear()
        self.ui.fieldSelect.addItem('')
        for fieldmodel in self.deckObj.s.query(FieldModel).\
                filter(FieldModel.modelId==self.modelId):
            self.ui.fieldSelect.addItem(fieldmodel.name, fieldmodel.id)
        
        self.ui.fieldSelect.setEnabled(True)
    
    def onFieldModelChosen(self):
        if self.ui.fieldSelect.currentIndex() == 0:
            return
        
        selectionIndex = self.ui.fieldSelect.currentIndex()
        self.fieldModelId = self.ui.fieldSelect.itemData(selectionIndex).toString()
        print self.fieldModelId
        self.fieldModelId = int(self.fieldModelId)
        
        name = 'Vocab of ' + self.deckObj.name()
        self.outputName = name
        self.ui.newDeckName.setText(QString(name))
        self.ui.newDeckName.setEnabled(True)
        self.ui.nextButton.setEnabled(True)


    def onMakeDeck(self):
        self.glossToDeck()
        

    def glossToDeck(self):
        '''deck -- input deck
        model -- model of input deck to find field
        field -- the field to extract vocab from
        outputDeck -- deck to save new vocab cards to'''
    
        fullPath = os.path.join(mw.documentDir, self.outputName + '.anki')
        print 'Making new db: ' + fullPath
        outputDeck = anki.deck.DeckStorage.Deck(fullPath)
        model = jvd.vocabModel.VocabModel()
        outputDeck.addModel(model)
        outputDeck.save()
                 
        
        i = 0
        for fact, field in self.deckObj.s.query(Fact, Field).\
                filter(Fact.id == Field.factId).\
                filter(Field.fieldModelId == self.fieldModelId).\
                order_by(Fact.created):
            
            sentence = stripHTML(field.value).strip()
            
            if len(sentence) > 0:
                glosses = jvd.jGloss.getGlossList(sentence)
                for g in glosses:
                    try:
                        impendingFacts[g.word].origSentences.append(sentence)
                    except:
                        impendingFacts[g.word] = ImpendingFact(g, sentence)
                
            i += 1
            print 'Glossing fact #%d of %d' % (i, self.deckObj.factCount)


        items = len(impendingFacts)
        i = 0
        for (k, ifact) in sorted(impendingFacts.items(), key=lambda t: t[1].order):
            i = i + 1
            print 'saving %s of %s' % (i, items)
            f = outputDeck.newFact()
            for newField in f.fields:
                if newField.name == "Expression":
                    newField.value = unicode(ifact.gloss.word)
                if newField.name == "Reading":
                    newField.value = unicode(ifact.gloss.reading)
                if newField.name == "Meaning":
                    newField.value = unicode(ifact.gloss.meaning)
                if newField.name == "From":
                    newField.value = u''
                    for osnt in ifact.origSentences:
                        newField.value = newField.value +\
                                         unicode(osnt) +\
                                         u'<br>' + ' -- ' + '<br>'

            outputDeck.addFact(f)
        
        outputDeck.save()

    

def onJVocab():
    mw.mainWin.jv = NewDeckDiag(mw)
    mw.mainWin.jv.show()


def init():   
    mw.mainWin.jVocab = QAction('jVocab', mw)
    mw.connect(mw.mainWin.jVocab, SIGNAL('triggered()'), onJVocab)
    mw.mainWin.toolBar.addAction(mw.mainWin.jVocab)
    

mw.registerPlugin("jVocab", 0.1)
addHook('init', init)