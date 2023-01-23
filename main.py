import os
import openai

import PyPDF2
import pandas as pd
import os
import glob

def read_pdf(path,from_page=0, until_page=None):

  """
  This function reads a SINGLE PDF file and converts all text data into a single string.
  
  Parameters
  ----------
  path : character, string
      Path to single PDF file
      
  Returns
  -------
  A character string with all text data from PDF file
  """
  with open(path, mode='rb') as f:

      text = []

      reader = PyPDF2.PdfReader(f)

      if until_page == None:
          until_page = len(reader.pages)

      for page_number in range(from_page, until_page):
          page = reader.pages[page_number]
          text.append(page.extract_text())
      
      text = '\n'.join(text)
  return text

openai.api_key = os.getenv("OPENAI_API_KEY")

YOUR_QUESTION = "What is an incident-response plan?"

prompt = read_pdf(path='pdfs\practice-exam-2013-questions-and-answers.pdf',from_page=11) + ". " + YOUR_QUESTION

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=prompt,
  temperature=0.3,
  max_tokens=100,
  top_p=1,
  frequency_penalty=0.5,
  presence_penalty=0
)

text = response['choices'][0]['text']
print(text)


