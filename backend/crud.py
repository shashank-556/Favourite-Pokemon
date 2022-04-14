from sqlalchemy.orm import Session
import models,schemas

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_user_by_id(db:Session,user_id:int) :
    return db.query(models.User).filter(models.User.id == user_id).first()
 
async def create_user(db:Session,usr:schemas.userInputModel) :
    db_user = models.User(**usr.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

async def add_pokemon(db:Session,user_id,pokemon_id) :
    db_row = models.Fav_Pokemon(user_id = user_id,pokemon_id=pokemon_id)
    db.add(db_row)
    db.commit()
    db.refresh(db_row)
    return db_row

async def delete_pokemon(db:Session,user_id,pokemon_id) :
    db.query(models.Fav_Pokemon).delete(models.Fav_Pokemon.user_id == user_id and models.Fav_Pokemon.pokemon_id == pokemon_id)