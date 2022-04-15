from databases import Base
from sqlalchemy import Column, ForeignKey,String,Integer, UniqueConstraint
from sqlalchemy.orm import relationship

class User(Base) :
    __tablename__ = "users"
    id = Column(Integer,primary_key = True)
    email = Column(String(30),unique = True,index = True)
    name = Column(String(30),nullable = False)
    password = Column(String(80),nullable = False)
    pokemons = relationship("Fav_Pokemon",cascade="all, delete")

    def __repr__(self) -> str:
        return f"User(id={self.id}, email={self.email}, name={self.name})"

class Fav_Pokemon(Base) :
    __tablename__ = "pokemons"
    id = Column(Integer,primary_key=True)
    user_id = Column(Integer,ForeignKey('users.id'),nullable = False)
    pokemon_id = Column(Integer,nullable = False)

    __table_args__ = (UniqueConstraint('user_id','pokemon_id',name = 'user_pokemon_uc'),)
