import collections
def compute_tf(text):
    tf_text = collections.Counter(text)
    for i in tf_text:
        tf_text[i] = tf_text[i]/float(len(text))
    return tf_text
import math
text1=[]
text2=[]
with open('Tom.txt', 'r') as myself:
    for word in myself.read().split():
        text1.append (word)
with open('Life.txt', 'r') as myself:
    for word in myself.read().split():
        text2.append (word)

print("idf 1-ого текста:")
print (compute_tf(text1))
print("idf 2-ого текста:")
print (compute_tf(text2))
#######################

def compute_idf(word,corpus):
    return math.log10(len(corpus)/sum([1.0 for i in corpus if word in i]))

text1=[]
with open('Tom.txt', 'r') as myself:
    for word in myself.read().split():
        text1.append (word)
text2=[]
with open('Life.txt', 'r') as myself:
    for word in myself.read().split():
        text2.append (word)

print("tdf слова:")
print (compute_idf('дом',text1))
print (compute_idf('стол',text2))


########################

from collections import Counter
import math

def compute_tfidf(corpus):
    def compute_tf(text):
        tf_text = Counter(text)
        for i in tf_text:
            tf_text[i] = tf_text[i]/float(len(text))
        return tf_text
    def compute_idf(word, corpus):
        return math.log10(len(corpus)/sum([1.0 for i in corpus if word in i]))
    documents_list = []
    for text in corpus:
        tf_idf_dictionary = {}
        computed_tf = compute_tf(text)
        for word in computed_tf:
            tf_idf_dictionary[word] = computed_tf[word] * compute_idf(word, corpus)
        documents_list.append(tf_idf_dictionary)
    return documents_list

text1=[]
text2=[]

with open('Tom.txt', 'r') as myself:
    for word in myself.read().split():
        text1.append (word)
with open('Life.txt', 'r') as myself:
    for word in myself.read().split():
        text2.append (word)
corpus=[text1,text2]
print (compute_tfidf([text1,text2]))

