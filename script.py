import pandas as pd
import numpy as np
import PyPDF2
import textract
import re
# outputs collected data to csv file for readability
import csv

filename ='./assets/articles/20.08.07.Blockchain.Lecture1.pdf' 

pdfFileObj = open(filename,'rb')               
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)   
num_pages = pdfReader.numPages                 


count = 0
text = ""
                                                            
while count < num_pages:                       
    pageObj = pdfReader.getPage(count)
    count +=1
    text += pageObj.extractText()
    
if text != "":
    text = text
 
else:
    text = textract.process('http://bit.ly/epo_keyword_extraction_document', method='tesseract', language='eng')


print(type(text))
# commented out for testing
# text = text.encode('ascii','ignore').lower()
keywords = re.findall(r'[a-zA-Z]\w+',text)

# data/words collected from the article
df = pd.DataFrame(list(set(keywords)),columns=['keywords'])


# formatting for data collected
def weightage(word,text,number_of_documents=1):
    word_list = re.findall(word,text)
    number_of_times_word_appeared =len(word_list)
    tf = number_of_times_word_appeared/float(len(text))
    idf = np.log((number_of_documents)/float(number_of_times_word_appeared))
    tf_idf = tf*idf
    return number_of_times_word_appeared,tf,idf ,tf_idf 


    
df['number_of_times_word_appeared'] = df['keywords'].apply(lambda x: weightage(x,text)[0])
df['tf'] = df['keywords'].apply(lambda x: weightage(x,text)[1])
df['idf'] = df['keywords'].apply(lambda x: weightage(x,text)[2])
df['tf_idf'] = df['keywords'].apply(lambda x: weightage(x,text)[3])

df = df.sort_values('tf_idf',ascending=True)
df.head(25)

print(df)

# function to create the csv file from the table data created
# with open ('article1.cv','wb') as file:
#    writer = csv.writer(file)
#    for row in df:
#         writer.writerow(row)

df.to_csv('article_1.csv')