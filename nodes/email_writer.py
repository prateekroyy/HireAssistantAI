from langchain_groq import ChatGroq
from models.structures import emailstructure
from models.flowstate import flowState
from dotenv import load_dotenv
load_dotenv()

model = ChatGroq(model="llama-3.3-70b-versatile")
structured_emailwriter = model.with_structured_output(emailstructure)

def writer(state=flowState) -> dict:
    evaluateddata = state['evaluateddata']
    prompt = f"""
You are a professional email writer at "Techmax India PVT. LTD". Generate a personalized interview invitation email in your company for a person based on the following information:

- Name: {evaluateddata['name']}
- Email: {evaluateddata['email']}
- Company the person is currently working at: {evaluateddata['company']}
- Role: {evaluateddata['role']}
- Years of Experience: {evaluateddata['experience_years']}

Requirements:
1. Use a polite, professional, and friendly tone.
2. Address the person by name.
3. Mention their current role, company, and experience to make the email personalized.
4. Clearly state that the purpose of the email is to invite them for an interview.
5. Include details about the interview (time, date, mode, or mention that these can be scheduled).
6. Encourage them to respond to confirm or suggest an alternative.
7. End with a professional closing and your name/contact information.

Structure to follow:
- Greeting using their name
- Acknowledge their experience and current role
- Invitation to interview with scheduling details
- Call-to-action for confirmation
- Closing
"""
    email = structured_emailwriter.invoke(prompt)
    return {'email': email.model_dump()}
