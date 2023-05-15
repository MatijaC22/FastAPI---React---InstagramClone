from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

#############*** USER ***##################
class UserBase(BaseModel):
    email: str
    password: str
    administrator: bool
    name: str
    middle_name: str
    last_name: str
    date_of_birth: str
    position: str
    image_url: str
    active : bool
    created_at: Optional[datetime] = None
    last_modify: Optional[datetime] = None

class UserUpdateBase(BaseModel):
    email: str
    password: str
    administrator: bool
    name: str
    middle_name: str
    last_name: str
    date_of_birth: str
    position: str
    active: bool
    image_url: str
    last_modify: datetime
    # class Config():
    #     orm_mode = True

class UserDisplay(BaseModel):
    id:int
    email:str
    administrator: bool
    name: str
    middle_name: str
    last_name: str
    date_of_birth: str
    position: str
    active: bool
    image_url: str
    created_at: datetime
    last_modify: datetime
    class Config():
        orm_mode = True

###########################################
###########*** CONTAINER ***###############
class ContainerBase(BaseModel):
    reference_number: str
    location: str
    country: str
    responsible_name: str
    client_name: str
    transport_type: str
    product_type: str
    created_at: Optional[datetime] = None
    last_modify: Optional[datetime] = None

class ContainerDisplay(BaseModel):
    reference_number: str
    location: str
    country: str
    responsible_name: str
    client_name: str
    transport_type: str
    product_type: str
    created_at: datetime
    last_modify: datetime
    class Config():
        orm_mode = True

###########################################
#############*** POST ***##################
class PostBase(BaseModel):
    image_url: str
    image_url_type: str
    caption: str
    creator_id: int

# For PostDisplay
class User(BaseModel):
    username: str
    id: int
    class Config():
        orm_mode = True

# For PostDisplay
class Comment(BaseModel):
    text: str
    username: str
    timestamp: datetime
    class Config():
        orm_mode = True

     
class PostDisplay(BaseModel):
    id: int
    image_url: str
    image_url_type: str
    caption: str
    timestamp: datetime
    user: User
    comments: List[Comment]
    class Config():
        orm_mode = True

class UserAuth(BaseModel):
    id: int
    email: str
    class Config():
        orm_mode = True

###########################################
###########*** COMMENT ***#################

class CommentBase(BaseModel):
    username: str
    text: str
    post_id: int
