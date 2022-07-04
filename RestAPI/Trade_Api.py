from database import Trade, TradeDetails, inventory
from fastapi import FastAPI, Path

app = FastAPI()

@app.post("/add-details/{trade_id}")
def add_details(trade_id: int, trade: Trade):
   if trade_id in inventory.keys():
       return {"Error": "Trade ID is already exixts"}
   inventory[trade_id] = trade
   return inventory[trade_id]

@app.get("/get-details/{trade_id}")
def get_details(trade_id: int = Path(None, description="The ID of Trade you'd like to view")):
    if trade_id not in inventory.keys():
        return {"Error": "Trade ID is not exists"}
    return inventory[trade_id]

@app.get("/get-trades")
def get_trades():
    return inventory
