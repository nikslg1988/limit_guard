from pydantic import BaseModel

class LimitCreate(BaseModel):
    user_id: str
    category_id: str
    amount: float

class LimitResponse(BaseModel):
    id: str
    user_id: str
    category_id: str
    amount:float
    
    model_config = {
        "from_attributes": True
    }

class LimitUpdate(BaseModel):
    id: str
    amount: float