from typing import List

from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.comment import CommentCreate, CommentsResponse
from app.repositories.comment_repository import CommentRepository
from app.services.comment_service import CommentService
from fastapi import Depends, APIRouter

router = APIRouter(prefix="/comments", tags=["Comments"])

def get_service(db: Session = Depends(get_db)):
    return CommentService(CommentRepository(db))

@router.post("/", response_model=CommentsResponse, status_code=201)
def create_comment(data: CommentCreate, service: CommentService = Depends(get_service)):
    return service.create(data)

@router.get("/", response_model=List[CommentsResponse])
def list_comments(service: CommentService = Depends(get_service)):
    return service.list_comments()

@router.get("/{id}", response_model=CommentsResponse)
def get_comment_by_id(id: int, service: CommentService = Depends(get_service)):
    return service.get_comment_by_id(id)

@router.delete("/{id}", status_code=204)
def delete_comment_by_id(id: int, service: CommentService = Depends(get_service)):
    service.delete_comment_by_id(id)