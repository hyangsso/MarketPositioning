import re
import os

try:
    import pandas as pd

except ImportError:
    print("Trying to Install required module: pandas\n")
    os.system('python -m pip install pandas')
    import pandas as pd


def only_eng_num(word):
    word = re.sub('[^0-9a-zA-Z]', ' ', word).strip()
    dummy_word = word.replace(' ', '')
    if dummy_word.isdigit():
        word = None
    elif dummy_word == '':
        word = None
    return word


def pp(word):
    spaces = [' ' * x for x in range(2, 10)]
    for space in spaces:
        if space in word:
            word = word.replace(space, '')
    return word


def extract_tag(text):
    res = []
    data = text.split(' ')
    for word in data:
        if word.startswith('#'):
            res.append(word)

    result = []
    for word in res:
        word = re.sub('[^0-9a-zA-Z]', '', word).strip()
        if len(word) > 1:
            result.append('#' + word)

    return ' '.join(result)


def extract_like(text):
    if type(text) == float:
        return 0
    if text.isdigit():
        return int(text)
    if '좋아요' in text:
        start_location = text.find('좋아요')
        end_location = text.find('개')
        return text[start_location + 3: end_location]
    else:
        return 0


