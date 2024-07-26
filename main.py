import asyncio
from discord.ext.commands import Bot
from random import randint

bot = Bot(command_prefix="?", self_bot=True, chunk_guilds_at_startup=False)

TOKEN = "YOUR TOKEN"
LOG_CHANNEL = "YOUR LOG CHANNEL ID" # OPTIONAL - Put the channel ID without quotation marks
CHANNEL_IDS = []

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    bot.loop.create_task(auto())

async def auto():
    while True:
        channels = CHANNEL_IDS
        for channel_id in channels:
            if channel := bot.get_channel(channel_id):
                if LOG_CHANNEL:
                    log_channel = bot.get_channel(LOG_CHANNEL)
                    await log_channel.send(f"```Sent bump command!\nChannel ID: {channel_id}\nGuild: {channel.guild}```")
                await channel.send("?bump")
                await asyncio.sleep(randint(1800, 1820)) # wait after each message
        await asyncio.sleep(randint(7200, 7220)) # wait after each round of messages

@bot.command()
async def bump(ctx):
    channel = bot.get_channel(ctx.channel.id)
    application_commands = await channel.application_commands()
    for command in application_commands:
        # Note: With these conditions it will only send the Disboard bump command if you want it to send other bump commands too you may remove the other conditions. Something like `if command.name == "bump":` but it might not work properly always! Also different bots have different cool down times.
        
        if command.name == "bump" and (
            command.application_id == 302050872383242240
            or command.id == 1252409457757913260
        ):
            await command(channel)
            await asyncio.sleep(60)

@bot.command()
async def bing(ctx):
    print("Command input detected. Bot is running!")
    await ctx.send(f"Bong!\nLatency {round(bot.latency * 1000)}ms")

bot.run(TOKEN)