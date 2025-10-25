from langgraph.graph import StateGraph, START, END
from models.flowstate import flowstate
from workflows.resume_workflow import resumeworkflow
from workflows.jd_workflow  import jdworkflow
from nodes.email_writer import email_writer
from nodes.format_output import format_email
from dotenv import load_dotenv

load_dotenv()

# Build workflow  
graph = StateGraph(flowstate)
graph.add_node("resume_parser", resumeworkflow)
graph.add_node("jd_parser", jdworkflow)
graph.add_node("email_writer", email_writer)
graph.add_node("final_output", format_email)

graph.add_edge(START, "resume_parser")
graph.add_edge("resume_parser", "jd_parser")
graph.add_edge("jd_parser", "email_writer")
graph.add_edge("email_writer", "final_output")
graph.add_edge("final_output", END)



workflow = graph.compile()

initial_state = {
    'pdf_resume': "D:/HireAssistantAI/data/test_resume.pdf",
    "pdf_jd": "D:/HireAssistantAI/data/demo_job_description.pdf"
}
result = workflow.invoke(initial_state)
print(result["output"])

