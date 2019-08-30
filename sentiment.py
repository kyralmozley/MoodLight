# I am using NRC Word-Emotion Association Lexicon (NRC Emotion Lexicon)
#defines the following emotions: anger, fear, anticipation, trust, surprise, sadness, joy, and disgust
#as well as negative or positive

filepath = 'Emotion-Lexicon.txt'
lexiconDic = {}

#create a dictionary of words to emotion
with open(filepath) as fp:
   line = fp.readline()
   while line:
       if not (line.__contains__('0')) and not (line.__contains__('trust')):
           lexicon = line.split()
           lexiconDic[lexicon[0]] = lexicon[1]
       line = fp.readline()


def getSentiment(tweet):
    emotions = {
        'anger': 0, 'fear': 0, 'anticipation': 0, 'surprise': 0, 'sadness': 0, 'joy': 0, 'disgust': 0,
        'negative': 0, 'positive': 0
    }

    #split tweet into tokens
    tokens = tweet.split()
    for token in tokens:
        if token in lexiconDic:     #if token exists in diectionary, get its emotion and add to emotion dic
            emotion = lexiconDic.get(token)
            emotions[emotion] = emotions.get(emotion) + 1
    emotion = max(emotions, key=emotions.get) #the emotion for this tweet is the most common

    #this solves an issue where, if no tokens in tweet are in dic, then all = 0 so would be assigned anger
    if emotion == 'anger' and emotions['anger'] == 0:
        return ''
    else:
        return emotion
