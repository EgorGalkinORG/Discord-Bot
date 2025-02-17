import discord, requests
from bs4 import BeautifulSoup

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
        deleted = await ctx.channel.purge(limit = amount + 1)
        await ctx.send(f"Видалено {len(deleted) - 1} повідомлень.")
        print(f"Del-{len(deleted) - 1} sms") 
    @bot.command()       
    async def project(ctx, link: str):
        response = requests.get(link)
        await ctx.message.delete()
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            readme_link = link + "/blob/main/README.md"

            project_name_tag = soup.find("strong", class_="mr-2 flex-self-stretch")
            project_name = project_name_tag.text.strip() if project_name_tag else "Ім'я проекту не знайдено"

            avatar_tag = soup.find("meta", {"property": "og:image"})
            owner_avatar = avatar_tag["content"] if avatar_tag else "Аватар не найден"

            await ctx.send(f"*Назва проекта:* **{project_name}**\n*Посилання на README:* **{readme_link}**\n**ДЯКУЄМО ЗА РАБОТУ**")
            await ctx.send(owner_avatar)
        else:
            await ctx.send("Помилка")

        
