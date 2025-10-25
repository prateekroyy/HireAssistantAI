from langchain_groq import ChatGroq
from langchain_community.document_loaders import PyPDFLoader
from models.structures import resumestructure
from models.flowstate import flowstate



def resume_parser(state: flowstate) -> dict:
    from dotenv import load_dotenv
    load_dotenv()

    model = ChatGroq(model="llama-3.3-70b-versatile")
    resume_structured_model = model.with_structured_output(resumestructure)
    pdf_resume = state['pdf_resume']
    loader = PyPDFLoader(pdf_resume)
    docs = loader.load()  # returns a list of Document objects
    text = "\n".join([doc.page_content for doc in docs])
    prompt = f'Extract the following fields from this resume text into JSON: name, company, role, experience_years in integer, email.\n{text}'
    data = resume_structured_model.invoke(prompt)
    return {'parsed_resume':data.model_dump()}