from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, relationship
from sqlalchemy.sql.schema import Column, ForeignKey, Table
from sqlalchemy.sql.sqltypes import Integer, String

Base = declarative_base()

character_skill = Table(
    "character_skill",
    Base.metadata,
    Column("character_id", Integer, ForeignKey("character.id")),
    Column("skill_id", Integer, ForeignKey("skill.id")),
    Column("degre", Integer)
)

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    user_name = Column(String)
    user_discord_id = Column(Integer)
    characters = relationship("character", backref=backref("user"))

class Character(Base):
    __table__ = "character"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    level = Column(Integer)
    strength = Column(Integer)
    dexterity = Column(Integer)
    constitution = Column(Integer)
    intelligence = Column(Integer)
    wisdom = Column(Integer)
    charisma = Column(Integer)

class Skill(Base):
    __table__ = "skill"
    id = Column(Integer, primary_key=True)
    skill_name = Column(String)
    skill_characteristic_1 = Column(String)
    skill_characteristic_2 = Column(String)
