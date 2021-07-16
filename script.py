import pandas as pd
import numpy as np
import PyPDF2
import textract
import re

# File to scrape text from
filename ='./assets/articles/20.08.07.Blockchain.Lecture1.pdf' 

pdfFileObj = open(filename,'rb')               
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)   
num_pages = pdfReader.numPages                 


count = 0
text = ""

# while to loop to cycle through pages
while count < num_pages:                       
    pageObj = pdfReader.getPage(count)
    count +=1
    text += pageObj.extractText()

# checks to see if words were returned
if text != "":
    text = text

# converts images to text using textract
else:
    text = textract.process('./assets/articles/20.08.07.Blockchain.Lecture1.pdf', method='tesseract', language='eng')


print(type(text))
# commented out for testing #
# text = text.encode('ascii','ignore').lower()
#

keywords = re.findall(r'[a-zA-Z]\w+',text)

# creates data frame from words pulled from the article
df = pd.DataFrame(list(set(keywords)),columns=['keywords'])


# formatting/columns for data collected
def weightage(word,text,number_of_documents=1):
    word_list = re.findall(word,text)
    number_of_times_word_appeared =len(word_list)
    tf = number_of_times_word_appeared/float(len(text))
    idf = np.log((number_of_documents)/float(number_of_times_word_appeared))
    tf_idf = tf*idf
    return number_of_times_word_appeared,tf,idf ,tf_idf 


# calculating term frequency   
df['number_of_times_word_appeared'] = df['keywords'].apply(lambda x: weightage(x,text)[0])
df['tf'] = df['keywords'].apply(lambda x: weightage(x,text)[1])
df['idf'] = df['keywords'].apply(lambda x: weightage(x,text)[2])
df['tf_idf'] = df['keywords'].apply(lambda x: weightage(x,text)[3])

df = df.sort_values('tf_idf',ascending=True)
df.head(25)

print(df)

# function to create the csv file from the dataframe created
df.to_csv('./dist/article_1.csv')