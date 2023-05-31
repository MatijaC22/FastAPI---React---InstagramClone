import os
from fastapi import APIRouter, Depends, Form, status, UploadFile, File
from routers.schemas import PostBase, PostDisplay
from sqlalchemy.orm.session import Session
from db.database import get_db
from db import db_post
from typing import List, Optional
from auth.oauth2 import get_current_user


router = APIRouter(
    prefix = '/post',
    tags = ['post']
)

@router.get('/all', response_model=List[PostDisplay])
def posts(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
   return db_post.get_all(db, current_user)

@router.get('/package', response_model=List[PostDisplay])
def posts(page: int = 1, per_page: int = 10, user_id: Optional[int] = None, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
   return db_post.get_all_package(db, current_user, user_id, page, per_page)

@router.post("/create")
def submit_form(
   images: List[UploadFile] = File(...), 
   reference: str = Form(...), 
   description: str = Form(...), 
   db: Session = Depends(get_db), 
   current_user = Depends(get_current_user)
   ):
    return db_post.create(db, images, reference, description, current_user)
   
####################################################################################################################
@router.get('/{id}', response_model = PostDisplay)
def post(id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
   return db_post.get_one(db, id, current_user)


@router.post('/update/{id}', response_model = PostDisplay)
def update_container(id:int, request: PostDisplay, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return db_post.update_post(db, id, current_user, request)


@router.post('/delete/{id}')
def delete(id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
   return db_post.delete(db, id, current_user.id)


