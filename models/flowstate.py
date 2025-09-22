from typing import TypedDict
import json

class flowState(TypedDict):
    pdf_path: str
    scrappeddata: json
    evaluateddata: dict
    email: dict
    final_email: dict
