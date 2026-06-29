from agenticAI.graph import graph
from agenticAI.state import state
state=None
while True:
    user_input=input('Ask more about related information')
    if user_input.lower().strip() in{'quit','bye','exit'}:
        print('Existing Browser')
        break
    state={
        'message':[user_input],
        'inventory':dict,
        'demand':dict,
        'risk':str,
        'policy':str,
        'recommentated':str       
    }
    result=graph.invoke(state)
    print('')