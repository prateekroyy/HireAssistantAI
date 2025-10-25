from langgraph.graph import StateGraph, START, END
from models.flowstate import flowstate
from nodes.resumeparser import resume_parser

resumegraph = StateGraph(flowstate)
resumegraph.add_node('resume_parser', resume_parser)


resumegraph.add_edge(START, 'resume_parser')
resumegraph.add_edge('resume_parser', END)

resumeworkflow = resumegraph.compile()


