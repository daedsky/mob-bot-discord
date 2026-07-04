import disnake
from disnake.ext import commands
import os


class Owner(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.is_owner()
    @commands.slash_command(guild_ids=[765870385979195412])
    async def logout(self, ctx):
        await ctx.send(embed=disnake.Embed(description="Logged out! Now I'm offline."))
        await self.bot.close()

    @commands.is_owner()
    @commands.slash_command(guild_ids=[765870385979195412])
    async def change_status(self, ctx: disnake.ApplicationCommandInteraction, mode=None, *, desc=None):
        guilds = self.bot.guilds
        if not desc:
            desc = f'Mob help | in {len(guilds)} servers'
        if mode == 'dnd':
            await self.bot.change_presence(activity=disnake.Game(desc), status=disnake.Status.dnd)
            await ctx.author.send('changed presence successfully')
        elif mode == 'online':
            await self.bot.change_presence(activity=disnake.Game(desc), status=disnake.Status.online)
            await ctx.author.send('changed presence successfully')
        elif mode == 'idle':
            await self.bot.change_presence(activity=disnake.Game(desc), status=disnake.Status.idle)
            await ctx.author.send('changed presence successfully')
        elif mode == 'streaming':
            await self.bot.change_presence(activity=disnake.Game(desc), status=disnake.Status.streaming)
            await ctx.author.send('changed presence successfully')
        elif mode == 'invisible':
            await self.bot.change_presence(activity=disnake.Game(desc), status=disnake.Status.invisible)
            await ctx.author.send('changed presence successfully')
        elif mode == 'offline':
            await self.bot.change_presence(activity=disnake.Game(desc), status=disnake.Status.offline)
            await ctx.author.send('changed presence successfully')

    @commands.is_owner()
    @commands.slash_command(guild_ids=[765870385979195412])
    async def load(self, ctx: disnake.ApplicationCommandInteraction, extension):
        self.bot.load_extension(f'cogs.{extension}')
        await ctx.author.send(f'successfully loaded {extension}')

    @commands.is_owner()
    @commands.slash_command(guild_ids=[765870385979195412])
    async def unload(self, ctx, extension):
        self.bot.unload_extension(f"cogs.{extension}")
        await ctx.author.send(f"successfully unloaded {extension}")

    @commands.is_owner()
    @commands.slash_command(guild_ids=[765870385979195412])
    async def reload(self, ctx, extension):
        self.bot.reload_extension(f"cogs.{extension}")
        await ctx.author.send(f"successfully reloaded {extension}")

    @commands.is_owner()
    @commands.slash_command(guild_ids=[765870385979195412])
    async def reload_all_cogs(self, ctx):
        for file in os.listdir("cogs"):
            if file.endswith(".py"):
                self.bot.reload_extension(f"cogs.{file[:-3]}")
        ctx.author.send("All cogs reload successfully.")


def setup(bot):
    bot.add_cog(Owner(bot))
