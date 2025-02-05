import discord
from discord.ext import commands
import asyncio
#
TOKEN = "YOUR TOKEN"
PREFIX = "/"
intents = discord.Intents().default()
intents.message_content = True
#Создаємо бота
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

#Команда мьюта
@bot.command()
async def mute(ctx, member: discord.Member):
    #Отримуваємо роль
    role = ctx.guild.get_role(1336785765434392637)
    #Добовляємо роль
    await member.add_roles(role)
    #Відпровляємо повідомлення
    await ctx.reply(f"{member.name} теперь стал unsigma!")

#Команда размьюта
@bot.command()
async def unmute(ctx, member: discord.Member):
    #Отримуваємо роль
    role = ctx.guild.get_role(1336785765434392637)
    #Видаляємо роль
    await member.remove_roles(role)
    #Відпровляємо повідомлення
    await ctx.reply(f"{member.name} теперь стал sigma!")

#Запуск бота
bot.run(TOKEN)