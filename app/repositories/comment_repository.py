from sqlalchemy.orm import Session
from app.models.comment import Comment
from app.schemas.comment import CommentCreate

class CommentRepository:
    def __init__(self, db: Session):
        self.db = db
        
    def create(self, data: CommentCreate):
        comment = Comment(**data.model_dump())
        self.db.add(comment)
        self.db.commit()
        self.db.refresh(comment)
        return comment
    
    def get_all(self):
        return self.db.query(Comment).all()
    
    def find_by_id(self, id:int):
        return self.db.query(Comment).filter(Comment.id == id).first()
    
    def delete_by_id(self, id:int):
        comment = self.find_by_id(id)
        self.db.delete(comment)
        self.db.commit()