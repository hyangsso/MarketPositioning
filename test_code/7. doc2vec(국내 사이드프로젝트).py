import os

try:
    import pandas as pd

except ImportError:
    print("Trying to Install required module: pandas\n")
    os.system('python -m pip install pandas')
    import pandas as pd

try:
    import gensim

except ImportError:
    print("Trying to Install required module: gensim\n")
    os.system('python -m pip install gensim')
    import gensim


"""
* 회사 내부 데이터로 학습하여 학습 코드는 주석처리 했습니다.

def tagged_document(list_of_list_of_words):
    for i, list_of_words in enumerate(list_of_list_of_words):
        yield gensim.models.doc2vec.TaggedDocument(list_of_words, [i])


data = []
with open('sample_text.txt', encoding='utf-8-sig') as file:
    for line in file:
        word = line.split()
        data.append(word)


data_for_training = list(tagged_document(data))

model = gensim.models.doc2vec.Doc2Vec(vector_size=40, min_count=2, epochs=30)
model.build_vocab(data_for_training)
model.train(data_for_training, total_examples=model.corpus_count, epochs=model.epochs)

save_as = './model/doc2vec_kr.model'
word2vec_file = save_as + ".word2vec_format"

model.save(save_as)
model.save_word2vec_format(word2vec_file, binary=False)
"""

model = gensim.models.Doc2Vec.load("./doc2vec/model/doc2vec_kr.model")

source = model.wv.most_similar(u'소스', topn=10)
dressing = model.wv.most_similar(u'드레싱', topn=10)
snack_source = model.wv.most_similar(positive=[u'과자', u'소스'], topn=10)

source = pd.DataFrame(source, columns=['단어', '유사도'])
dressing = pd.DataFrame(dressing, columns=['단어', '유사도'])
snack_source = pd.DataFrame(snack_source, columns=['단어', '유사도'])


print("소스와 관련된 유사어", end='\n\n')
print(source)

print("드레싱 관련된 유사어", end='\n\n')
print(dressing)

print("[과자, 소스] 동시에 관련된 유사어", end='\n\n')
print(snack_source)
