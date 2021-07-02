from operator import and_, mod
from typing import List, Tuple, Union
import sqlalchemy
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.elements import False_, True_
from sqlalchemy.sql.expression import insert, select, update
from sqlalchemy.sql.functions import mode
import discord_bot.model as model
from sqlalchemy import create_engine


class DBManager():
    def __init__(self) -> None:
        self.engine = create_engine(
            "sqlite:///db.sqlite3", future=True, echo=True)
        model.Base.metadata.create_all(self.engine)
        self.initSkill()
        self.initAsset()

    def initSkill(self):
        with Session(self.engine, future=True) as session:
            session : Session
            stmt = select(model.SkillModel)
            result = session.execute(stmt).all()
            if len(result) == 0:
                session.add_all(
                    [
                        model.SkillModel(
                            name="Athlétisme",
                            characteristic_1="STR",
                            characteristic_2="DEX",
                            description="Utilisez cette compétence pour courir, sauter, faire des bonds et des cabrioles, escalaer des murs et des falaises, nager. C'est aussi la compétence des sports et de presque toutes les activités physiques athlétiques. Cette compétence peut aussi réduire les dommages encaissés lors d'une chute.",
                            clutter_malus=True
                        ),
                        model.SkillModel(
                            name="Bluff",
                            characteristic_1="INT",
                            characteristic_2="CHA",
                            description="Vous permet de mentir ou de baratiner. On peut résister à l'utilisation de cette compétance grâce à un jet de *Psychologie* ou de *bluff*.",
                            clutter_malus=False
                        ),
                        model.SkillModel(
                            name="Concentration",
                            characteristic_1="CON",
                            characteristic_2="WIS",
                            description="Servez-vous de cette compétence pour vous concentrer sur une tâche ou pour méditer. Vous pouvez aussi regagner ou faire regagner des points d'énergie.",
                            clutter_malus=False
                        ),
                        model.SkillModel(
                            name="Déguisement",
                            characteristic_1="DEX",
                            characteristic_2="CHA",
                            description="Cette compétence est utile pour se travestir ou se maquiller. On peut percer à jour un déguisement grâce à un jet de Perception en opposition. Il faut un minimum de 10 tours pour se déguiser, à condition d'avoir le matériel adéquat.",
                            clutter_malus=False
                        ),
                        model.SkillModel(
                            name="Diplomatie",
                            characteristic_1="INT",
                            characteristic_2="CHA",
                            description="Utilisez cette compétence pour parler à un auditoire, chercher à convaincre un interlocuteur grâce à des arguments cohérents ou cal mer des personnes hostiles. C'est aussi la compétence qu'il vous faut si vous voulez savoir vous habiller correctement et vous tenir à table. On peut résister à l'utilisation de cette compétence grâce à un jet de *Psychologie* ou de *Diplomatic*.",
                            clutter_malus=False
                        ),
                        model.SkillModel(
                            name="Discrétion",
                            characteristic_1="DEX",
                            characteristic_2="INT",
                            description="Elle vous servira pour vous déplacer en silence, vous dissimuler ou camoufler sur vous un petit objet. On peut repérer un personnage discret grâce à un jet de *Perception* en opposition.",
                            clutter_malus=True
                        ),
                        model.SkillModel(
                            name="Équitation",
                            characteristic_1="DEX",
                            characteristic_2="WIS",
                            description="Les héros en font usage pour monter tous les animaux qui l'acceptent. Il est évidemment plus facile de chevaucher une créature entraînée qu'une bête sauvage. Dans certains univers, cette compétence peut être remplacée par *Conduite*.",
                            clutter_malus=False
                        ),
                        model.SkillModel(
                            name="Érudition",
                            characteristic_1="INT",
                            characteristic_2="WIS",
                            description="Cette compétence vous permet de savoir tout un tas de trucs sur tout un tas de sujets très différents. Bien entendu, vous n'êtes pas vraiment un spécialiste, mais vous en savez assez pour savoir de quoi il s'agit.",
                            clutter_malus=False
                        ),
                        model.SkillModel(
                            name="Foi",
                            characteristic_1="WIS",
                            characteristic_2="CHA",
                            description="Vous connaissez les dieux et leurs histoires de coucherie. Vous avez lu leur interview dans le dernier People magazine qui leur est consacré. Si ça se trouve, vous croyez même tout ce qu'ils racon tent et, en échange, vous savez provoquer des miracles et vous occuper des créatures que votre dieu déteste. Trop cool!",
                            clutter_malus=False
                        ),
                        model.SkillModel(
                            name="Influence",
                            characteristic_1="CHA",
                            characteristic_2="INT",
                            description="Vous connaissez quelqu'un qui connait quelqu'un qui peut vous aider. Cette com pétence vous permet d'obtenir des appuis matériels et des services de la part de personnes ou d'organisa tions. Bien entendu, comme pour Renseignements, il vous faut du temps et de l'argent pour obtenir de tel les faveurs ponctuelles - en général, une bonne soirée et un ou plusieurs d6 DO (les Dragons d'Or, la mon naie du dK) pour débloquer les verrous. Vous pouvez aussi utiliser cette compétence comme une connais sance des différents réseaux sociaux de Tendroit où vous êtes. On peut résister à cette compétence grace à un jet de *Psychologie* ou d'*Influence*.",
                            clutter_malus=False
                        ),
                        model.SkillModel(
                            name="Initiative",
                            characteristic_1="DEX",
                            characteristic_2="WIS",
                            description="Avez-vous de bons réflexes? Cette compétence sert au conteur à détermi ner qui agit le premier dans une situation conflictuelle comme un combat.",
                            clutter_malus=True
                        ),
                        model.SkillModel(
                            name="Intimidation",
                            characteristic_1="STR",
                            characteristic_2="CHA",
                            description="Utilisez cette compé tence pour impressionner un adversaire, pour donner des ordres ou pour mener des interrogatoires un peu musclés. On peut résister à cette compétence grâce à un jet de *Psychologie* ou d'*Intimidation*.",
                            clutter_malus=False
                        ),
                        model.SkillModel(
                            name="Linguistique",
                            characteristic_1="INT",
                            characteristic_2="CHA",
                            description="Vous savez parler vore langue maternelle. Vous pouvez aussi apprendre un nombre de langues égal à votre Intelligence (peut-être les connaissez-vous au début de vos aventures ou les apprendrez-vous au cours de celle-ci). Dans tous le autres cas, *Linguistique* vous permet de vous faire comprendre et d'échanger avec ceux que vous rencontre grâce à un sabir déroutant et à beaucoup de gestes. Lorsque vous ne parlez pas la même langue que vos interlocuteurs, vos compétences sociales sont limitées pa celle-ci : utilisez la moins bonne des deux.",
                            clutter_malus=False
                        ),
                        model.SkillModel(
                            name="Magie",
                            characteristic_1="INT",
                            characteristic_2="WIS",
                            description="Avec cette compétence, vous voilà prêt à utiliser des pouvoirs cosmiques phénoménaux (dans un mouchoir de poche) ! En tout ca vous savez de quoi il retourne quand on vous parle sortilège, rituel, focus, gestuelle et composantes..",
                            clutter_malus=False
                        ),
                        model.SkillModel(
                            name="Métier",
                            characteristic_1="INT",
                            characteristic_2="DEX",
                            description="Vous êtes à l'aise avec les outils et le travail manuel. Vous avez appris des techniques dans des domaines très différents. Sans être un pe cialiste d'aucun, vous vous débrouillez assez bien.",
                            clutter_malus=False
                        ),
                        model.SkillModel(
                            name="Perception",
                            characteristic_1="INT",
                            characteristic_2="WIS",
                            description="C'est la compétence reine pour voir, entendre, goûter, sentir votre environnement. Vous pouvez aussi fouiller une pièce, repérer une embuscade, examiner un lieu, etc...",
                            clutter_malus=False
                        ),
                        model.SkillModel(
                            name="Psychologie",
                            characteristic_1="INT",
                            characteristic_2="WIS",
                            description="Utilisez cette compétence résister à toutes les tentatives de manoeuvre sociale et d'influence. Vous pouvez aussi l'utiliser pour comprendre les motivations et les émotions des gens que vous côtoyez ou dont vous avez témoignage.",
                            clutter_malus=False
                        ),
                        model.SkillModel(
                            name="Renseignements",
                            characteristic_1="WIS",
                            characteristic_2="CHA",
                            description="Cette compétence vous servira à trouver des renseignements en traînant dans des endroits publics et en posant des questions. Il faut l'équivalent d'une demi-journée pour obtenir des informations. En général, vous dépensez 1d6 DO en verres payés à vos informateurs. Vous pouvez aussi utiliser cette compétence pour vous y retrouver dans les méandres d'une bureaucratie tentaculaire.",
                            clutter_malus=False
                        ),
                        model.SkillModel(
                            name="Représentation",
                            characteristic_1="CHA",
                            characteristic_2="WIS",
                            description="Cette compétence est celle des artistes, saltimbanques, musiciens, acteurs et autres pratiquants des arts vivants.",
                            clutter_malus=False
                        ),
                        model.SkillModel(
                            name="Reputation",
                            characteristic_1="CHA",
                            characteristic_2="WIS",
                            description="Vous cherchez vraiment à être connu partout parce que, quand même, c'est bon la gloire parfois. En jouant cette compétence contre une difficulté qui dépend de la nature des personnes à qui vous vous adressez (de 15 pour des gens de votre pays à 40 et plus pour de parfaits étrangers loin de chez vous), vous pouvez vous faire reconnaître et, peut-être, profiter de votre célébrité.",
                            clutter_malus=False
                        ),
                        model.SkillModel(
                            name="Sécurité",
                            characteristic_1="DEX",
                            characteristic_2="INT",
                            description="Cette compétence est pratique pour crocheter des serrures et désamorcer (ou poser) des pièges.",
                            clutter_malus=False
                        ),
                        model.SkillModel(
                            name="Subterfuge",
                            characteristic_1="DEX",
                            characteristic_2="INT",
                            description="Compétence des illusionnistes et des prestidigitateurs, elle est utile pour faire des tours de passe-passe, du vol à l'étalage ou à la tire, pour vous faufiler dans les passages étroits, vous contorsionner ou échapper à des liens. On peut résis ter à l'utilisation de cette compétence grâce à un jet de *Perception*.",
                            clutter_malus=True
                        ),
                        model.SkillModel(
                            name="Survie",
                            characteristic_1="CON",
                            characteristic_2="WIS",
                            description="La compétence préférée de tous les asociaux qui s'en servent pour chasser, monter un camp, suivre des traces, trouver leur chemin et de manière générale survivre en milieu hostile.",
                            clutter_malus=False
                        )
                    ]
                )
                session.commit()

    def initAsset(self):
        with Session(self.engine, future=True) as session:
            session : Session
            stmt = select(model.AssetModel)
            result = session.execute(stmt).all()
            if len(result) == 0:
                session.add_all(
                    [
                    ]
                )
                session.commit()

    def addAsset(self, _name, _description) -> None:
        with Session(self.engine, future=True) as session:
            session : Session
            session.add(
                model.AssetModel(name=_name, description=_description)
            )
            session.commit()

    def addUser(self, _user_name, _user_id) -> None:
        with Session(self.engine, future=True) as session:
            session : Session
            session.add(
                model.UserModel(user_name=_user_name, user_discord_id=_user_id)
            )
            session.commit()

    def createCharacter(self, _character_name, **kwargs) -> Union[model.CharacterModel, None]:
        with Session(self.engine, future=True) as session:
            session : Session
            user_id = None
            if "user_id" in kwargs:
                user_id = kwargs['user_id']
            elif 'user_discord_id' in kwargs:
                stmt = select(model.UserModel.id).where(model.UserModel.user_discord_id == kwargs['user_discord_id'])
                user_id = session.execute(stmt).scalars().first()
            if user_id != None:
                character = model.CharacterModel(name=_character_name, user_id=user_id)
                session.add(
                    character
                )
                session.flush()
                stmt = select(model.SkillModel.id)
                for row in session.execute(stmt).scalars().all():
                    session.add(model.CharacterSkillModel(character.id, row))
                session.commit()
                return character
            else:
                return None
    
    def getCharacters(self, **kwargs) -> List[model.CharacterModel]:
        with Session(self.engine, future=True) as session:
            session : Session
            user_id = None
            if "user_id" in kwargs:
                user_id = kwargs['user_id']
            elif 'user_discord_id' in kwargs:
                stmt = select(model.UserModel.id).where(model.UserModel.user_discord_id == kwargs['user_discord_id'])
                user_id = session.execute(stmt).scalars().first()
            if user_id != None:
                stmt = select(model.CharacterModel).where(model.CharacterModel.user_id == user_id)
                return session.execute(stmt).scalars().all()
            else:
                return []

    def getCharacterSkill(self, character : model.CharacterModel) -> List[Tuple[model.CharacterSkillModel, model.SkillModel]]:
        with Session(self.engine, future=True) as session:
            session : Session
            stmt = select(model.CharacterSkillModel, model.SkillModel).where(model.CharacterSkillModel.character_id == character.id).join(model.SkillModel, model.CharacterSkillModel.skill_id == model.SkillModel.id)
            return session.execute(stmt).all()

    def updateCharacterSkill(self, character_skill : model.CharacterSkillModel) -> None:
        with Session(self.engine, future=True) as session:
            session : Session
            stmt = update(model.CharacterSkillModel).where(model.CharacterSkillModel.id == character_skill.id).values(
                degre=character_skill.degre,
                bonus=character_skill.degre
            )
            session.execute(stmt)

    def updateCharacter(self, character : model.CharacterModel) -> None:
        with Session(self.engine, future=True) as session:
            session : Session
            stmt = update(model.CharacterModel).where(model.CharacterModel.id == character.id).values(
                name=character.name,
                level=character.level,
                strength=character.strength,
                dexterity=character.dexterity,
                constitution=character.constitution,
                intelligence=character.intelligence,
                wisdom=character.wisdom,
                charisma=character.charisma
            )
            session.execute(stmt)