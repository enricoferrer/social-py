from typing import List

from pydantic import BaseModel, EmailStr
from app.schemas.post import PostResponse

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    senha: str
    
class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    posts: List[PostResponse]
    
    model_config = {'from_attributes': True}