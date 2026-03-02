from sqlalchemy.orm import Session
from app.models.post import Post
from app.schemas.post import PostCreate

class PostRepository:
    def __init__(self, db: Session):
        self.db = db
        
    def get_all(self):
        return self.db.query(Post).all()
    
    def get_by_id(self, id: int):
        return self.db.query(Post).filter(Post.id == id).first()
    
    def create(self, data: PostCreate):
        post = Post(**data.model_dump())
        self.db.add(post)
        self.db.commit()
        self.db.refresh(post)
        return post