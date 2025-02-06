import discord, ffmpeg, yt_dlp, asyncio

def music_comands_function(bot):
    @bot.command()
    async def play(ctx, url: str):
        if not ctx.author.voice:
            await ctx.send("Ти не у войсі😑")
            return

        voice_channel = ctx.author.voice.channel
        voice_client = ctx.voice_client 

        if voice_client:
            if voice_client.channel != voice_channel:
                await voice_client.move_to(voice_channel)
        else: 
            voice_client = await voice_channel.connect()

        ydl_opts = {
            'format': 'bestaudio/best',
            'noplaylist': True,
            'quiet': True,
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(url, download=False)
                audio_url = info_dict['url']

            ffmpeg_options = {
                'options': '-vn'
            }
            player = discord.FFmpegOpusAudio(audio_url, executable="C:/ffmpeg/bin/ffmpeg.exe", **ffmpeg_options)
            voice_client.play(player, after=lambda e: print(f'Player error: {e}') if e else None) 

            await ctx.send(f"Зараз грає: {info_dict['title']}")

        except Exception as e:
            print(f"Помилка: {str(e)}")
            if voice_client:
                await voice_client.disconnect()

    @bot.command(name="stop")
    async def stop(ctx):
        voice_client = ctx.voice_client
        if voice_client:
            voice_client.stop() 
            await voice_client.disconnect()
            await ctx.send("Виходжу... 😔")
        else:
            await ctx.send("Мене там немає 😑")

    @bot.command(name='pause')
    async def pause(ctx):
        voice_client = ctx.voice_client
        if voice_client and voice_client.is_playing():
            voice_client.pause()
            await ctx.send("⏸️")  
        elif voice_client and voice_client.is_paused():
            await ctx.send("Spamer😡")
        else:
            await ctx.send("Ти не у войсі😑")

    @bot.command(name='resume')
    async def resume(ctx):
        voice_client = ctx.voice_client
        if voice_client and voice_client.is_paused(): 
            voice_client.resume()
            await ctx.send("▶️")  
        elif voice_client and voice_client.is_playing():
            await ctx.send("Spamer😡")
        else:
            await ctx.send("Ти не у войсі😑")

    @bot.event
    async def on_voice_state_update(member, before, after):
        if member == bot.user:
            voice_client = before.channel.guild.voice_client if before.channel else None
            if voice_client and not after.channel:
                await voice_client.disconnect()

