import os
import disnake
from disnake.ext import commands
from dotenv import load_dotenv

load_dotenv('.env', verbose=True)

bot = commands.InteractionBot(sync_commands_debug=True)

bot.invite_url = 'https://discord.com/api/oauth2/authorize?client_id=774679887101427713&permissions=8&scope=bot'
bot.server_url = 'https://discord.gg/UPtQtvk'


@bot.event
async def on_ready():
    print(f'{bot.user} is online.')
    await bot.change_presence(activity=disnake.Game(f'The Umbrella Academy.'))
    print(f'{await bot.application_info()}')
    print(type(await bot.application_info()))
    print(bot.owner)


def load_the_cogs():
    for file in os.listdir("cogs"):
        if file.endswith(".py"):
            try:
                bot.load_extension(f"cogs.{file[:-3]}")
            except disnake.ext.commands.errors.NoEntryPointError as e:
                print(e)


load_the_cogs()

bot.run(os.getenv('TOKEN'))
