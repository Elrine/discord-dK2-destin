from discord_bot.DBManager import DBManager
import re

from random import randrange
from discord.ext import commands

class AppBot():
    def __init__(self, _token):
        self.token = _token
        self.bot = commands.Bot(command_prefix="/")
        self.manage = DBManager()

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
    
    def run(self):
        self.bot.run(self.token)