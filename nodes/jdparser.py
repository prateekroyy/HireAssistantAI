from langchain_groq import ChatGroq
from langchain_community.document_loaders import PyPDFLoader
from models.structures import jdstructure
from models.flowstate import flowstate
from dotenv import load_dotenv
import json
load_dotenv()


model = ChatGroq(model="llama-3.3-70b-versatile")
jd_structure_model = model.with_structured_output(jdstructure)

def jd_parser(state: flowstate)-> dict:
    pdf_jd = state['pdf_jd']
    loader = PyPDFLoader(pdf_jd)
    docs = loader.load()
    text = '\n'.join([doc.page_content for doc in docs])
    prompt = f"""
    Extract the following fields from this Job Description into JSON:
    job_title, company, location, experience_required, skills_required, education, employment_type, salary_range.
    
    Job Description:
    {text}
    """

    jd = jd_structure_model.invoke(prompt)
    return {'parsed_jd':jd.model_dump()}