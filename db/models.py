from db.database import Base
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String, DateTime, Boolean
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship


class DbUser(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    # username = Column(String)
    password = Column(String)
    email = Column(String, unique=True)
    administrator = Column(Boolean)
    name = Column(String)
    middle_name = Column(String)
    last_name = Column(String)
    date_of_birth = Column(String)
    position = Column(String)
    image_url = Column(String)
    active = Column(Boolean)
    created_at = Column(DateTime)
    last_modify = Column(DateTime)
    items = relationship('DbPost', back_populates='user')



# RADIM NA OVOM !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class DbContainer(Base):
    __tablename__ = 'container'
    id = Column(Integer, primary_key=True, index=True)
    reference_number = Column(String, nullable=False)
    location = Column(String)
    country = Column(String)
    responsible_name = Column(String)
    client_name = Column(String)
    transport_type = Column(String)
    product_type = Column(String)
    created_at = Column(DateTime)
    last_modify = Column(DateTime)
    post = relationship('DbPost', back_populates='container')


class DbPost(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True, index=True)
    image_url = Column(String)
    image_url_type = Column(String)
    caption = Column(String)
    created_at = Column(DateTime)
    last_modify = Column(DateTime)
    reference_number = Column(Integer, ForeignKey('container.reference_number'))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('DbUser', back_populates='items')
    comments = relationship('DbComment', back_populates='post')
    container = relationship('DbContainer', back_populates='post')


class DbComment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key= True, index = True)
    text = Column(String)
    username = Column(String)
    timestamp = Column(DateTime)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship("DbPost", back_populates='comments')

