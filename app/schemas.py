from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr
from pydantic.types import conint


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class CreatePost(PostBase):
    pass


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True


class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config:
        orm_mode = True


class PostVote(BaseModel):
    Post: Post
    votes: int

    class Config:
        orm_mode = True

# ********** USERS ******** #


class CreateUser(BaseModel):
    email: EmailStr
    password: str


# ******* AUTH ****** #
class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None


'''VOTE SCHEMA'''


class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)
