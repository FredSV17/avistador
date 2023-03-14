from api.api_models.product import ProductModel
from db.db_manager import db
from fastapi.encoders import jsonable_encoder

async def insert_one(product: ProductModel):
    product_json_encoder = jsonable_encoder(product)
    new_product = db["product"].insert_one(product_json_encoder)
    return new_product


# async def find_one(id: str):    
#     found_animal = db["animal"].find_one({"_id": id})
#     return found_animal

# async def get_random_one():    
#     cursor = db["animal"].aggregate([{ "$sample": { "size": 1 } }]).next()
#     animal = cursor['name']
#     return animal


def drop_collection():
    db["product"].drop()