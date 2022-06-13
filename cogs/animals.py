import disnake
from disnake.ext import commands
import core_functions


class Animals(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def fox(self, ctx, amount: int = 1):
        """Get some fox images"""
        await core_functions.send_praw_posts(ctx, 'fox', amount)

    @commands.slash_command()
    async def dogs(self, ctx, amount: int = 1):
        """Get some dog pictures"""
        await core_functions.send_praw_posts(ctx, 'DOG+PuppySmiles', amount)

    @commands.slash_command()
    async def cats(self, ctx, amount: int = 1):
        """Get cat pics"""
        await core_functions.send_praw_posts(ctx, 'cat+cats+catpics', amount)

    @commands.slash_command()
    async def cute(self, ctx, subreddit, amount: int = 1):
        """Get pics of the animal"""
        is_nsfw = await core_functions.is_subreddit_nsfw(subreddit)
        if is_nsfw and not ctx.channel.is_nsfw():
            await ctx.edit_original_message('', embed=disnake.Embed(
                description="You dickhead! this is not a nsfw channel.",
                color=disnake.Colour.random()))
        else:
            await core_functions.send_praw_posts(ctx, subreddit, amount)


def setup(bot):
    bot.add_cog(Animals(bot))
