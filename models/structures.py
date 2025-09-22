from pydantic import BaseModel, Field

class structuredevaluation(BaseModel):
    name: str = Field(description='Name of the person')
    company: str = Field(description='Name of the company the person is currently working')
    role: str = Field(description='Current position of the person in the company')
    experience_years: int = Field(description='Number of years of experience this person has within the industry')
    email: str = Field(description='Email Id of the person')

class emailstructure(BaseModel):
    subject: str = Field(..., description="Subject line of the email")
    body: str = Field(..., description="Content/body of the email")

class final_email(BaseModel):
    recipient: str = Field(..., description="Email address of the recipient")
    subject: str = Field(..., description="Subject line of the email")
    body: str = Field(..., description="Content/body of the email")
