import os
import sys
project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)
if project_root not in sys.path:
    sys.path.insert(0, project_root)   
from state import State
from  rag_policy.search import search_policy
def rag_agent(state:State):
    if state.get('error'):
        return state
    inventory=state.get('inventory',{})
    product=inventory.get('product_name','unknown product')
    risk=state.get('risk','low')
    query=f"what is the comany policy for {product} when inventory risk is {risk}"
    policy=search_policy(query)
    state['policy']=policy
    if state.get('all_dates_inventory'):
        for items in state['all_dates_inventory']:
            items['policy']=policy
    return state
