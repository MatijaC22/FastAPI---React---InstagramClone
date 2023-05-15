from sqlalchemy.orm.session import Session
from db.database import get_db
from fastapi import APIRouter, Depends
from routers.schemas import ContainerDisplay, ContainerBase
from db import db_container
from typing import List
from auth.oauth2 import get_current_user


router = APIRouter(
    prefix = '/container',
    tags = ['container']
)


@router.post('/', response_model = ContainerDisplay)
def create_container(request: ContainerBase, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
  return db_container.create_container(db, current_user.administrator, request)

@router.get('/all', response_model=List[ContainerDisplay])
def get_all_containers(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
   return db_container.get_all_containers(db, current_user.administrator)

@router.get('/{id}', response_model=ContainerDisplay)
def get_container(id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
   return db_container.get_container_by_id(db, id, current_user)

@router.post('/update/{id}', response_model = ContainerDisplay)
def update_container(id:int, request: ContainerBase, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return db_container.update_user(db, id, current_user.administrator, request)

@router.post('/delete/{id}')
def delete(id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
   return db_container.delete(db, id, current_user.administrator)
