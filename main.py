import os
import disnake
from disnake.ext import commands

bot = commands.InteractionBot(sync_commands_debug=True)

bot.invite_url = ''
bot.server_url = ''

@bot.event
async def on_ready():
    print(f'{bot.user} is online.')
    await bot.change_presence(activity=disnake.Game(f'The Umbrella Academy.'))
    print(f'{await bot.application_info()}')
    print(type(await bot.application_info()))
    print(bot.owner)


@commands.is_owner()
@commands.slash_command(guild_ids=[840468981551071232])
async def load(ctx: disnake.ApplicationCommandInteraction, extension):
    bot.load_extension(f'cogs.{extension}')
    await ctx.author.send(f'successfully loaded {extension}')


@commands.is_owner()
@bot.slash_command(guild_ids=[840468981551071232])
async def unload(ctx, extension):
    bot.unload_extension(f"cogs.{extension}")
    await ctx.author.send(f"successfully unloaded {extension}")


@commands.is_owner()
@bot.slash_command(guild_ids=[840468981551071232])
async def reload(ctx, extension):
    bot.reload_extension(f"cogs.{extension}")
    await ctx.author.send(f"successfully reloaded {extension}")


@commands.is_owner()
@bot.slash_command(guild_ids=[840468981551071232])
async def reload_all_cogs(ctx):
    for file in os.listdir("cogs"):
        if file.endswith(".py"):
            bot.reload_extension(f"cogs.{file[:-3]}")
    ctx.author.send("All cogs reload successfully.")


def load_the_cogs():
    for file in os.listdir("cogs"):
        if file.endswith(".py"):
            bot.load_extension(f"cogs.{file[:-3]}")


load_the_cogs()

bot.run(os.getenv('TOKEN'))
