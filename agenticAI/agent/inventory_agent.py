from state import State
from backend.app.database import get_connection
from datetime import datetime, timedelta
def inventory_agent(state: State):

    product_name = state["message"][-1].content.lower().strip()
    conn = get_connection()
    query = """
    SELECT
        p.product_name,
        i.date,
        i.current_stock,
        s.quantity_sold,
        p.supplier_id,
        p.avg_lead_time_day,
        p.cost_price,
        p.base_price,
        s.customer_rating,
        i.expiry_date
    FROM products p
    JOIN inventory_daily i
        ON p.product_id = i.product_id
    JOIN sales s
        ON p.product_id = s.product_id
       AND i.date = s.date
    WHERE LOWER(p.product_name) = LOWER(?)
    ORDER BY i.date
    """
    rows = conn.execute(query, (product_name,)).fetchall()
    conn.close()
    if not rows:
        state["error"] = f"Product '{product_name}' not found."
        return state
    inventory_history = []
    for row in rows:
        inventory_history.append({
            "date": row["date"],
            "product_name": row["product_name"],
            "current_stock": int(row["current_stock"]),
            "quantity_sold": int(row["quantity_sold"]),
            "supplier_id": row["supplier_id"],
            "lead_time": int(row["avg_lead_time_day"]),
            "cost_price": float(row["cost_price"]),
            "base_price": float(row["base_price"]),
            "customer_rating": float(row["customer_rating"]),
            "expiry_date": row["expiry_date"]
        })
    state["all_dates_inventory"] = inventory_history
    latest = inventory_history[-1]
    state["inventory"] = latest
    latest_date = datetime.strptime(latest["date"], "%Y-%m-%d")
    predicted_stock = max(0, latest["current_stock"] - latest["quantity_sold"])
    state["next_day_inventory"] = {
        "date": (latest_date + timedelta(days=1)).strftime("%Y-%m-%d"),
        "current_stock": predicted_stock,
        "quantity_sold": latest["quantity_sold"]
    }
    return state