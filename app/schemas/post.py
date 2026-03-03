from typing import List
from app.schemas.comment import CommentsResponse
from pydantic import BaseModel
from app.schemas.user import UserSummary

class PostCreate(BaseModel):
    titulo: str
    descricao: str
    user_id: int
    
class PostResponse(BaseModel):
    titulo: str
    descricao: str
    author: UserSummary
    comments: List[CommentsResponse]
    
    model_config= {'from_attributes': True}