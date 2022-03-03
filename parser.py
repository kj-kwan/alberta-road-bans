import pandas as pd
import PyPDF2
import re
import os

files = [file for file in os.listdir('./') if '.pdf' in file]

pdfFileObj = open('trans-2004-road-bans-40.pdf','rb')

def parse_pdf(file):
    with open(file,'rb') as f:
        pdfReader = PyPDF2.PdfFileReader(f)




def main():
    parse_pdf(file)

    pass

if __name__ == '__main__':
    main()
