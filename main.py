import asyncio
from discord.ext.commands import Bot
from random import randint

bot = Bot(command_prefix="b", self_bot=True, chunk_guilds_at_startup=False)

TOKEN = "YOUR TOKEN"
LOG_CHANNEL = "YOUR LOG CHANNEL" # Put the channel id without quotation marks
CHANNEL_IDS = []

@bot.event
async def on_ready():
    print("Logged in!")
    bot.loop.create_task(auto())

async def auto():
    while True:
        channels = CHANNEL_IDS
        for channel_id in channels:
            channel = bot.get_channel(channel_id)
            if channel:
                log_channel = bot.get_channel(LOG_CHANNEL)
                await log_channel.send(f"```Sent bump command!\nChannel ID: {channel_id}```")
                await channel.send("bump")
                await asyncio.sleep(randint(1800, 1820))  # wait after each message
        await asyncio.sleep(randint(7200, 7220))  # wait after each round of messages

@bot.command()
async def ump(ctx):
    channel = bot.get_channel(ctx.channel.id)
    async for command in channel.slash_commands():
        if command.name == "bump":
            await command(channel)
            await asyncio.sleep(60)

bot.run(TOKEN)
