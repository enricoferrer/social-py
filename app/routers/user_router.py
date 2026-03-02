from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session 
from app.repositories.user_repository import UserRepository
from app.services.user_service import UserService
from app.core.database import get_db
from app.schemas.user import UserCreate, UserResponse

router = APIRouter(prefix="/users", tags=["Users"])

def get_service(db: Session = Depends(get_db)):
    return UserService(UserRepository(db))

@router.post("/", response_model=UserResponse, status_code=201)
def create_user(data: UserCreate, service: UserService = Depends(get_service)):
    return service.create_user(data)

@router.get("/", response_model=List[UserResponse], status_code=200)
def list_users(service: UserService = Depends(get_service)):
    return service.get_all()

@router.get("/{id}", response_model=UserResponse, status_code=200)
def get_user_by_id(id: int, service: UserService = Depends(get_service)):
    return service.get_by_id(id)

@router.delete("/{id}", status_code=204)
def delete_user_by_id(id: int, service:UserService = Depends(get_service)):
    service.delete_by_id(id)