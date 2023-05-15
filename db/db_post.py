from routers.schemas import PostBase
from sqlalchemy.orm.session import Session
from db.models import DbPost
import datetime
from fastapi import HTTPException, status

def create(db: Session, request: PostBase):
    new_post = DbPost(
        image_url = request.image_url,
        image_url_type = request.image_url_type,
        caption = request.caption,
        timestamp = datetime.datetime.now(),
        user_id = request.creator_id
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

def get_all(db: Session):
    return db.query(DbPost).all()

def get_all_package(db: Session, user_id=None, page: int = 1, per_page: int = 10):
    offset = (page - 1) * per_page
    query = db.query(DbPost)
    if user_id:
        query = query.filter(DbPost.user_id == user_id)
    query = query.order_by(DbPost.timestamp.desc()).offset(offset).limit(per_page).all()
    return query

def get_one(db: Session, id: int):
    post = db.query(DbPost).filter(DbPost.id == id).first()
    if not post:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail = f"post with id {id} not found")
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