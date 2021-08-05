# article-scraper

Running 'python3 script.py' in your VS Code or mac terminal while in the working directory of the application will prompt the user to provide a PDF file for key word extraction. Upon successful delivery of a PDF file the application will produces a CSV document displaying 15 relevant keywords found from a provided, and locally saved pdf document. The keywords are displayed in ascending order of relevance to the article.

## Table of Contents

[Technologies](Technologies)
[Installation](Installation)
[Usage](Usage)
[Contributions](Contributions)

## Technologies

Requires the following installations to terminal:
- python3
- pip
- textract
- pandas
- PyPDF2
- colorama (optional)
- gensim v3.8.3

## Installation
1. Clone the Repo
Clone this repository to your local machine(PC). Click on the clipboard icon to copy the URL for git cloning.

![step1](git-clone-img.PNG)

2. Open your Terminal (Mac)
On your Mac, do one of the following: Click the Launchpad icon in the Dock, type Terminal in the search field, then click Terminal. 

OR

In the Finder , open the /Applications/Utilities folder, then double-click Terminal.

![step2](launchpad-img.PNG) ![step2b](terminal-icon-img.PNG)

3. Type 'ls' to see your accesible folders. You can use 'cd ' followed by the name of the folder you wish to navigate into to save your article scraper. (To ensure the application runs properly, save your article PDF's in the same folder).

Commonly repositories are saved in a 'code' file in the documents folder. To make a file, type 'mkdir ' followed by the name of 
the file you want to create.

4. Type 'git clone ' followed by the URL you copied earlier in Step 1.

## Usage


## Contributions

Primary resource used: [How to Extract Keywords From PDFs](https://towardsdatascience.com/how-to-extract-keywords-from-pdfs-and-arrange-in-order-of-their-weights-using-python-841556083341)