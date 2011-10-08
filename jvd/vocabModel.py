# -*- coding: utf-8 -*-
from anki.models import Model, CardModel, FieldModel
import anki.stdmodels

def VocabModel():
    m = Model(_("Vocab"))
    m.addFieldModel(FieldModel(u'Expression', True, False))
    m.addFieldModel(FieldModel(u'Reading', False, False))
    m.addFieldModel(FieldModel(u'Meaning', False, False))
    m.addFieldModel(FieldModel(u'From', False, False))
    
    m.addCardModel(CardModel(u"Recognition",
                             #Question side
                             u"%(Expression)s",
                             #Answer side
                             u"%(Reading)s<br>"+
                             u"%(Meaning)s<br>"+
                             u"%(From)s"))
    
    m.tags = u"Japanese Vocab Vocabulary"
    return m

def init():
    anki.stdmodels.models['Vocab'] = VocabModel