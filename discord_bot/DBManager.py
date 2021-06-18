import sqlalchemy
from sqlalchemy.sql.elements import False_, True_
from sqlalchemy.sql.expression import insert, select
import discord_bot.model as model
from sqlalchemy import create_engine


class DBManager():
    def __init__(self) -> None:
        self.engine = create_engine(
            "sqlite:///db.sqlite3", future=True)
        model.Base.metadata.create_all(self.engine)
        self.initSkill()

    def initSkill(self):
        stmt = select(model.SkillModel)
        with sqlalchemy.orm.Session(self.engine, future=True) as session:
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
                        )
                    ]
                )
                session.commit()

    def initSkill(self):
        stmt = select(model.AssetModel)
        session = sqlalchemy.orm.Session(self.engine, future=True)
        result = session.execute(stmt).all()
        if len(result) == 0:
            session.add_all(
                [
                    model.AssetModel(
                        name=""
                    )
                ]
            )
            session.commit()
        session.close()

    def addUser(self, _user_name, _user_id) -> None:
        stmt = insert(model.UserModel).values(
            user_name=_user_name, user_discord_id=_user_id)
