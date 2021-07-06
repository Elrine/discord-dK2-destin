import asyncio
import discord
from discord import User
from discord.channel import TextChannel
from discord.emoji import Emoji
from discord.message import Message
from emoji import EMOJI_UNICODE_ENGLISH as EMOJIS
from discord_bot.DBManager import DBManager
from discord_bot.model import CharacterModel
import re

from random import randrange
from discord.ext import commands

class AppBot():
    def __init__(self, _token):
        self.token = _token
        self.bot = commands.Bot(command_prefix="/")
        self.manage = DBManager()

    def _createCharacter(self, character : CharacterModel, channel : TextChannel, user : User, is_dm = False):
        characteristics_point = 15
        question_msg = channel.send(f"Vous avez {characteristics_point} point répartir dans les caractéristique suivant:\n- {character.strength} Force \U0001F4AA\n- {character.dexterity} Dextérité \U0001F3AF\n- {character.constitution} Constitution \U0001F48E\n- {character.intelligence} Intelligence \U0001F4A1\n- {character.wisdom} Sagesse \U0001F47C\n- {character.charisma} Charisme \U0001F3A9\nVous pouvez avoir plus d'information sur le caractéristique avec \U00002139\nVous pouvez valider avec \U0001F197")
        channel.

    def setupCommand(self):        
        @self.bot.event
        async def on_ready():
            print("Le bot est prêt !")

        @self.bot.command(name="del")
        async def delete(ctx: commands.Context, number: int):
            print("Delete command")
            messages = await ctx.history(limit=number + 1).flatten()

            for each_message in messages:
                await each_message.delete()


        @self.bot.command(name="r")
        async def roll(ctx: commands.Context, dice: str):
            result = 0
            matchs = re.findall(r"(\d+)(d(\d+))?([+-])?", dice)
            dices_result = []
            op = "+"
            for match in matchs:
                if match[1] == "":
                    match_result = ("const", int(match[0]), op)
                    dices_result.append(match_result)
                else:
                    list_dice = []
                    for _ in range(int(match[0])):
                        dice_result = randrange(int(match[2])) + 1
                        list_dice.append(dice_result)
                    dices_result.append((match[1], list_dice, op))
                op = match[3]
                if op == "":
                    break
            result_str = ""
            for index, (dice_type, dice, op) in enumerate(dices_result):
                dice_result = 0
                if index > 0:
                    result_str += op
                if dice_type == "const":
                    dice_result = dice
                    result_str += str(dice)
                else:
                    critique = int(re.match(r"d(\d+)", dice_type).group(1))
                    dice_result = sum(dice)
                    result_str += "("
                    for index, value in enumerate(dice):
                        if value == 1:
                            result_str += f"~~**{value}**~~:game_die:"
                        elif value == critique:
                            result_str += f"**{value}**:dart:"
                        else:
                            result_str += str(value)
                        if index + 1 < len(dice):
                            result_str += "+"
                    result_str += ")"
                if op == "+":
                    result += dice_result
                else:
                    result -= dice_result
            result_str += f"\n={result}"
            await ctx.send(result_str)
    
        @self.bot.command(name="join")
        async def join(ctx: commands.Context):
            self.manage.addUser(ctx.author.name, ctx.author.id)

        @self.bot.command(name="character")
        async def character(ctx : commands.Context, command : str, *option):
            await ctx.message.delete()
            if command == "create":
                if self.manage.getUser(ctx.author.id) == None:
                    await ctx.send("Vous ne vous est pas enregistrer")
                    return
                character_name = None
                if len(option) > 0:
                    character_name = option[0]
                if character_name == None:
                    msg : Message = await ctx.send("Quel est le nom de votre personnage?")
                    character_msg : Message = await self.bot.wait_for("message", check=(lambda m: m.author.id == ctx.author.id and m.channel.id == ctx.channel.id))
                    character_name = character_msg.content
                    await msg.delete()
                    await character_msg.delete()
                create_msg : Message = await ctx.send(f"Création de {character_name}...")
                character = self.manage.createCharacter(character_name, user_id=ctx.author.id)
                if character == None:
                    await create_msg.edit(content=f"Création de {character_name}...Échec")
                    await create_msg.delete(delay=10)
                else:
                    await create_msg.edit(content=f"Création de {character_name}...Fait")
                    question_msg : Message = await ctx.send("Voulez vous continer la création ici?")
                    await question_msg.add_reaction(EMOJIS[":thumbs_up:"])
                    await question_msg.add_reaction(EMOJIS[":thumbs_down:"])
                    try:
                        reaction, _ = await self.bot.wait_for('reaction_add', timeout=30.0, check=(lambda r, u: u == ctx.author and (str(r.emoji) == EMOJIS[":thumbs_up:"] or str(r.emoji) == EMOJIS[":thumbs_down:"])))
                        if reaction.emoji == EMOJIS[":thumbs_up:"]:
                            pass # TODO create method to create the character in the server
                        elif reaction.emoji == EMOJIS[":thumbs_down:"]:
                            channel = ctx.author.dm_channel
                            if channel == None:
                                channel = ctx.author.create_dm()
                            pass # TODO create method to create the character in DM
                        
                    except asyncio.TimeoutError:
                        await question_msg.delete()

        @self.bot.command(name="test")
        async def test(ctx : commands.Context):
            await ctx.message.delete()
            msg : Message = await ctx.send(f"Vous avez {15} point répartir dans les caractéristique suivant:\n- {0} Force \U0001F4AA\n- {0} Dextérité \U0001F3AF\n- {0} Constitution \U0001F48E\n- {0} Intelligence \U0001F4A1\n- {0} Sagesse \U0001F47C\n- {0} Charisme \U0001F3A9\nVous pouvez avoir plus d'information sur le caractéristique avec \U00002139\nVous pouvez valider avec \U0001F197")
            await msg.add_reaction(u"\U0001F4AA")
            await msg.add_reaction(u"\U0001F3AF")
            await msg.add_reaction(u"\U0001F48E")
            await msg.add_reaction(u"\U0001F4A1")
            await msg.add_reaction(u"\U0001F47C")
            await msg.add_reaction(u"\U0001F3A9")
            await msg.add_reaction(u"\U00002139")
            await msg.add_reaction(u"\U0001F197")
            try:
                reaction, _ = await self.bot.wait_for('reaction_add', timeout=10.0, check=(lambda r, u: u == ctx.author))
                print(reaction.emoji, reaction.emoji == u"\U00002139")
                next_msg : Message = await ctx.send(reaction.emoji)
            except asyncio.TimeoutError:
                next_msg : Message = await ctx.send("Timeout message")
            await msg.delete(delay=10)
            await next_msg.delete(delay=10)

    def run(self):
        self.bot.run(self.token)