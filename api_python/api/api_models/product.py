from pydantic import BaseModel, Field
from .py_object_id import PyObjectId
from bson import ObjectId


class ProductModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
    price: float = Field(...)
    general_details: str = Field(...)
    tecnical_details: str = Field(...)
    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "tv",
                "price": 1234.5
            }
        }
