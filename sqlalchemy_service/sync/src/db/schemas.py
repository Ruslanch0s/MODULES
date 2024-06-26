from pydantic import BaseModel


class UserBaseSchema(BaseModel):
    name: str
    email: str


class UserCreateSchema(UserBaseSchema):
    hashed_password: str


class UserSchema(UserBaseSchema):
    id: int

    class Config:
        from_attributes = True
