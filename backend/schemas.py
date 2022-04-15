from pydantic import BaseModel, Field

class userBaseModel(BaseModel) :
    email:str = Field(...,max_length=30)
    name: str = Field(...,max_length=30)

class userOutputModel(userBaseModel) :
    id:int
    class Config:
        orm_mode = True

class userInputModel(userBaseModel) :
    password:str = Field(...,min_length=8)

class Token(BaseModel):
    access_token: str
    token_type: str