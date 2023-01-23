import PyPDF2

FILE_PATH = 'pdfs\practice-exam-2013-questions-and-answers.pdf'

with open(FILE_PATH, mode='rb') as f:

    text = []

    reader = PyPDF2.PdfReader(f)

    for page_number in range(0, len(reader.pages)):
         page = reader.pages[page_number]
         text.append(page.extract_text())



text
s = '\n'.join(text)
text=s


# q = s + ""