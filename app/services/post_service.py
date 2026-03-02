from app.repositories.post_repository import PostRepository
from app.schemas.post import PostCreate

class PostService():
    def __init__(self, repository: PostRepository):
        self.repository = repository
        
    def create(self, data: PostCreate):
        return self.repository.create(data)
    
    def get_all_post(self):
        return self.repository.get_all()
    
    def get_post_by_id(self, id: int):
        return self.repository.get_by_id(id)