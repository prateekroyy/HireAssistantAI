from langchain_groq import ChatGroq
from models.structures import emailstructure
from models.flowstate import flowstate
from dotenv import load_dotenv
load_dotenv()

model = ChatGroq(model="llama-3.3-70b-versatile")
structured_emailwriter = model.with_structured_output(emailstructure)

def email_writer(state: flowstate) -> dict:
    # Convert Pydantic models to dicts
    resume = state["parsed_resume"]
    if hasattr(resume, "model_dump"):
        resume = resume.model_dump()
    
    jd = state["parsed_jd"]
    if hasattr(jd, "model_dump"):
        jd = jd.model_dump()

    prompt = f"""
You are an HR assistant generating a professional interview invitation email.

Candidate Information:
- Name: {resume['name']}
- Current Company: {resume['company']}
- Current Role: {resume['role']}
- Experience: {resume['experience_years']} years

Job Information:
- Job Title: {jd.get('job_title')}
- Company: {jd.get('company')}
- Location: {jd.get('location')}
- Required Experience: {jd.get('experience_required')}
- Required Skills: {', '.join(jd.get('skills_required', []))}
- Education: {jd.get('education', 'Not specified')}
- Employment Type: {jd.get('employment_type', 'Not specified')}
- Salary Range: {jd.get('salary_range', 'Not specified')}

Instructions:
1. Write a polite and professional email inviting the candidate for an interview.
2. Include the candidate’s name in the greeting.
3. Mention the job title and company in the email body.
4. Suggest possible next steps (e.g., interview schedule or contact for coordination).
5. Keep the email concise and friendly.

Output the email in JSON format with fields:
- subject
- body
"""
    email_output = structured_emailwriter.invoke(prompt)

    # Must return this exact key
    return {"email": email_output.model_dump()}
