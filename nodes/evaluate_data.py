from langchain_groq import ChatGroq
from models.structures import structuredevaluation
from models.flowstate import flowState
from dotenv import load_dotenv
load_dotenv()

model = ChatGroq(model="llama-3.3-70b-versatile")
structured_model = model.with_structured_output(structuredevaluation)

def evaluatedata(state=flowState) -> dict:
    prompt = f"Analyze the following JSON data and segregate and return the needed output \n {state['scrappeddata']}"
    evaluated_data = structured_model.invoke(prompt)
    return {'evaluateddata': evaluated_data.model_dump()}
