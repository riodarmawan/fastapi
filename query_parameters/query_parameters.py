# from fastapi import FastAPI


# app = FastAPI()

# products_db = [
#     {"id": 1, "name": "Laptop", "category": "elektronik", "price": 800.0, "available": True},
#     {"id": 2, "name": "Kemeja", "category": "pakaian", "price": 50.0, "available": False},
#     {"id": 3, "name": "Mouse", "category": "elektronik", "price": 25.0, "available": True},
#     {"id": 4, "name": "Buku", "category": "lainnya", "price": 15.0, "available": True}
# ]


# @app.get("/products/")
# async def get_products(category: str = "all",min_price:int =0.0,available: bool =True):
        
#     return {
#   "filters": {
#     "category": category,
#     "min_price": min_price,
#     "available": available
#   },
#   "results": [
#     product for product in products_db 
#     if product["price"] <= min_price 
#     and (product["category"] == category or category == "all")
#     and product["available"] == available
# ]
# }



# from fastapi import FastAPI


# app = FastAPI()


# books_db = [
#     {"id": 1, "title": "Dunia Sophie", "author": "Jostein Gaarder", "year": 1991, "genre": "fiksi"},
#     {"id": 2, "title": "Sapiens", "author": "Yuval Noah Harari", "year": 2011, "genre": "non-fiksi"},
#     {"id": 3, "title": "The Martian", "author": "Andy Weir", "year": 2011, "genre": "sains"},
#     {"id": 4, "title": "1984", "author": "George Orwell", "year": 1949, "genre": "fiksi"}
# ]



# @app.get("/library/books")
# def library(author:str | None = None ,year:int | None = None,genre:str | None = None):
    
#     books=[]
#     for book in books_db:
#         if(
#             (author == book["author"] or author is None)
#            and (year == book["year"] or year is None) and
#            (genre == book["genre"] or genre is None)
#            ):
#             books.append(book)
            


    
#     return {
#           "filters_applied": {
#             "author": author,
#             "year": year,
#             "genre": genre
#         },
#         "books": books
#     }
 

# from fastapi import FastAPI


# app = FastAPI()

# products_db = [
#     {
#         "id": 1,
#         "name": "Laptop Gaming",
#         "price": 1500.0,
#         "description": "Laptop dengan GPU high-end",
#         "stock": 10
#     },
#     {
#         "id": 2,
#         "name": "Mouse Wireless",
#         "price": 50.0,
#         "description": "Mouse ergonomis 2400 DPI",
#         "stock": 25
#     }
# ]

# @app.get("/products/{product_id}")
# def get_detail_product(product_id:int,detailed:bool | None = False):

#     detail = []

#     for product in products_db:
#         if(product_id == product["id"] and detailed == True):
#             detail.append(product)
#         elif(product_id == product["id"] and detailed == False):
#             product.pop("description")
#             product.pop("stock")

#             detail.append(product)

#     return {"result": detail}


from fastapi import FastAPI


app = FastAPI()


library_db = [
    {
        "user_id": 123,
        "book_id": "A1B2C3",
        "book_title": "Dunia Sophie",
        "description": "Sebuah novel filsafat yang mengajak pembaca menjelajahi sejarah pemikiran Barat.",
        "due_date": "2023-12-31"
    },
    {
        "user_id": 456,
        "book_id": "X7Y8Z9",
        "book_title": "Sapiens",
        "description": "Buku tentang sejarah manusia dari Zaman Batu hingga revolusi teknologi.",
        "due_date": "2024-01-15"
    }
]

@app.get("/library/users/{user_id}/books/{book_id}")
async def get_book(user_id:int, book_id:str, show_due_date:bool | None=False,limit:int | None=None):
    
        for book in library_db:
            if (user_id == book["user_id"] and book_id == book["book_id"]):

                result = {
                        "user_id": book["user_id"],
                        "book_id": book["book_id"],
                        "book_title": book["book_title"],                    
                }
                if(show_due_date == True):
                    result["due_date"] = book["due_date"]
                if(limit is not None):
                    result["description"] = book["description"][0:limit]

                return result
        
        return {"error": "Book not found"}
                                 
















