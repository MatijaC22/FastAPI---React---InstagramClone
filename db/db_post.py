import math
from routers.schemas import PostBase, PostInsert
from sqlalchemy.orm.session import Session
from db.models import DbPost, DbContainer, DbUser
import datetime
from fastapi import HTTPException, status, UploadFile
from utils import validate_file_extension, validate_file_size
from typing import List
import os


def create(db: Session,  images:List[UploadFile], reference_number:str, description:str, current_user:DbUser):
    container_exist = db.query(DbContainer).filter(DbContainer.reference_number == reference_number).first()
    
    if container_exist is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
          detail = f"Inserted container reference number doesn't exist!")
    
    post_exist = db.query(DbPost).filter(DbPost.reference_number == reference_number).first()
    
    if post_exist is not None and container_exist.reference_number == post_exist.reference_number:
        raise HTTPException(status_code = status.HTTP_403_FORBIDDEN,
          detail = f"Post for this container reference already exist")
    
    if container_exist.responsible_email != current_user.email:
        raise HTTPException(status_code = status.HTTP_403_FORBIDDEN,
          detail = f"This user is not assigned for this container")

    
    image_dir = f"images/posts/{reference_number}"
    os.makedirs(image_dir, exist_ok=True)
    
    imageListAsString = ''
    for image in images:
        validate_file_extension(os.path.splitext(image.filename)[1])        
        validate_file_size(image.file, 5 * 1024 * 1024)
        
        imageListAsString = imageListAsString+image.filename+','

        file_path = os.path.join(image_dir, image.filename)
        with open(file_path, "wb") as f:
            f.write(image.file.read())
    
    new_post = DbPost(
        image_url = imageListAsString,
        description = description,
        user_id = current_user.id,
        created_at = datetime.datetime.now(),
        last_modify = datetime.datetime.now(),
        reference_number = reference_number
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

def get_all(db: Session, current_user:DbUser):
    if not current_user.administrator:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED,
          detail = f"User don't have authorization!")
    
    return db.query(DbPost).all()

def get_all_package(db: Session, current_user:DbUser, user_id=None, page: int = 1, per_page: int = 10):
    
    offset = (page - 1) * per_page

    # IF ADMINISTRATOR
    if current_user.administrator:
        query = db.query(DbPost)
        if user_id:
            query = query.filter(DbPost.user_id == user_id)
        
        total_lines = query.count()  # Get the total number of lines

        query = query.order_by(DbPost.last_modify.desc()).offset(offset).limit(per_page).all()
        total_pages = math.ceil(total_lines / per_page)  # Calculate the total number of pages
        return {
            "lines": total_lines,
            "pages": total_pages,
            "page": page,
            "per_page": per_page,
            "data": query,
        }
        # return query

    # IF NOT ADMINISTRATOR
    if not current_user.administrator:
        query = db.query(DbPost).filter(DbPost.user_id == current_user.id)
        total_lines = query.count()  # Get the total number of lines
        query = query.order_by(DbPost.last_modify.desc()).offset(offset).limit(per_page).all()
        
        total_pages = math.ceil(total_lines / per_page)  # Calculate the total number of pages
        return {
            "lines": total_lines,
            "pages": total_pages,
            "page": page,
            "per_page": per_page,
            "data": query,
        }
        # return query

# GORNJA FUNKCIJA RADI TAJ POSAO   
# def get_user_posts(db: Session, current_user:DbUser, user_id=None, page: int = 1, per_page: int = 10):
#     offset = (page - 1) * per_page

#     if not current_user.administrator:
#         query = db.query(DbPost).filter(DbPost.user_id == current_user.id)
#         query = query.order_by(DbPost.last_modify.desc()).offset(offset).limit(per_page).all()
#         return query    

def get_one(db: Session, id: int, current_user:DbUser):
    
    post = db.query(DbPost).filter(DbPost.id == id).first()
    
    if not post:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail = f"Post with id {id} not found")
    
    if not current_user.administrator and post.user_id != current_user.id:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED,
          detail = f"User don't have authorization!")
    
    return post

def update_post(db:Session, id: int, current_user:DbUser, request: PostInsert):
    post = db.query(DbPost).filter(DbPost.id == id).first()
    
    if not post:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
          detail = f"Post id {id} not found!")
    

    #ZAVRSI OVO IDEJA JE OCISTITI DA SE UPDATE POST
    if current_user.id != post.user_id:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED,
          detail = f"User don't have authorization!")
       
    post.image_url = request.reference_number
    post.description = request.description
    post.reference_number = request.reference_number
    post.last_modify: datetime.datetime.now()

    db.commit()
    db.refresh(post)
    return post

def delete(db: Session, id: int, user_id: int):
    post = db.query(DbPost).filter(DbPost.id == id).first()
    if not post:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail = f"post with id {id} not found")
    if (post.user_id != user_id):
        raise HTTPException(status_code = status.HTTP_403_FORBIDDEN,
                            detail = 'only post creator can delete post')
    
    db.delete(post)
    db.commit()
    return 'ok'