from typing import TypedDict
import json

class flowState(TypedDict):
    scrappeddata: json
    evaluateddata: dict
    email: dict
    final_email: dict
