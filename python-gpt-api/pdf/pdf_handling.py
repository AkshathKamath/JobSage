import PyPDF2
import io
import requests

def extract_text_from_pdf(pdf_path):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Windows; Windows x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36'}
    url = pdf_path
    response = requests.get(url=url, headers=headers, timeout=120)
    on_fly_mem_obj = io.BytesIO(response.content)

    reader = PyPDF2.PdfReader(on_fly_mem_obj)
    text = ''
    for page in reader.pages:
        text += page.extract_text()
    return text

# print(extract_text_from_pdf('https://resumehelp.s3.amazonaws.com/Resume.pdf'))
