from typing import TypedDict, Annotated, List
from models.structures import jdstructure, resumestructure, outputstructure, emailstructure

class flowstate(TypedDict):
    pdf_resume: Annotated[List[str], "input"]
    pdf_jd: Annotated[List[str], "input"]
    parsed_jd : jdstructure
    parsed_resume: resumestructure
    email: str
    output : outputstructure

