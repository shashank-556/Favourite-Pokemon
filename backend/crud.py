from sqlalchemy.orm import Session
import models,schemas

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_user_by_id(db:Session,user_id:int) :
    return db.get(models.User,user_id)
 
async def create_user(db:Session,usr:schemas.userInputModel) :
    db_user = models.User(**usr.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

async def get_pokemon(db:Session,usr:models.User) :
    return [i.pokemon_id for  i in usr.pokemons ]

async def add_pokemon(db:Session,user_id,pokemon_id) :
    db_row = models.Fav_Pokemon(user_id = user_id,pokemon_id=pokemon_id)
    db.add(db_row)
    db.commit()
    db.refresh(db_row)
    return db_row

async def delete_pokemon(db:Session,user_id,pokemon_id) :
    db.query(models.Fav_Pokemon).filter(models.Fav_Pokemon.user_id == user_id, models.Fav_Pokemon.pokemon_id == pokemon_id).delete()
    db.commit()
    