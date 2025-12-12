from pydantic import BaseModel

class TransactionCreate(BaseModel):
    user_id: str
    category_id: str
    amount: float

class TransactionResponse(BaseModel):
    id: str
    user_id: str
    category_id: str
    amount: float
    
    model_config = {
        "from_attributes": True
    }