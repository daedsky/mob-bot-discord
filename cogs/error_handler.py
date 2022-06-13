import disnake
from disnake.ext import commands


class ErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = disnake.Embed(description="You do not have permission to run this command.",
                                  color=disnake.Colour.random())
            await ctx.send(embed=embed)
        elif isinstance(error, commands.NSFWChannelRequired):
            embed = disnake.Embed(description="You need to run this command in NSFW channels only.",
                                  color=disnake.Colour.random())
            await ctx.send(embed=embed)
        elif isinstance(error, commands.CommandNotFound):
            await ctx.send(embed=disnake.Embed(description=f"command not found",
                                               color=disnake.Colour.random()))

        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.author.send(
                embed=disnake.Embed(description="""Hey! I am missing permissions to perform the action."""))

        elif isinstance(error, commands.NotOwner):
            pass

        elif isinstance(error, commands.errors.MemberNotFound):
            await ctx.send(embed=disnake.Embed(description="Member not found"))

        else:
            err = str(error)
            if "disnake.errors.Forbidden" in err:
                print(error)
            else:
                print(type(error))
                raise error


def setup(bot):
    bot.add_cog(ErrorHandler(bot))
