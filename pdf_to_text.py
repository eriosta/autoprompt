import PyPDF2
import pandas as pd
import os
import glob

def read_pdfs(path):

    """
    This function reads PDF files and converts all text data into a single string.
    
    Parameters
    ----------
    path : character, string
        Path to the directory with PDF files
        
    Returns
    -------
    A character string with all text data from PDF files
    """

    ls = []

    for file in os.listdir(path):

        file_full = path + '/' + file

        with open(file_full, mode='rb') as f:

            text = []

            reader = PyPDF2.PdfReader(f)

            for page_number in range(0, len(reader.pages)):
                page = reader.pages[page_number]
                text.append(page.extract_text())
            
            text = '\n'.join(text)
            ls.append(text)

    return ('\n'.join(ls))

text = read_pdfs('pdfs')

len(text)