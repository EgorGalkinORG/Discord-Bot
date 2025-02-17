import os, json, discord
def level_function(bot, commands):
    if os.path.exists("static/json/xp_data.json"):
        with open("static/json/xp_data.json", "r") as f:
            xp_data = json.load(f)
    else:
        xp_data = {}
    @bot.event
    async def on_message(message):
        if message.author.bot:
            return
    
        user_id = str(message.author.id)
    
        if user_id not in xp_data:
            xp_data[user_id] = {"xp": 0, "level": 1}
    
        xp_data[user_id]["xp"] += 1
    
        if xp_data[user_id]["xp"] >= 5000 * xp_data[user_id]["level"]:
            xp_data[user_id]["xp"] = 0
            xp_data[user_id]["level"] += 1
            await message.channel.send(f"🎉 {message.author.mention}, ти підвищив рівень до {xp_data[user_id]['level']}!")
    
        with open("static/json/xp_data.json", "w") as f:
            json.dump(xp_data, f, indent=4)
    
        await bot.process_commands(message)

    @bot.command()
    async def level(ctx):
        user_id = str(ctx.author.id)
        user = ctx.author
        role = ctx.guild.get_role(1341119335434813515)
        if role in user.roles:
            active = "Активний!🟩"
        else:
            active = "не активний⬛..."
        level = xp_data.get(user_id, {}).get("level", 1)
        xp = 5000 * xp_data[user_id]["level"] - int(xp_data[user_id]["xp"])
        await ctx.send(f"🔹 {ctx.author.mention}, твiй рiвень: {level}! Git активність: {active}\nДо наступного рівня {xp} досвіду")

    @bot.command()
    @commands.has_permissions(administrator=True)
    async def give_xp(ctx, member : discord.Member, amount: int):
        user_id = str(member.id)
        if user_id not in xp_data:
            xp_data[user_id] = {"xp": 0, "level": 1}
        
        xp_data[user_id]["xp"] += amount
        await ctx.reply("Додано!")

        if xp_data[user_id]["xp"] >= 5000 * xp_data[user_id]["level"]:
            xp_data[user_id]["xp"] = 0
            xp_data[user_id]["level"] += 1
            await ctx.channel.send(f"🎉 {ctx.author.mention}, ти підвищив рівень до {xp_data[user_id]['level']}!")

    @bot.command()
    @commands.has_permissions(administrator=True)
    async def add_level(ctx, member : discord.Member):
        xp_data[str(member.id)]["level"] += 1

    @bot.command()
    @commands.has_permissions(administrator=True)
    async def del_xp(ctx, member : discord.Member, amount: int):
        user_id = str(member.id)
        if user_id not in xp_data:
            xp_data[user_id] = {"xp": 0, "level": 1}
        
        xp_data[user_id]["xp"] -= amount

        if xp_data[user_id]["xp"] <= -1:
            xp_data[user_id]["xp"] = 0
            xp_data[user_id]["level"] -= 1
            await ctx.channel.send(f"🎉 {ctx.author.mention}, ти мабуть дуже поганий, 😡:point_right: в тебе {xp_data[user_id]['level']} рівень!")