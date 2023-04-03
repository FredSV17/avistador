from fastapi import APIRouter
from fastapi import Body
from fastapi.responses import JSONResponse
from fastapi import Body, status
from webscraper.webscraping_amazon import start_webscraping

router = APIRouter()

@router.get("/hello",summary="Hello, start scraping!")
def hello_from_product():
    return "Hello from from product!"


# @router.post("/insert",summary="Animal name insert",response_model=AnimalModel)
# async def insert_animal(animal: AnimalModel = Body(...)):
#     new_animal = await insert_one(animal)
#     created_animal = await find_one(new_animal.inserted_id)
#     return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_animal)


@router.post("/get/{product_name}",summary="Amazon product name webscraping")
async def webscrape_amazon_product(product_name: str):
    # drop_collection()
    await start_webscraping(product_name=product_name,number=20)
    return JSONResponse(status_code=status.HTTP_200_OK, content="")