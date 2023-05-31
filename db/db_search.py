from routers.schemas import PostDisplay
from sqlalchemy.orm.session import Session 
from db.models import DbUser, DbPost, DbContainer
from fastapi import HTTPException, status
from sqlalchemy import or_

def get_search_posts(search_term: str, db: Session, current_user:DbUser):

    if current_user.administrator:
      results = db.query(DbPost).join(DbContainer).join(DbUser).filter(
        or_(
            DbPost.description.ilike(f'%{search_term}%'),
            DbPost.reference_number.ilike(f'%{search_term}%'),
            DbUser.email.ilike(f'%{search_term}%'),
            DbUser.name.ilike(f'%{search_term}%'),
            DbUser.last_name.ilike(f'%{search_term}%'),
            DbUser.position.ilike(f'%{search_term}%'),
            DbContainer.location.ilike(f'%{search_term}%'),
            DbContainer.country.ilike(f'%{search_term}%'),
            DbContainer.responsible_name.ilike(f'%{search_term}%'),
            DbContainer.responsible_email.ilike(f'%{search_term}%'),
            DbContainer.client_name.ilike(f'%{search_term}%'),
            DbContainer.transport_type.ilike(f'%{search_term}%'),
            DbContainer.product_type.ilike(f'%{search_term}%'),
            # Add more columns as needed
        )
        ).all()
      return results
    
    results = db.query(DbPost).join(DbContainer).join(DbUser).filter(
        DbPost.user_id == current_user.id,
        or_(
            DbPost.description.ilike(f'%{search_term}%'),
            DbPost.reference_number.ilike(f'%{search_term}%'),
            DbUser.email.ilike(f'%{search_term}%'),
            DbUser.name.ilike(f'%{search_term}%'),
            DbUser.last_name.ilike(f'%{search_term}%'),
            DbUser.position.ilike(f'%{search_term}%'),
            DbUser.position.ilike(f'%{search_term}%'),
            DbContainer.location.ilike(f'%{search_term}%'),
            DbContainer.country.ilike(f'%{search_term}%'),
            DbContainer.responsible_name.ilike(f'%{search_term}%'),
            DbContainer.responsible_email.ilike(f'%{search_term}%'),
            DbContainer.client_name.ilike(f'%{search_term}%'),
            DbContainer.transport_type.ilike(f'%{search_term}%'),
            DbContainer.product_type.ilike(f'%{search_term}%'),
            # Add more columns as needed
        )
        ).all()
    return results


