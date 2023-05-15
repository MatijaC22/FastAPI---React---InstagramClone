from routers.schemas import ContainerBase
from sqlalchemy.orm.session import Session 
from db.models import DbContainer
from fastapi import HTTPException, status
import datetime


def create_container(db: Session, current_user:bool, request: ContainerBase):
    if not current_user:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED,
          detail = f"User don't have authorization!")
    
    container_exist = db.query(DbContainer).filter(DbContainer.reference_number == request.reference_number).first()
    if container_exist:
        raise HTTPException(status_code = status.HTTP_409_CONFLICT,
          detail = f"Inserted container reference number already exist!")
    
    
    new_container = DbContainer(       
        reference_number = request.reference_number,
        location = request.location,
        country = request.country,
        responsible_name = request.responsible_name,
        client_name = request.client_name,
        transport_type = request.transport_type,
        product_type = request.product_type,
        created_at = datetime.datetime.now(),
        last_modify = datetime.datetime.now(),
    )
    db.add(new_container)
    db.commit()
    db.refresh(new_container)
    return new_container

def update_container(db:Session, id: int, current_user:bool, request: ContainerBase):
    container = db.query(DbContainer).filter(DbContainer.id == id).first()
    
    if not container:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
          detail = f"Container id {id} not found!")
    
    if not current_user:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED,
          detail = f"User don't have authorization!")
        
    container.reference_number = request.reference_number
    container.location = request.location
    container.country = request.country
    container.responsible_name = request.responsible_name
    container.client_name = request.client_name
    container.transport_type = request.transport_type
    container.product_type = request.product_type
    container.last_modify = datetime.datetime.now()

    container_exist = db.query(DbContainer).filter(DbContainer.email == request.email).first()
    if container_exist and container_exist.id != container.id:
        raise HTTPException(status_code = status.HTTP_409_CONFLICT,
          detail = f"Inserted email already exist!")

    db.commit()
    db.refresh(container)
    return container

def get_container_by_reference_number(db: Session, reference_number: str):
    container = db.query(DbContainer).filter(DbContainer.reference_number == reference_number).first()
    if not container:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail=f'Container with reference_number {reference_number} not found')
    return container

def get_container_by_id(db: Session, id: str, current_user:DbContainer):

    if (not current_user.administrator and not current_user.id==id):
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED,
          detail = f"User don't have authorization!")
    
    container = db.query(DbContainer).filter(DbContainer.id == id).first()

    if not container:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail=f'Container with id {id} not found')
    return container

def get_all_containers(db: Session, current_user_admin:bool):
    if (not current_user_admin):
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED,
          detail = f"User don't have authorization!")
    
    return db.query(DbContainer).all()

def delete(db: Session, id: int, current_user_admin:bool):
    container = db.query(DbContainer).filter(DbContainer.id == id).first()

    if not current_user_admin:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED,
          detail = f"User don't have authorization!")
    if not container:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail = f"Container with id {id} not found")
    
    db.delete(container)
    db.commit()
    return 'ok'

