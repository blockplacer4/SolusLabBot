import discord
import ezcord
from utils.loadenv import discord_bot_token

bot = ezcord.Bot(intents=discord.Intents.all())
bot.load_extension('cogs.listeners')

bot.run(discord_bot_token)