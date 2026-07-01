from graph import graph
while True:
    user_input = input("Ask More details about product: ")
    if user_input.lower().strip() in {"quit", "bye", "exit"}:
        print("Exiting browser")
        break
    state = {
        "message": [user_input],
        "inventory": {},
        "all_dates_inventory": [],
        "demand": {},
        "risk": "",
        "policy": "",
        "recommendation": "",
        "error": ""
    }
    result = graph.invoke(state)
    if result.get("error"):
        print("\nERROR:", result["error"])
    else:
        print("\nAI Inventory Recommendation\n")
        print(result.get("recommendation", "No output generated"))