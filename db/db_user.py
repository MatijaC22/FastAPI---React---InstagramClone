from routers.schemas import UserBase, UserUpdateBase
from sqlalchemy.orm.session import Session 
from db.models import DbUser
from db.hashing import Hash
from fastapi import HTTPException, status, UploadFile, File
import datetime

import shutil


# Event function to create a new user if none exist
def create_initial_user(db: Session):
    user = db.query(DbUser).first()

    if user is None:
        new_user = DbUser(
            email = 'matija@gmail.com',
            password = Hash.bcrypt('matija'),
            administrator = True,
            name = 'matija',
            middle_name = '',
            last_name = 'corak',
            date_of_birth = '07/12/1992',
            position = 'WebDeveloper',
            active = True,
            image_url = '/images/users/matija',
            created_at = datetime.datetime.now(),
            last_modify = datetime.datetime.now(),
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

def create_user(db: Session, current_user:bool, request: UserBase):
    if not current_user:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED,
          detail = f"User don't have authorization!")
    
    user_exist = db.query(DbUser).filter(DbUser.email == request.email).first()
    if user_exist:
        raise HTTPException(status_code = status.HTTP_409_CONFLICT,
          detail = f"Inserted email already exist!")
    
    new_user = DbUser(
        email = request.email,
        password = Hash.bcrypt(request.password),
        administrator = request.administrator,
        name = request.name,
        middle_name = request.middle_name,
        last_name = request.last_name,
        date_of_birth = request.date_of_birth,
        position = request.position,
        active = request.active,
        image_url = request.image_url,
        created_at = datetime.datetime.now(),
        last_modify = datetime.datetime.now(),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def update_user(db:Session, id: int, current_user:bool, request: UserUpdateBase):
    user = db.query(DbUser).filter(DbUser.id == id).first()
    
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
          detail = f"User id {id} not found!")
    
    if not current_user:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED,
          detail = f"User don't have authorization!")
        
    user.email = request.email
    user.password = Hash.bcrypt(request.password)
    user.administrator = request.administrator
    user.name = request.name
    user.middle_name = request.middle_name
    user.last_name = request.last_name
    user.date_of_birth = request.date_of_birth
    user.position = request.position
    user.active = request.active
    user.image_url = request.image_url
    user.last_modify = request.last_modify

    user_exist = db.query(DbUser).filter(DbUser.email == request.email).first()
    if user_exist and user_exist.id != user.id:
        raise HTTPException(status_code = status.HTTP_409_CONFLICT,
          detail = f"Inserted email already exist!")

    db.commit()
    db.refresh(user)
    return user

def get_user_by_email(db: Session, email: str):
    user = db.query(DbUser).filter(DbUser.email == email).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail=f'User with email {email} not found')
    return user

def get_user_by_id(db: Session, id: str, current_user:DbUser):

    if (not current_user.administrator and not current_user.id==id):
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED,
          detail = f"User don't have authorization!")
    
    user = db.query(DbUser).filter(DbUser.id == id).first()

    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail=f'User with id {id} not found')
    return user

def get_all_users(db: Session, current_user_admin:bool):
    if (not current_user_admin):
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED,
          detail = f"User don't have authorization!")
    
    return db.query(DbUser).all()

def delete(db: Session, id: int, current_user_admin:bool):
    user = db.query(DbUser).filter(DbUser.id == id).first()

    if not current_user_admin:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED,
          detail = f"User don't have authorization!")
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail = f"user with id {id} not found")
    
    db.delete(user)
    db.commit()
    return 'ok'

# NAPRAVI OVO KAKO SPADA
def upload_image(email, image: UploadFile = File(...)):
   if hasattr(image, 'filename'):
       new = f'_{email}.'
       filename = new.join(image.filename.rsplit('.', 1))
       path = f'images/users/{filename}'
    #    return path
   else:
       path = f"/images/users/{email}"


   with open(path, "w+b") as buffer:
      shutil.copyfileobj(image.file, buffer)
      return {'filename': path}
