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
        total_channels = len(channels)
        
        # Loop through each channel to bump
        for channel_id in channels:
            if channel := bot.get_channel(channel_id):
                if LOG_CHANNEL:
                    log_channel = bot.get_channel(LOG_CHANNEL)
                    await log_channel.send(f"```Sent bump command!\nChannel ID: {channel_id}\nGuild: {channel.guild}```")
                
                await channel.send("?bump")
                await asyncio.sleep(randint(1800, 1820))  # Wait for 30 minutes between each bump
        
        # Calculate remaining time to ensure the total time for one round is 2 hours (7200 seconds) [ I am not sure if this will work or not I will test and add a better fix ]
        total_bump_time = 1800 * total_channels  # Total time spent bumping all channels
        remaining_time = max(0, 7200 - total_bump_time)  # Remaining time to make the total 2 hours
        
        await asyncio.sleep(remaining_time)

@bot.command()
async def bump(ctx):
    channel = bot.get_channel(ctx.channel.id)
    application_commands = await channel.application_commands()
    for command in application_commands:
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
