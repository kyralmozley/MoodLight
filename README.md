# MoodLight
A Python program, performing sentiment analysis of top trending tweets, and setting my Philips Hue to a colour matching the worlds current emotion 
> hence a literal mood light 💡

### Sentiment Analysis 
It uses the NRC Word-Emotion Association Lexicon (NRC Emotion Lexicon). I have 6168 words, where some words have multiple emotions associated with them. 

### Twitter Trending
I use Tweepy, a Python Library for using the Twitter API. I get the top trends in the UK, and then for each trend, get 100 (which is the max Tweepy will return) tweets with that trend and analyse each one. 

### Colour 
The top emotion corrolates to which colour the Philips Hue changes to:

| Emotion       | Colour   |
| ------------- | -------- |
| Anger         | Red      |
| Fear          | Red      |
| Anticipation  | Orange   |
| Surprise      | Purple   |
| Sadness       | Dark Blue|
| Joy           | Yellow   |
| Disgust       | Green    |
| Negative      | Blue     |
| Postitive     | White    |

### TODO
- [ ] Add emoji analysis
- [ ] Find/Generate lexicon with more current/slang/topical words in (e.g. Brexit, fetch)
- [ ] Deal with negation (e.g. Not Happy, where as currently get Happy)
