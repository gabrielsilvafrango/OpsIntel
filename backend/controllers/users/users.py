from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models.users import User
from controllers.users.dto import UserCreate

router = APIRouter(prefix="/users")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(name=user.name)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
