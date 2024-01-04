from pydantic import BaseModel

class User(BaseModel):
    full_name: str
    email: str
    phone_number: str
    national_id: str
    password: str

class UserInDB(User):
    hashed_password: str

class Token(BaseModel):
    access_token: str
    refresh_token: str

class Hotel(BaseModel):
    name: str
    location: str