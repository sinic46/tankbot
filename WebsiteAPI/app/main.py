from fastapi import FastAPI
import logging

logger = logging.getLogger(__name__)

app = FastAPI()


@app.get("/")
def read_root():
    logger.info(f"request / endpoint!")
    return{"message":"The tank will see you now."}



@app.post("/direction/{x}/{y}")
def movement_direction(x:int,y:int):
    logger.info(f"requested[/direction/{x}/{y}]")

    return{"message":f"the x axis is {x} and the y axis is {y}"}


