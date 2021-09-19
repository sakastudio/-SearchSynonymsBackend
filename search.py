from datetime import datetime

from gensim.models import word2vec
import sys

model = word2vec.KeyedVectors.load_word2vec_format("wiki_model.txt")
args = sys.argv
search = args[1]
number = int(args[2])

words = []
for word in model.most_similar(positive=[search], topn=number):
    words.append(str(word).split("'")[1])

print(str(words))
