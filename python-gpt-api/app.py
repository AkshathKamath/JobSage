from fastapi import FastAPI, Request
import uvicorn
from config.config import file_path
from pdf.pdf_handling import extract_text_from_pdf
from resume.resume_improve import improve_resume
from resume.resume_summarize import summarize_resume
from resume.resume_score import score_resume
from resume.resume_compare import compare_resume
from resume.text_to_json import convert_to_json

app = FastAPI()

#------------------------------------------------#

@app.get('/')
def index():
    return {'msg': 'Resume-Help App'}

#------------------------------------------------#

@app.get('/view')
def view():
    res_text = extract_text_from_pdf(file_path)
    view = improve_resume(res_text)
    view = convert_to_json(view)
    return {"view": view}

#------------------------------------------------#

@app.get('/summarize')
def summary():
    res_text = extract_text_from_pdf(file_path)
    summary = summarize_resume(res_text)
    return {"summary": summary}

#------------------------------------------------#

@app.post('/score')
async def score_compare(request: Request):
     response = await request.json()
     job_description = response["jd"]
     role = response["role"]
     res_text = extract_text_from_pdf(file_path)
     score = score_resume(res_text, job_description, role)
     imp = compare_resume(res_text, job_description, role)
     imp = convert_to_json(imp)
     return {
          "score":score,
          "improvements":imp
     }

#------------------------------------------------#

if __name__ == '__main__':
	uvicorn.run(app, host='0.0.0.0', port=5000)