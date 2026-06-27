from state import State
from config import llm
def recommentation(state:State):
    inventory=state['inventory']
    demand=state['demand']
    risk=state['risk']
    policy=state['policy']
    prompt=f"""
    You are at Agentic Replenishment AI
    product name:{inventory['product_name']}
    current stock:{inventory['current_stock']}
    quantity sold:{inventory['estimated_sold']}
    estimated demand:{demand['estimated_demand']}
    risk level:{risk}
    company policies:{policy}
    Based On the information whether retailer will reorder the product
    Mention:
    1.stock states
    2.risk level
    3.recommented 
    4.reason
    """
    response=llm.invoke(prompt)
    state['recommentated']=response.content
    return state

    