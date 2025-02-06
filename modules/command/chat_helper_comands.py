import discord

def chat_herlpers_function(bot, commands):
    @bot.command()
    @commands.has_permissions(administrator=True)
    async def role(ctx, member: discord.Member, role: discord.Role):
        rrole = ctx.guild.get_role(role.id)
        await member.add_roles(rrole)
        await ctx.reply(f"print({member.name} заробив роль {role.name}!)")
    @bot.command()
    @commands.has_permissions(administrator=True)
    async def clear(ctx, amount: int):
        deleted = await ctx.channel.purge(limit=amount + 1)
        await ctx.send(f"Видалено {len(deleted) - 1} повідомлень.")
        print(f"Del-{len(deleted) - 1} sms")    