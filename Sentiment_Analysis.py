from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import speech_recognition as sr
recognizer=sr.Recognizer()
with sr.Microphone() as source:
    print('Clearing background noise')
    recognizer.adjust_for_ambient_noise(source,duration=1)
    print('Waiting for your message')
    recorderdaudio=recognizer.listen(source)
    print('Done Recording')
try:
    print('Printing the message')
    text=recognizer.recognize_google(recorderdaudio,language='en-US')
    print('Your message:{}'.format(text))
except Exception as ex:
    print(ex)
#Performing Sentiment Analysis
Sentence=[str(text)]
analyzer=SentimentIntensityAnalyzer()
for i in Sentence:
    v=analyzer.polarity_scores(i)
    print(v)


