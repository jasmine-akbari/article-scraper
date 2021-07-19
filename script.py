import pandas as pd
import numpy as np
import PyPDF2
import textract
import re

from colorama import init, Fore, Back, Style

givenFile = input(Fore.CYAN + "What is the name of the PDF File you would like to scrape?")
filename = f'../../articles/PDF/{givenFile}.pdf'


pdfFileObj = open(filename,'rb')               
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)   
num_pages = pdfReader.numPages                 


count = 0
text = ""
desiredWords = ""

# while to loop to cycle through pages
while count < num_pages:                       
    pageObj = pdfReader.getPage(count)
    count +=1
    text += pageObj.extractText()
if text != "":
    text = text
# converts images to text using textract
else:
    text = textract.process('../../articles/PDF/' + givenFile + '.pdf', method='tesseract', language='eng')


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


df = df.sort_values('tf_idf',ascending=False)
df_max_res = df.head(15)

print(df_max_res)

# function to create the csv file from the dataframe created
df_max_res.to_csv('./dist/article_1.csv')
print(Fore.GREEN + 'Please check your repositories /dist folder for the csv file with relevant keywords!')

init()