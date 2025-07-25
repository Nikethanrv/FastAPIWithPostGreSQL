from pydantic import BaseModel
# For data validation while performing CRUD operations

class ItemBase(BaseModel):
    name: str
    description: str

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    model_config = {
        "from_attributes": True
    }