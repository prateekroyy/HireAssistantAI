from models.structures import final_email
from models.flowstate import flowState

def format_email(state: flowState) -> dict:
    
    evaluateddata = state["evaluateddata"]
    email_content = state["email"]

    
    final_obj = final_email(
        recipient=evaluateddata["email"],
        subject=email_content["subject"],
        body=email_content["body"]
    )

    return {"final_email": final_obj.model_dump()}