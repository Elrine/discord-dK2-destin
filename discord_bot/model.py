from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, relationship
from sqlalchemy.sql.schema import Column, ForeignKey, Table
from sqlalchemy.sql.sqltypes import Boolean, Integer, String

Base = declarative_base()

character_skill = Table(
    "character_skill",
    Base.metadata,
    Column("character_id", Integer, ForeignKey("character.id")),
    Column("skill_id", Integer, ForeignKey("skill.id")),
    Column("degre", Integer)
)

character_asset = Table(
    "character_asset",
    Base.metadata,
    Column("character_id", Integer, ForeignKey("character.id")),
    Column("asset_id", Integer, ForeignKey("asset.id")),
)

class UserModel(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    user_name = Column(String)
    user_discord_id = Column(Integer)
    characters = relationship("CharacterModel", backref=backref("user"))

    def __init__(self, user_name="", user_discord_id=0) -> None:
        super().__init__()
        self.user_name = user_name
        self.user_discord_id = user_discord_id

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.user_name!r}, discord_id={self.user_discord_id!r})"

class CharacterModel(Base):
    __tablename__ = "character"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    level = Column(Integer)
    strength = Column(Integer)
    dexterity = Column(Integer)
    constitution = Column(Integer)
    intelligence = Column(Integer)
    wisdom = Column(Integer)
    charisma = Column(Integer)
    
    def __init__(self, name="", user_id=0, level=0, strength=0, dexterity=0, constitution=0, intelligence=0, wisdom=0, charisma=0) -> None:
        super().__init__()
        self.name = name
        self.user_id = user_id
        self.level = level
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma - charisma

    def __repr__(self) -> str:
        return f"Character(id={self.id!r}, level={self.level!r}, strength={self.strength!r}), dexterity={self.dexterity!r}), constitution={self.constitution!r}), intelligence={self.intelligence!r}), wisdom={self.wisdom!r}), charisma={self.charisma!r})"

class SkillModel(Base):
    __tablename__ = "skill"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    characteristic_1 = Column(String)
    characteristic_2 = Column(String)
    description = Column(String)
    clutter_malus = Column(Boolean)

    def __init__(self, name="", characteristic_1="", characteristic_2="", description="", clutter_malus=False) -> None:
        super().__init__()
        self.name = name
        self.characteristic_1 = characteristic_1
        self.characteristic_2 = characteristic_2
        self.description = description
        self.clutter_malus = clutter_malus

    def __repr__(self) -> str:
        return f"Skill(id={self.id!r}, name={self.name!r}, characteristic_1={self.characteristic_1!r}, characteristic_2={self.characteristic_2!r}, description={self.description!r}, clutter_malus={self.clutter_malus!r})"

class AssetModel(Base):
    __tablename__ = "asset"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    
    def __init__(self, name="", description="") -> None:
        super().__init__()
        self.name = name
        self.description = description

    def __repr__(self) -> str:
        return f"Asset(id={self.id!r}, name={self.name!r}, description={self.description!r})"