import discord, asyncio
from discord.ext import commands
from . import command
from .tools.json_manager import read_json

config = read_json("static/json/config.json")

TOKEN = config["TOKEN"]
PREFIX = "/"

voice_clients = {}
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
#Создаємо бота
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

def run():
    command.mute_commmands_function(bot, commands)
    command.chat_herlpers_function(bot, commands)
    command.music_comands_function(bot)    
    command.level_function(bot, commands)
    @bot.event
    async def on_member_join(member):
        guild = member.guild
        role = member.guild.get_role(1336784590232354848)
        await member.add_roles(role)
        print(f"{member.name} get {role.name}")


    #Запуск бота
    bot.run(TOKEN)