from pydantic import BaseModel
from app.schemas.user import UserSummary

class CommentCreate(BaseModel):
    comment: str
    user_id: int
    post_id: int
    
class CommentsResponse(BaseModel):
    comment: str
    author: UserSummary
    post_id: int
    
    model_config = {'from_attributes': True}