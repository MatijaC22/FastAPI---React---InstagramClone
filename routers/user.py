from sqlalchemy.orm.session import Session
from db.database import get_db, SessionLocal
from fastapi import APIRouter, Depends, UploadFile, File, Form
from routers.schemas import UserDisplay, UserBase, UserUpdateBase
from db import db_user
from typing import List, Optional
from auth.oauth2 import get_current_user


router = APIRouter(
    prefix = '/user',
    tags = ['user']
)

# Register the event function with the FastAPI app
@router.on_event('startup')
def startup_event():
    with SessionLocal() as db:
        return db_user.create_initial_user(db)

# @router.post('/', response_model = UserDisplay)
# def create_user(request: UserBase, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
#   return db_user.create_user(db, current_user.administrator, request)

@router.post("/create")
def submit_form(
   password: str = Form(...),
   date_of_birth: str = Form(...),
   image: UploadFile = File(...), 
   active: bool = Form(...), 
   administrator: bool = Form(...),
   email: str = Form(...), 
   name: str = Form(...), 
   middle_name: Optional[str] = Form(None), 
   last_name: str = Form(...), 
   position: str = Form(...), 
   db: Session = Depends(get_db), 
   current_user = Depends(get_current_user)
   ):
    return db_user.create(db, password, date_of_birth, image, active, administrator, email, name, middle_name, last_name, position, current_user)
   

@router.get('/all', response_model=List[UserDisplay])
def get_all_users(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
   return db_user.get_all_users(db, current_user.administrator)

@router.get('/{id}', response_model=UserDisplay)
def get_user(id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
   return db_user.get_user_by_id(db, id, current_user)

@router.post('/update/{id}', response_model = UserUpdateBase)
def update_user(id:int, request: UserBase, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return db_user.update_user(db, id, current_user.administrator, request)

@router.post('/delete/{id}')
def delete(id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
   return db_user.delete(db, id, current_user.administrator)
