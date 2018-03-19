#################################
import random
#################################
import datetime
currentDT = datetime.datetime.now()
dateString = currentDT.strftime("%A %m/%d/%Y %H:%M:%S")
#################################
# filePath = '/Users/user/Desktop/python wkshp/ScrabbleWordList.txt'
# textFile = open(filePath, 'r')
# words = textFile.read().split('\n')
# textFile.close()
#################################
ptsPerInch = 72
paperWidth = 11*ptsPerInch
paperHeight = 8.5*ptsPerInch

size(paperWidth, paperHeight)
x, y, w, h = ptsPerInch, ptsPerInch, 9*ptsPerInch, 6.5*ptsPerInch

fontPath = '/Users/user/Documents/RoboFonts/tcw2/tbd2/tbd2.1.otf'
fontName = installFont(fontPath)

lettersUC = 'habirf'
lettersLC = 'hair'
### Helper functions ############
def setFont(size, ratio=1.1):
    font(fontName, size)
    lineHeight(size * ratio)
    
def spacingStringUC(letter):
    return('HH' + letter + 'HHOO' + letter + 'OO')
    
def spacingStringLC(letter):
    return('hh' + letter + 'nn oo' + letter + 'oo')
    
def testRect(x, y, w, h):
    fill(None); stroke(0)
    rect(x, y, w, h)
    fill(0); stroke(None)

def renderFooter(info=''):
    fSize = 10
    fontSize(fSize)
    lineHeight(fSize * 1.5)
    text(fontName + ' ' + info + '\n' + dateString, (x, y-fSize*2+fSize/2))
    text(str(pageCount()), (w+x, y-fSize*3))
    
def getValidWords(letters, lowercase=True):
    foundWords = []
    for word in words:
        if lowercase:
            word = word.lower()
        goodWord = True
        for letter in word:
            if not letter in letters:
                goodWord = False
                break 
        if goodWord is True:
            foundWords.append(word)
    return foundWords
    
def renderParagraph(words, numberOfWords):
    storyText = ''
    for i in range(numberOfWords):
        storyText += random.choice(words) + ' '
    textBox(storyText, (x, y, w, h))
#################################
# Page 1:
# Large text showing of the full character set
renderFooter()
setFont(size=144, ratio=0.8)
textBox(lettersUC + '\n' + lettersLC + '\nfriar', (x, y, w, h))
