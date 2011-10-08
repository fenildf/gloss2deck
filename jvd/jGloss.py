# -*- coding: utf-8 -*-
import urllib, re

testSentence1 = u'犯人をどこかで見ましたか。'
testSentence2 = u'最近のウィルスは強力で、プログラムを実行しようがしまいが、ページを見るだけで感染するらしい。'
testSentence3 = u'猫はいない。'


#The code on the end of this URL means:
# 9 - Type of dictionary (9 is the gloss dictionary, as recommended)
# Z - Raw server output (instead of the output of the HTML page)
# I - The text we give it is utf8
# G - Glossing, and DO repeat any identical terms
#See: http://www.csse.monash.edu.au/~jwb/wwwjdicinf.html#backdoor_tag
#To use it, we simply append the text we want to gloss to the end of it.
glossURL = 'http://www.csse.monash.edu.au/~jwb/cgi-bin/wwwjdic.cgi?9ZIG'

class Gloss:
    
    def __init__(self, word, reading, meaning):
        self.word = word
        self.reading = reading
        self.meaning = meaning
        #self.highlightedSentence


def __getGlossList(serverResponse):
    '''Returns a list of Gloss objects representing each gloss in the server
    response. serverResponse is the raw server output from the wwwjdic 
    server after bring fed Japanese text.'''
       
    #Find the gloss data from the HTML response
    #Each gloss line is contained within an HTML list item (<li>)
    #Note the superfluous spaces on the inside of the elements.
    pattern = '<li> (.*) </li>'
    liRegEx = re.compile(pattern)
    glossLines = liRegEx.findall(serverResponse)
    
    glosses = []
    for glossLine in glossLines:
        #We need to extract the separate part of the gloss line.
        #Potential cases:
        #Case 1: 犯人 【はんにん】      (n) offender; criminal; (P); ED 
        #Case 2: どこか         (adv,exp,n) somewhere; anywhere; in some respects; KD 
        #Case 3: Possible inflected verb or adjective: (polite, past)<br>見る 見る(P); 観る; 視る 【みる】........etc  
        
        #Only case 1 and 2 can produce glosses. Case 3 is reduced to one of
        #those two before being parsed.
        
        #Handle case 3 above. Get everything after the <br>.
        #Effectively turns case 3 into case 1.
        brSplit = glossLine.split('<br>', 1)
        if len(brSplit) > 1:
            glossLine = brSplit[1] 
    
        #Handle case 1 above. First part is the word portion, second is the 
        #reading, everything else is the explanation    
        pattern = '(.+)【(.+)】(.+)'
        glossPartsRegEx = re.compile(pattern)
        partsList = glossPartsRegEx.findall(glossLine)
        #If matches are found, it's case 1. Else, case 2.
        if len(partsList) > 0:
            for part in partsList:
                kanji = part[0]
                reading = part[1]
                meaning = part[2].strip()
                
                #Sometimes, alternative word are given after the one we are
                #concerned with. E.g., 見る 見る(P); 観る; 視る. Grab only the first.
                kanji = kanji.split(None, 1)[0]
                
                gloss = Gloss(kanji, reading, meaning)
                glosses.append(gloss)
        
        else:   #Handle case 2. Kana-only.    
            reading, meaning = glossLine.split(None, 1)
            kanji = reading
            
            gloss = Gloss(kanji, reading, meaning.strip())
            glosses.append(gloss)
    return glosses
    

def __getGlossResponse(jText):
    '''Query the wwwjdic server for text glossing. Returns the raw server 
    response for the text given.'''
    
    escaped = urllib.quote(jText.encode('utf8'))
    return urllib.urlopen(glossURL + escaped).read()


def getGlossList(sentence):
    serverResponse = __getGlossResponse(sentence)
    glosses = __getGlossList(serverResponse)
    return glosses

if __name__ == '__main__':
    
    for sentence in (testSentence1, testSentence2, testSentence3):
        print '[',sentence,']' 
        serverResponse = __getGlossResponse(sentence)
        glosses = __getGlossList(serverResponse)
    
        print "Glosses:"
        for gloss in glosses:
            print gloss.word, '==', gloss.reading, '==', gloss.meaning
