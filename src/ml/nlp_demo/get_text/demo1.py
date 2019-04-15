# import PyPDF2
from PyPDF2 import PdfFileReader
import PyPDF2
# import docx
from pprint import pprint

import requests
import json

def parse_json():
    r = requests.get("https://quotes.rest/qod.json")
    res = r.json()
    print(json.dumps(res, indent=4))
    pprint(res['contents']['quotes'][0]['length'])

def parse_pdf(file_path):
    with open(file_path, 'rb') as pdf:
        pdf_reader = PyPDF2.PdfFileReader(pdf)
        print(pdf_reader.numPages)
        page = pdf_reader.getPage(0)
        print(page.extractText().decode("utf-8"))

file = "F:/data/text.pdf"
parse_pdf(file)





