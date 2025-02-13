# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/greet/{name}")
# def greet(name:str):
#     return {"Hello, {name}"}

# @app.post("/create-item")
# def create_item(item: dict):
#     return {"massage": f"Item {item['name']} with price {item['price']} was created!"}



# # SOAL NO 2
# from fastapi import FastAPI

# app = FastAPI()

# @app.put("/update-item/{item-id}")
# async def update_item(item_id : int):
#     return {"massage" : f"item {item['item_id']} updated with name{item['name']} and price {item['price']}"}

# @app.delete("/delete-item/{item_id}")
# async def delete_item(item_id:int):
#     return {"massage": f"item {item_id} deleted"}



# # SOAL NO 3
# import asyncio
# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/delayed-data")
# async def delayed():
#     asyncio.sleep(3)
#     return {"data": f"this data delayed"}


# SOAL NO 4

# from fastapi import FastAPI,HTTPException

# app = FastAPI()

# @app.get("/user/{user_id}")
# def getUserId(user_id: int):
#     if(user_id<1):
#         raise HTTPException(status_code=400,detail="User ID must be greater than 0")
#     else:
#         raise HTTPException(status_code=400, detail="User not found")
    
#     return {"message":{
#         "user_id : {user_id}",
#         "name": "User 5"
#     }}

# @app.get("/user/me")
# def getMe():
#     return {"message":{
#   "user_id": "current",
#   "name": "Logged-in User"
# }
# }


















