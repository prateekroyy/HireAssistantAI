from langchain_groq import ChatGroq
from langchain_community.document_loaders import PyPDFLoader
from models.structures import structuredevaluation
from models.flowstate import flowState
from dotenv import load_dotenv
import json
load_dotenv()




def file_to_data(state: flowState) -> json:
    pdf_path = state.get("pdf_path")
    model = ChatGroq(model="llama-3.3-70b-versatile")
    structured_model = model.with_structured_output(structuredevaluation)
    loader = PyPDFLoader(pdf_path)
    docs = loader.load()  # returns a list of Document objects
    text = "\n".join([doc.page_content for doc in docs])
    prompt = f'Extract the following fields from this resume text into JSON: name, company, role, experience_years in integer, email.\n{text}'
    data = structured_model.invoke(prompt)
    return {'scrappeddata':data.model_dump_json()}