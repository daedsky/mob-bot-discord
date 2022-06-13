from disnake.ext import commands
import core_functions


class Nsfw(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @staticmethod
    async def think(ctx):
        await ctx.send('Mob bot is thinking...')

    @commands.slash_command()
    async def boobs(self, ctx, amount: int = 1):
        await self.think(ctx)
        if not ctx.channel.is_nsfw():
            await ctx.edit_original_message('You cock sucker This is not a nsfw channel')
        elif amount > 20:
            await ctx.edit_original_message('❌Try a num less than 20')
        else:
            await core_functions.send_praw_posts(ctx, 'boobs', amount)

    @commands.slash_command()
    async def pussy(self, ctx, amount: int = 1):
        await self.think(ctx)
        if not ctx.channel.is_nsfw():
            await ctx.edit_original_message('You cock sucker This is not a nsfw channel')
        elif amount > 20:
            await ctx.edit_original_message('❌ Try a num less than 20')
        else:
            await core_functions.send_praw_posts(ctx, 'pussy', amount)

    @commands.slash_command()
    async def ass(self, ctx, amount: int = 1):
        await self.think(ctx)
        if not ctx.channel.is_nsfw():
            await ctx.edit_original_message('You cock sucker This is not a nsfw channel')
        elif amount > 20:
            await ctx.edit_original_message('❌ Try a num less than 20')
        else:
            await core_functions.send_praw_posts(ctx, 'ass', amount)

    @commands.slash_command()
    async def booty(self, ctx, amount: int = 1):
        await self.think(ctx)
        if not ctx.channel.is_nsfw():
            await ctx.edit_original_message('You cock sucker This is not a nsfw channel')
        elif amount > 20:
            await ctx.edit_original_message('❌ Try a num less than 20')
        else:
            await core_functions.send_praw_posts(ctx, 'booty', amount)

    @commands.slash_command()
    async def nsfw(self, ctx, amount: int = 1, *, subredit='nsfw'):
        if not ctx.channel.is_nsfw():
            await ctx.edit_original_message('You cock sucker This is not a nsfw channel')
        elif amount > 20:
            await ctx.edit_original_message('❌Try a num less than 20')
        else:
            await core_functions.send_praw_posts(ctx, subredit, amount)

    @commands.slash_command()
    async def nudes(self, ctx, amount: int = 1):
        await self.think(ctx)
        if not ctx.channel.is_nsfw():
            await ctx.edit_original_message('You cock sucker This is not a nsfw channel')
        elif amount > 20:
            await ctx.edit_original_message('❌ Try a num less than 20')
        else:
            await core_functions.send_praw_posts(ctx, 'nudes', amount)


def setup(bot):
    bot.add_cog(Nsfw(bot))
