from state import State
from config import llm
def recommendation_agent(state:State):
    inventory=state['inventory']
    demand=state['demand']
    risk=state['risk']
    policy=state['policy']
    prompt=f"""
    You Are At Autonomus Inventory Replenishment Agent
    product name:{inventory['product_name']}
    current stock:{inventory['current_stock']}
    quantity sold:{inventory['quantity_sold']}
    estimated demand:{demand['estimated_demand']}
    risk level:{risk}
    company policies:{policy}
    Based in the above information whether retailers wants to reorder the product
    Mention:
    1.stock states
    2.Risk level
    3.Recommentated
    4.Reason
    """
    response=llm.invoke(prompt)
    state['recommentated']=response.content
    return state

    