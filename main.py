import asyncio

from discord.ext.commands import Bot

bot = Bot(command_prefix="b", self_bot=True, chunk_guilds_at_startup=False)

TOKEN = "MTEwODY2NDU5NTA0NTk0OTU0MQ.GDrr87.4f48nIV46FKUhvc-7ZRjNbnr9LqFYXWvoRPcw8"
LOG_CHANNEL = 1166688091642273883
CHANNEL_IDS = [1063027190238818304, 1057293896801079416, 1150840909328552058, 1096798254437498920]

@bot.event
async def on_ready():
    print("Logged in!")

    bot.loop.create_task(auto())

async def auto():
    while True:
        await asyncio.sleep(10)
        channels = CHANNEL_IDS
        for channel in channels:
          log_channel = bot.get_channel(LOG_CHANNEL)
          await log_channel.send(f"## `Sent bump command to {channel.guild.name}`\n> `Server ID - {channel.guild.id}`\n> `Channel ID - {channel}`")

@bot.command()
async def ump(ctx):
  channel = bot.get_channel(ctx.channel.id)
  async for command in channel.slash_commands():
    if command.name == "bump":
       await command(channel)
       await asyncio.sleep(10)

bot.run(TOKEN)
