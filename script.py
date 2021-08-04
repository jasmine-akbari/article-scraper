# import re
# import numpy as np
# desiredWords = ""

import pandas as pd
import PyPDF2
import textract
from colorama import init, Fore, Back, Style

from gensim.summarization import keywords
import warnings

warnings.filterwarnings("ignore")

# function prompt user
def init():
    print(Fore.CYAN + 'Welcome to Amesite\'s Article Scraper! This application will search\nany given PDF File for important Key Words and Topics. \n')

    try:
        givenFile = input(Fore.CYAN + 'Please type the name of the PDF File you would like to search to begin.\n' + Fore.YELLOW + 
        '(Please make sure the PDF File you would like to search is saved in the same location you saved this application)')
        extract_keywords(givenFile)
    except:
        print(Fore.RED + 'Sorry! The file name you provided does not exist, please confirm your file name and file type before you try again.')
        try_again = input(Fore.CYAN + 'Would you like to try again? (Type yes|y to continue or tap the enter key to exit)')
        rerun_script(try_again)


def rerun_script(try_again):
    response = try_again.lower()
    print(response)

    if response == 'yes' or response == 'y':
        init()
    else:
        print(Fore.GREEN + 'Thank you for using Amesite\'s Article Scraper, have a good day!')
        return


def extract_keywords(givenFile):

    filename = f'../{givenFile}.pdf'
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
        text = textract.process(f'../../articles/PDF/{givenFile}.pdf', method='tesseract', language='eng')
    create_csv(text)


def create_csv(text):
    text = text.lower()
    values = keywords(text=text,split='\n',scores=True)
    data = pd.DataFrame(values,columns=['keyword','score'])
    data = data.sort_values('score',ascending=False)
    df_max_res = data.head(15)

    # create file with keywords
    df_max_res.to_csv('./dist/article_1.csv')
    print(Fore.GREEN + 'Success! Please check this application\'s "dist" folder for the csv file created with relevant keywords!')

init()