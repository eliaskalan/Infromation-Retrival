file= open('doc.txt',encoding='utf8')
read=file.read()
file.seek(0)
read
  
# to obtain the
# number of lines
# in file
line = 1
for word in read:
    if word == '\n':
        line += 1
  
# create a list to
# store each line as
# an element of list
array = []
for i in range(line):
    array.append(file.readline())


punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
for ele in read:  
    if ele in punc:  
        read = read.replace(ele, " ")  
          
  
# to maintain uniformity
read=read.lower()                    
print(read)

from nltk.tokenize import word_tokenize
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')
for i in range(1):
    # this will convert
    # the word into tokens
    text_tokens = word_tokenize(read)
  
tokens_without_sw = [
    word for word in text_tokens if not word in stopwords.words()]
  
print(tokens_without_sw)

dict = {}
  
for i in range(line):
    check = array[i].lower()
    for item in tokens_without_sw:
  
        if item in check:
            if item not in dict:
                dict[item] = []
  
            if item in dict:
                dict[item].append(i+1)
  
print(dict)