import disnake
from disnake.ext import commands


class Owner(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.is_owner()
    @commands.slash_command(guild_ids=[840468981551071232])
    async def logout(self, ctx):
        await ctx.send(embed=disnake.Embed(description="Logged out! Now I'm offline."))
        await self.bot.close()

    @commands.is_owner()
    @commands.slash_command(guild_ids=[840468981551071232])
    async def botguilds(self, ctx):
        guilds = self.bot.guilds
        Guilds = [f"{x.name} | id: {x.id}" for x in guilds]
        await ctx.send(Guilds)

    @commands.is_owner()
    @commands.slash_command(guild_ids=[840468981551071232])
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


def setup(bot):
    bot.add_cog(Owner(bot))
