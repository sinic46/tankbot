from fastapi import FastAPI

app = FastAPI()




@app.get("/")
def read_root():
    return{"message":"The tank will see you now."}



@app.post("/direction/{x}/{y}")
def movement_direction(x:int,y:int):
    return{"message":f"the x axis is {x} and the y axis is {y}"}


