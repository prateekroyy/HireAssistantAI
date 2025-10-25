from models.flowstate import flowstate

def format_email(state: flowstate) -> dict:
    
    resume_data = state["parsed_resume"]


    
    email_content = state["email"]


    final_obj = {
        "recipient": resume_data["email"],
        "subject": email_content["subject"],
        "body": email_content["body"]
    }

    return {"output": final_obj}
