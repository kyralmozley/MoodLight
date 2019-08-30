import re
import string


def removeNonAscii(s):
    return "".join(i for i in s if ord(i)<126 and ord(i)>31)

def clean_tweet(text):
    text = removeNonAscii(text).lower()
    entity_prefixes = ['@','#']
    text = re.sub('(https?:\/\/)(\s)*(www\.)?(\s)*((\w|\s)+\.)*([\w\-\s]+\/)*([\w\-]+)((\?)?[\w\s]*=\s*[\w\%&]*)*', " ", text) #remove links
    for separator in string.punctuation:
        if separator not in entity_prefixes :
            text = text.replace(separator,' ')
    words = []
    for word in text.split():
        word = word.strip()
        if word:
            if word[0] not in entity_prefixes:
                words.append(word)
    return ' '.join(words)