# from fastapi import FastAPI
# from enum import Enum


# app = FastAPI()

# class CarType(str,Enum):
#     sedan = "sedan"
#     suv = "suv"
#     truck = "truck"

# messageType ={
#     CarType.sedan:"A sleek and stylish car.",
#     CarType.suv: "A spacious and powerful vehicle.",
#     CarType.truck:"A heavy-duty workhorse.",
# }

# @app.get("/cars/{car_type}")
# def getCarType(car_type:CarType):
#     return{
#         "car_type":car_type,
#         "message":messageType[car_type]
#         }



#PATH FILE
from fastapi import FastAPI
from enum import Enum
app = FastAPI()


@app.get("/storage/{item_path:path}")
def storage_path(item_path:str):
    if(item_path.endswith("/")):
        return {
            "path":item_path,
            "type":"Folder"
        }
    else:
        return {
            "path":item_path,
            "type":"File"
        }




















