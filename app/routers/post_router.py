from typing import List
from sqlalchemy.orm import Session

from app.repositories.post_repository import PostRepository
from app.services.post_service import PostService
from app.core.database import get_db
from app.schemas.post import PostCreate, PostResponse
from fastapi import APIRouter, Depends

router = APIRouter(prefix="/posts", tags=["Posts"])

def get_service(db: Session = Depends(get_db)):
    return PostService(PostRepository(db))

@router.post("/",response_model=PostResponse, status_code=201)
def create(data: PostCreate, service: PostService = Depends(get_service)):
    return service.create(data)
    
@router.get("/", response_model=List[PostResponse])
def list_post(service: PostService = Depends(get_service)):
    return service.get_all_post()

@router.get("/{id}", response_model=PostResponse)
def get_post_by_id(id: int, service: PostService = Depends(get_service)):
    return service.get_post_by_id(id)