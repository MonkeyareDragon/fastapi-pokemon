from pydantic import BaseModel

class Pokemon(BaseModel):
    name: str
    image: str
    type: str
    
    class Config:
        from_attributes = True