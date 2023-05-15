from sqlalchemy.orm.session import Session
from db.models import DbComment
from routers.schemas import CommentBase
from datetime import datetime
from fastapi import HTTPException, status


def create(db: Session, request: CommentBase):
    new_comment = DbComment(
        text = request.text,
        username = request.username,
        post_id = request.post_id,
        timestamp = datetime.now()
    )
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment


def get_all(db : Session, post_id: int):
    return db.query(DbComment).filter(DbComment.post_id == post_id ).all()
    
def delete(db: Session, id: int, user_id: int):
    comment = db.query(DbComment).filter(DbComment.id == id).first()
    if not comment:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail = f"comment with id {id} not found")
    
    print(comment.username)
    print(user_id)

    if (comment.username != user_id):
        raise HTTPException(status_code = status.HTTP_403_FORBIDDEN,
                            detail = 'only comment creator can delete comment')
    
    db.delete(comment)
    db.commit()
    return 'ok'