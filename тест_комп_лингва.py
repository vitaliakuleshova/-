
#A

mydict = {}
with open('text_for_test.txt', encoding='utf8') as f:
  f = f.read()
  text = f.replace('?', '.').replace('!', '.').replace('...', '.')
  for sentence in text.split("."):
      mydict[sentence] = len([j for j in sentence.split() if len(j)==1 ])
  l = text.split(' ')
  c = text.count('.')
print('а)1.Среднее количество слов в предложении:',len(l)/c)
dp = [(value, key) for key, value in mydict.items()]
print ("a)2.Предложение с максимальным количеством односимвольных слов:", max(dp)[1])

#Б

import re
import string
frequency = {}
document_text = open('text_for_test.txt', encoding='utf8' )
text_string = document_text.read().lower()
match_pattern = re.findall(r'ответил\b', text_string)
for word in match_pattern:
    count = frequency.get(word,0)
    frequency[word] = count + 1
frequency_list = frequency.keys()
for words in frequency_list:
    print ('Количество слов "ответил" в файле:',frequency[words])
file = open('text_for_test.txt', encoding='utf8' )
data = file.read()
w = data.split()
print('Количество слов в файле:', len(w))
print('2.tf для слова "ответил":',frequency[words]/len(w))



