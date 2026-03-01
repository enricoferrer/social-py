from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse


class UserRepository:
    def __init__(self, db: Session):
        self.db = db
        
    def get_all(self):
        return self.db.query(User).all()
    
    def get_by_id(self, id: int):
        return self.db.query(User).filter_by(User.id == id).first()
    
    def create_user(self, data: UserCreate):
        user = User(**data.model_dump())
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
    
    def delete_user(self, id: int):
        user = self.get_by_id(id)
        self.db.delete(user)
        self.db.commit()