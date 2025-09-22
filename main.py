from langgraph.graph import StateGraph, START, END
from models.flowstate import flowState
from nodes.evaluate_data import evaluatedata
from nodes.email_writer import writer
from nodes.format_email import format_email
import json

# Load example JSON
with open("data/example.json", "r") as f:
    example = json.load(f)

# Build workflow
graph = StateGraph(flowState)
graph.add_node('evaluate_data', evaluatedata)
graph.add_node('email_writer', writer)
graph.add_node('final_format', format_email)

graph.add_edge(START, 'evaluate_data')
graph.add_edge('evaluate_data', 'email_writer')
graph.add_edge('email_writer', 'final_format')
graph.add_edge('final_format', END)

workflow = graph.compile()

# Run workflow
initial_state = {'scrappeddata': example}
final_state = workflow.invoke(initial_state)

# Access final email
print(final_state['final_email'])
