# 
# --- see https://radimrehurek.com/gensim_3.8.3/index.html docs on gensim keyword extraction ---
# 
# --- see https://textract.readthedocs.io/en/stable/python_package.html docs on textract text extraction ---
# 

import pandas as pd
import PyPDF2
import textract
from colorama import init, Fore, Back, Style

from gensim.summarization import keywords
import warnings

warnings.filterwarnings("ignore")

# function prompt user
def init():
    print(Fore.MAGENTA + Style.BRIGHT + 'Welcome to Article Scraper! This application will search\nany given PDF File for important Key Words and Topics. \n')

    try:
        givenFile = input(Fore.MAGENTA + Style.BRIGHT + 'Please type the name of the PDF File you would like to search to begin.\n' + Fore.WHITE + 
        '(Please make sure the PDF File you would like to search is saved in the same location you saved this application)')
        extract_keywords(givenFile)
    except:
        print(Fore.RED + Style.NORMAL + 'Sorry! The file name you provided does not exist, please confirm your file name and file type before you try again.')
        try_again = input(Fore.MAGENTA + Style.BRIGHT + 'Would you like to try again? (Type yes|y to continue or the enter key to exit)')
        rerun_script(try_again)


def rerun_script(try_again):
    response = try_again.lower()

    if response == 'yes' or response == 'y':
        init()
    else:
        print(Fore.WHITE + Style.BRIGHT + 'Thank you for using Article Scraper, have a good day!')
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
    try: 
        text = text.lower()

        # words to neglect
        stopwords = {'http', 'https', 'com', 'www'}
        for i in stopwords:
            remove_stopwords = text.replace(i,'')
            text = remove_stopwords

        # gensim specific metrics for keywords to be returned
        values = keywords(text=text,split='\n',scores=True,lemmatize=True)
        data = pd.DataFrame(values,columns=['keyword','score'])
        data = data.sort_values('score',ascending=False)
        df_max_res = data.head(15)

        # create file with keywords
        df_max_res.to_csv('./dist/article_1.csv')
        print(Fore.MAGENTA + Style.BRIGHT + 'Success! Please check this application\'s "dist" folder for the csv file created with relevant keywords!')
    except:
        print(Fore.RED + Style.BRIGHT + 'Sorry! Something went wrong with sorting the words in the PDF File, try another document.')
        try_again = input(Fore.MAGENTA + Style.BRIGHT + 'Would you like to try again? (Type yes|y to continue or the enter key to exit)')
        rerun_script(try_again)
init()
