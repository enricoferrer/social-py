from pydantic import BaseModel
from app.schemas.user import UserSummary
from datetime import datetime

class CommentCreate(BaseModel):
    comment: str
    user_id: int
    post_id: int
    
class CommentsResponse(BaseModel):
    comment: str
    author: UserSummary
    commented_at: datetime 
    post_id: int
    
    model_config = {'from_attributes': True}