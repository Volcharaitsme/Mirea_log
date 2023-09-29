from pydantic import BaseModel, EmailStr
from typing import List, Optional


class BookingBase(BaseModel):
    title: str
    description: Optional[str] = None


class BookingCreate(BookingBase):
    pass


class Booking(BookingBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str


UserAuth = UserCreate


class LiteUser(UserBase):
    id: int


class User(UserBase):
    id: int
    is_active: bool
    bookings: List[Booking] = []

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
