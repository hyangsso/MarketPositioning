import pandas as pd
from collections import Counter
import nltk
import csv

data = []
col = 'product_name'
df = pd.read_excel("no_dup_merged_seaweed_words.xlsx", usecols = [col])
#add words to be removed
# stop_words = nltk.corpus.stopwords.words('english')
# stop_words.extend(['Jayone', 'Tao Kae Noi','Pinkfong', 'seaweed', 'kae', 'noi','x'])

#create excel file
# file = open('seaweed_-1_+1_with.csv', 'w')
# writer = csv.writer(file)
# writer.writerow(['word-1', 'word', 'word+1'])
#writer.writerow(['word-2','word-1','word', 'word+1','word+2'])
def words_with(df):
    text = ''
    for i in range(len(df.index)):
        data.append(df[col].iloc[i])
    for i in data:
        text += str(i)

# Cleaning text and lower casing all words
    for char in '-,\n;[]?!$()&':
        text = text.replace(char,' ')
    text = text.lower()     #combined text without punctuation

# split returns a list of words delimited by sequences of whitespace (including tabs, newlines, etc, like re's \s)
    word_list = text.split() #words splited
    print(word_list)
    for i in range(len(word_list)):
        word = word_list[i]
        if word == "seaweed":
            after = word_list[i-1:i+2]
            print(after)
            # writer.writerow(after)

words_with(df)