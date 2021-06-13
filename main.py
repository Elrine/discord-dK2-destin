from discord_bot.AppBot import AppBot
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env/config")

bot = AppBot(os.getenv("DISCORD_TOKEN"))
bot.setupCommand()
bot.run()
