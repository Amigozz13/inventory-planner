from state import State

def rag_agent(state: State):

    if state.get("error"):
        return state

    inventory = state.get("inventory", {})

    product = inventory.get("product_name", "Unknown Product")

    policy = (
        f"Maintain safety stock for {product}. "
        f"Reorder before inventory reaches the average demand during lead time."
    )

    # Store global policy
    state["policy"] = policy

    # Store in latest inventory
    inventory["policy"] = policy

    # Store in every historical record
    if state.get("all_dates_inventory"):
        for item in state["all_dates_inventory"]:
            item["policy"] = policy

    return state