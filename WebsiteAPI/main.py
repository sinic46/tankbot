from fastapi import FastAPI
from decimal import Decimal

app = FastAPI()




@app.get("/")
def read_root():
    return{"message":"The tank will see you now."}



@app.post("/direction/{x}/{y}")
def movement_direction(x:Decimal,y:Decimal):
    return{"message":f"the x axis is {x} and the y axis is {y}"}


