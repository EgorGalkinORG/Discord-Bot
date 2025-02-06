import asyncio
import discord

def mute_commmands_function(bot, commands):
    #Команда размьюта
    @bot.command()
    @commands.has_permissions(administrator=True)
    async def unmute(ctx, member: discord.Member):
        #Отримуваємо роль
        role = ctx.guild.get_role(1336785765434392637)
        #Видаляємо роль
        await member.remove_roles(role)
        #Відпровляємо повідомлення
        await ctx.reply(f"print({member.name} зараз став sigma!)")
    #Команда мьюта
    @bot.command()
    @commands.has_permissions(administrator=True)
    async def mute(ctx, member: discord.Member):
        #Отримуваємо роль
        role = ctx.guild.get_role(1336785765434392637)
        #Добовляємо роль
        await member.add_roles(role)
        #Відпровляємо повідомлення
        await ctx.reply(f"print({member.name} зараз став unsigma!)")
        await asyncio.sleep(300) if True else None
        await member.remove_roles(role)
        await ctx.reply(f"print({member.name} зараз став sigma!)")