"""
Contains info on Static & Instance Methods
(also decorators)
"""

"""Static & Instance Method"""

class WordSet:
    def __init__(self):
        self.words= set()

    def cleanText(text): #self not used so not needed
        text = text.replace('!', '').replace(',', '').replace('.','')
        return text.lower()

    def addText(self, text): #depends on self, instance method
        text = WordSet.cleanText(text)
        for word in text.split():
            self.words.add(word)

#/ as self not used in def of cleantext, must do class.method
#  to call it, this is called a static method as it is not
#  reliant on self, dependent on class itself

wordSet = WordSet()
wordSet.addText('Hello! My name is Nathan, I\'m 18.')
print(wordSet.words)

print('------------------')

class WordSet:
    replacePuncs = ['!', '.', ',', '\'']
    def __init__(self):
        self.words= set()

    def cleanText(text):
        for punc in WordSet.replacePuncs:
            text = text.replace(punc, '')
        return text.lower()

    def addText(self, text):
        text = WordSet.cleanText(text)
        for word in text.split():
            self.words.add(word)

wordSet = WordSet()
wordSet.addText('Hello! My name is Nathan, I\'m 18.')
print(wordSet.words)

#/ for static variables, we could use self. or class. depending
#  on what we decide to use, but if we use self. for addText,
#  it will attempt to input self as a variable, which is undefined
#  cleanText even though we know it's a static method

print('------------------')

"""Decorators"""

#/ We use decorators to inform python of things eg.
class WordSet:
    replacePuncs = ['!', '.', ',', '\'']
    def __init__(self):
        self.words= set()

    @staticmethod
    def cleanText(text):
        for punc in WordSet.replacePuncs:
            text = text.replace(punc, '')
        return text.lower()

    def addText(self, text):
        text = self.cleanText(text)
        for word in text.split():
            self.words.add(word)
#/ @staticmethod tells python its a static method so it
#  won't try to pass the class instance through, meaning
#  we can use self.cleanText

wordSet = WordSet()
wordSet.addText('Hello! My name is Nathan, I\'m 18.')
print(wordSet.words)

