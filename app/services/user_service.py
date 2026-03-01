from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate

class UserService():
    def __init__(self, repository: UserRepository):
        self.repository = repository
        
    def create_user(self, data: UserCreate):
        return self.repository.create_user(data)
        
    def get_all(self):
        return self.repository.get_all()
    
    def get_by_id(self, id: int):
        user = self.repository.get_by_id(id)
        if not user:
            return None
        else: 
            return user
        
    def delete_by_id(self, id: int):
        self.repository.delete_user(id)
        