# article-scraper

Article Scraper is a CLI(Command Line Interface) application for the purpose of extracting keywords from PDF Files. 

By typing 'python3 script.py' in your VS Code or mac terminal while in the working directory of the application will prompt the user to provide a PDF file for key word extraction. Upon successful delivery of a PDF file, the application will produces a CSV document displaying 15 relevant keywords found from the locally saved PDF document. The keywords are displayed in ascending order by relevance.

## Table of Contents

- [Technologies](#Technologies)
- [Installation](#Installation)
- [Usage](#Usage)
- [Contributions](#Contributions)

## Technologies

Requires the following installations:
- Homebrew
- VS Code
- python3
- pip
- textract
- PyPDF2
- colorama (optional)
- gensim v3.8.3

## Installation
- You can install Python3 by clicking on the following link: [Download Python3](https://www.python.org/downloads/).
- You can install VS Code by clicking on the following link: [Download VS Code](https://code.visualstudio.com/download).
- You can install Homebrew by clicking on the following link: [Download Homebrew](https://brew.sh/)

1. Clone the Repo
To use this application you will need to clone this repository to your local machine(PC). Click on the clipboard icon to copy the URL for git cloning.

![step1](/src/images/git-clone-img.png)

2. Open your Terminal (Mac)
On your Mac, do one of the following: Click the Launchpad icon in the Dock, type Terminal in the search field, then click Terminal. OR in the Finder , open the /Applications/Utilities folder, then double-click Terminal.

![step2](/src/images/launchpad-img.png)

![step2b](/src/images/terminal-icon-img.png)

3. Type 'ls' to see your accesible folders. You can use 'cd ' followed by the name of the folder you wish to navigate into to save your article scraper. (To ensure the application runs properly, save your article PDF's in the same folder). Common practice is to save repositories in a 'code' file in the documents folder. To make a file, type 'mkdir ' followed by the name of the file you want to create.

4. Type 'git clone ' followed by the URL you copied earlier in Step 1. Once this command has completed executing 'cd' into the 
article scraper folder and type 'code .' to open in VS Code.

5. In order for this application to run you will need to type the following commands to install the required packages:
    - brew install pip
    - pip install PyPDF2
    - pip install textract
    - pip install regex
    - pip install gensim==v3.8.3
    - pip install colorama (optional: colors the command line text, purely aesthetic)


## Usage

To trigger the prompts, type 'python3 script.py' in your command line. Follow the prompts and provide the name of the PDF you have locally saved. Once you've received the success message you can view the keyword CSV document in this repositories 'dist' folder.

![initial prompt](/src/images/initial-prompt.png)
![success message](/src/images/success-img.png)

This is what a preview of the CSV will look like from VS Code:

![sample preview](/src/images/sample-preview.png)

## Contributions

[jasmine-akbari](https://github.com/jasmine-akbari) Please contact jasmine_akbari@amesite.com for inquiries regarding contributions.
