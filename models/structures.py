from pydantic import BaseModel, Field
from typing import List, Optional

class resumestructure(BaseModel):
    name: str = Field(description='Name of the person')
    company: str = Field(description='Name of the company the person is currently working')
    role: str = Field(description='Current position of the person in the company')
    experience_years: int = Field(description='Number of years of experience this person has within the industry')
    email: str = Field(description='Email Id of the person')

class emailstructure(BaseModel):
    subject: str = Field(..., description="Subject line of the email")
    body: str = Field(..., description="Content/body of the email")

class outputstructure(BaseModel):
    recipient: str = Field(..., description="Email address of the recipient")
    subject: str = Field(..., description="Subject line of the email")
    body: str = Field(..., description="Content/body of the email")

class jdstructure(BaseModel):
    job_title: Optional[str] = Field(
        None, description="The official title of the job role, e.g., 'Software Engineer'"
    )
    company: Optional[str] = Field(
        None, description="The name of the company offering the job"
    )
    location: Optional[str] = Field(
        None, description="The primary location of the job, e.g., 'Bangalore, India'"
    )
    experience_required: Optional[str] = Field(
        None, description="Years of experience required for the role, e.g., '3-5 years'"
    )
    skills_required: List[str] = Field(
        default_factory=list,
        description="List of technical and soft skills required, e.g., ['Python', 'Django', 'SQL']"
    )
    education: Optional[str] = Field(
        None, description="The minimum education qualification required, e.g., 'Bachelor’s in Computer Science'"
    )
    employment_type: Optional[str] = Field(
        None, description="Type of employment, e.g., 'Full-time', 'Part-time', 'Contract'"
    )
    salary_range: Optional[str] = Field(
        None, description="The salary range if mentioned, e.g., '10-15 LPA'"
    )