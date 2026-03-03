from pydantic import BaseModel

class CommentCreate(BaseModel):
    comment: str
    user_id: int
    post_id: int
    
class CommentsResponse(BaseModel):
    comment: str
    user_id: int
    post_id: int
    
    model_config = {'from_attributes': True}