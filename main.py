import settings
import discord
from discord.ext import commands

logger = settings.logging.getLogger("bot")

def run():
    intents = discord.Intents.default()

    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():
        print(bot.user)
        print(bot.user.id)
        print("__________________")


    bot.run(settings.DISCORD_API_SECRET, root_logger=True)

if __name__ == "__main__":
    run()