from langchain_groq import ChatGroq
from models.structures import emailstructure
from models.flowstate import flowState
from dotenv import load_dotenv
load_dotenv()

model = ChatGroq(model="llama-3.3-70b-versatile")
structured_emailwriter = model.with_structured_output(emailstructure)

def writer(state=flowState) -> dict:
    prompt = f"Wrtie an email to invite the following person to an interview on 22 September 2025, at 10 AM within 200 words \n {state['evaluateddata']}"
    email = structured_emailwriter.invoke(prompt)
    return {'email': email.model_dump()}
