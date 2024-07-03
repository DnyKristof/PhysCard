from fastapi import FastAPI
from physcard_backend.cardService import CardService

app=FastAPI()
card_service = CardService()

@app.get("/")
def test():
    return {"message":"Hello World"}

@app.get("/cards")
def get_all_cards():
    return card_service.get_all_cards()
 
@app.post("/cards")
def create_card(card: dict):
    result=card_service.create_card(card)
    return {"id":str(result)} 

if __name__=="__main__":
    import uvicorn
    uvicorn.run("app:app",reload= True,host="0.0.0.0")

