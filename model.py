import re
import pickle
from nltk.stem import WordNetLemmatizer

class Model:

    def __init__(self):
        self.model = pickle.load(open('Sentiment-LR-model.pickle', 'rb'))
        self.incoder = pickle.load(open('Incoder-ngram-(1,2).pickle', 'rb'))
    
    
    def preprocess(self, textdata , wordLemm):
        # dictionary containing all emojis.
        emojis = {':)': 'smile', ':-)': 'smile', ';d': 'wink', ':-E': 'vampire', ':(': 'sad', 
                ':-(': 'sad', ':-<': 'sad', ':P': 'raspberry', ':O': 'surprised',
                ':-@': 'shocked', ':@': 'shocked',':-$': 'confused', ':\\': 'annoyed', 
                ':#': 'mute', ':X': 'mute', ':^)': 'smile', ':-&': 'confused', '$_$': 'greedy',
                '@@': 'eyeroll', ':-!': 'confused', ':-D': 'smile', ':-0': 'yell', 'O.o': 'confused',
                '<(-_-)>': 'robot', 'd[-_-]b': 'dj', ":'-)": 'sadsmile', ';)': 'wink', 
                ';-)': 'wink', 'O:-)': 'angel','O*-)': 'angel','(:-D': 'gossip', '=^.^=': 'cat'}

        processedText = []
        
        # Defining regex patterns.
        urlPattern        = r"((http://)[^ ]*|(https://)[^ ]*|( www\.)[^ ]*)"
        userPattern       = '@[^\s]+'
        alphaPattern      = "[^a-zA-Z0-9]"
        sequencePattern   = r"(.)\1\1+"
        seqReplacePattern = r"\1\1"
        
        for character in textdata:
            character = character.lower()
            
            # Replace all URls with 'URL'
            character = re.sub(urlPattern,' URL',character)
            # Replace all emojis.
            for emoji in emojis.keys():
                character = character.replace(emoji, "EMOJI" + emojis[emoji])        
            # Replace @USERNAME to 'USER'.
            character = re.sub(userPattern,' USER', character)        
            # Replace all non alphabets.
            character = re.sub(alphaPattern, " ", character)
            # Replace 3 or more consecutive letters by 2 letter.
            character = re.sub(sequencePattern, seqReplacePattern, character)
            
            charwords = ''
            for word in character.split():
                if len(word)>1:
                    # Lemmatizing the word.
                    word = wordLemm.lemmatize(word)
                    charwords += (word+' ')
                
            processedText.append(charwords)
            
        return processedText

    def predict(self, text):
        wordLemm = WordNetLemmatizer()
        processedtext = self.preprocess([text], wordLemm)
        x = self.incoder.transform(processedtext)
        prd = self.model.predict(x)
        print(f"prediction = {prd}")
        return prd[0]



