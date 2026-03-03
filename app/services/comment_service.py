from app.repositories.comment_repository import CommentRepository
from app.schemas.comment import CommentCreate

class CommentService():
    def __init__(self, repository: CommentRepository):
        self.repository = repository
        
    def create(self, data: CommentCreate):
        return self.repository.create(data)
    
    def list_comments(self):
        return self.repository.get_all()
    
    def get_comment_by_id(self, id: int):
        return self.repository.find_by_id(id)
    
    def delete_comment_by_id(self, id: int):
        self.repository.delete_by_id(id)