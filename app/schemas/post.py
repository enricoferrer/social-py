from pydantic import BaseModel

class PostCreate(BaseModel):
    titulo: str
    descricao: str
    user_id: int
    
class PostResponse(BaseModel):
    titulo: str
    descricao: str
    user_id: int
    
    model_config= {'from_attributes': True}