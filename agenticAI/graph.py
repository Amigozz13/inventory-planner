from agenticAI.state import state
from langgraph.graph import StateGraph,START,END
from agent.demand_agent import demand_agent
from agent.inventory_agent import inventory_agent
from agent.rag_agent import rag_agent
from agent.recommendation import recommentated_agent
from agent.risk_agent import risk_analysis
builder=StateGraph(state)
builder.add_node('inventory_agent',inventory_agent)
builder.add_node('demand_agent',demand_agent)
builder.add_node('risk_analysis',risk_analysis)
builder.add_node('rag_agent',rag_agent)
builder.add_node('recommendation',recommentated_agent)
builder.add_edge(START,'inventory')
builder.add_edge('inventory','demand_agent')
builder.add_edge('demand_agent','risk_analysis')
builder.add_edge('risk_analysis','rag_agent')
builder.add_edge('rag_agent','recommendation')
builder.add_edge('recommendation',END)
graph=builder.compile()

 