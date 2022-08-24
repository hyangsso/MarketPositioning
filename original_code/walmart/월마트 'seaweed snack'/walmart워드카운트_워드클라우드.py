import pandas as pd
from collections import Counter
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import nltk
data = []
col = 'comment'
df = pd.read_csv("walmartcsv/walmartneg1-2.csv", usecols = [col])
stop_words = nltk.corpus.stopwords.words('english')
stop_words.extend(['halo',"i'm", "ocean's", 'x99s', 'seaweed', 'snack', 'flavor', 'snacks'])

def wordcount(df):
    text = ''
    for i in range(len(df.index)):
        data.append(df[col].iloc[i])
    for i in data:
        text += i

# Cleaning text and lower casing all words
    for char in '-.,\n;[]':
        text = text.replace(char,' ')
    text = text.lower()     #combined text without punctuation

# split returns a list of words delimited by sequences of whitespace (including tabs, newlines, etc, like re's \s)
    word_list = text.split() #words splited
    filtered_list = []  #filtering stop_words
    for word in word_list:
        if word not in stop_words:
            filtered_list.append(word)
    word_count = Counter(filtered_list).most_common()
    print(word_count)

def wordCloud(df):
    text = ''
    for i in range(len(df.index)):
        data.append(df[col].iloc[i])
    for i in data:
        text += i
    for char in '-.,\n;[]':
        text = text.replace(char,' ')
    text = text.lower()
    wc = WordCloud(stopwords = stop_words, background_color='black', max_words=100, collocations=False)
    wc.generate(text)

    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.show()


# wordCloud(df)



