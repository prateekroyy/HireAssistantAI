from langgraph.graph import StateGraph, START, END
from models.flowstate import flowstate
from nodes.jdparser import jd_parser

jdgraph = StateGraph(flowstate)
jdgraph.add_node('jd_parser', jd_parser)


jdgraph.add_edge(START, 'jd_parser')
jdgraph.add_edge('jd_parser', END)

jdworkflow = jdgraph.compile()

