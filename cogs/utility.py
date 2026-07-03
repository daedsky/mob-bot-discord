import disnake
from disnake.ext import commands
import qrcode
import requests


class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.randomcolor = disnake.Colour.random

    @commands.slash_command(dm_permission=False)
    @commands.check_any(commands.has_permissions(manage_nicknames=True), commands.has_permissions(administrator=True))
    async def nickname(self, ctx, user: disnake.Member, name: str):
        """Change the nickname of the person in server"""
        await user.edit(nick=name)
        embed = disnake.Embed(description=f"{user.name}'s nickname changed to {name}",
                              color=disnake.colour.Colour.random())
        await ctx.send(embed=embed)

    @nickname.error
    async def nickname_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            embed = disnake.Embed(description="You need `manage nicknames` permission to run this command.",
                                  color=disnake.Colour.random())
            await ctx.send(embed=embed)

    @commands.slash_command()
    async def qr(self, ctx, text, fill_color='black', bg_color='white'):
        """Generates qr code of provided text"""
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=2,
        )
        qr.add_data(text)
        qr.make(fit=True)

        img = qr.make_image(fill_color=fill_color, back_color=bg_color)
        img.save('images/qr.png')

        file = disnake.File('images/qr.png')
        await ctx.send(file=file)

    @commands.has_permissions(manage_emojis=True)
    @commands.slash_command(dm_permission=False)
    async def add_emoji(self, ctx, emoji_name: str, image_url: str):
        """Add an emoji to the server by providing the emoji image/gif url"""
        emj = requests.get(image_url).content

        emoji = await ctx.guild.create_custom_emoji(name=emoji_name, image=emj)
        await ctx.send(embed=disnake.Embed(description=f'successfully add <:{emoji.name}:{emoji.id}> to the server.',
                                           color=disnake.Colour.green()))


def setup(bot):
    bot.add_cog(Utility(bot))
