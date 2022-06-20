import disnake
from disnake.ext import commands
import requests
from core_functions import ImageFunctions, getdetails_for_details_command
import core_functions


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.randomcolor = disnake.Color.random

    @staticmethod
    async def get_img_url(ctx, args):
        try:
            user = await commands.MemberConverter().convert(ctx, args)
            img_url = user.avatar.url
        except commands.MemberNotFound:
            img_url = args

        return img_url

    @commands.slash_command()
    async def captcha(self, ctx, text):
        """generate a captcha using your text"""
        await ImageFunctions.captcha(text, 'images/captcha.png')
        await ctx.send(file=disnake.File('images/captcha.png'))

    @commands.slash_command()
    async def did_you_mean(self, ctx, search_text, suggestion_text):
        """generate a google search did you mean? image"""
        await ImageFunctions.did_you_mean(search_text, suggestion_text, 'images/did_you_mean.png')
        await ctx.send(file=disnake.File('images/did_you_mean.png'))

    @commands.slash_command()
    async def sketch(self, ctx, usr_or_img_url):
        """Sketch image without colors"""
        await core_functions.think(ctx)
        try:
            img_url = await self.get_img_url(ctx, usr_or_img_url)
            r = requests.get(img_url)
            with open("images/pencil_avatar.png", "wb") as f:
                f.write(r.content)

            await ImageFunctions.pencil("images/pencil_avatar.png", 'images/pencil_output.png')

            embed = disnake.Embed(title="Pencil sketch", color=self.randomcolor())
            embed.set_image(url="attachment://sketch.png")
            embed.set_footer(text=f"Rendered by {ctx.author}")
            file = disnake.File("images/pencil_output.png", filename="sketch.png")
            await ctx.edit_original_message('', embed=embed, file=file)

        except requests.RequestException:
            await ctx.edit_original_message('',
                                            embed=disnake.Embed(description='Invalid image url',
                                                                color=self.randomcolor()))

    @commands.slash_command()
    async def colorsketch(self, ctx, usr_or_img_url):
        """Sketch image with colors."""
        await core_functions.think(ctx)
        try:
            img_url = await self.get_img_url(ctx, usr_or_img_url)
            r = requests.get(img_url)
            with open("images/sketch_avatar.png", "wb") as f:
                f.write(r.content)

            await ImageFunctions.colored_ketch("images/sketch_avatar.png", 'images/coloured_sketch.png')

            embed = disnake.Embed(title="Coloured sketch", color=self.randomcolor())
            embed.set_image(url="attachment://coloured_sketch.png")
            embed.set_footer(text=f"Rendered by {ctx.author}")
            file = disnake.File("images/coloured_sketch.png", filename="coloured_sketch.png")
            await ctx.edit_original_message('', embed=embed, file=file)

        except requests.RequestException:
            await ctx.edit_original_message('', embed=disnake.Embed(description='Invalid image url',
                                                                    color=self.randomcolor()))

    @commands.slash_command()
    async def paise_barbad(self, ctx, *, text):
        """Create a paise barbad meme"""
        await core_functions.think(ctx)
        await ImageFunctions.paise_barbad_bc(text, "images/paisa_barbad.png")

        embed = disnake.Embed(title="Paise barbad bahenchod",
                              color=disnake.Colour.orange()).set_image(url="attachment://paisa_barbad.png")
        file = disnake.File("images/paisa_barbad.png", filename="paisa_barbad.png")
        await ctx.edit_original_message('', embed=embed, file=file)

    @commands.slash_command()
    async def canny(self, ctx, usr_or_img_url):
        """Convert the image or avatar of user to canny image"""
        await core_functions.think(ctx)
        try:
            img_url = await self.get_img_url(ctx, usr_or_img_url)
            r = requests.get(img_url)
            with open("images/canny_avatar.png", "wb") as f:
                f.write(r.content)

            await ImageFunctions.canny("images/canny_avatar.png", 'images/canny.png')

            embed = disnake.Embed(color=self.randomcolor(), title="Canny Image")
            embed.set_image(url="attachment://canny.png")
            embed.set_footer(text=f"Rendered by {ctx.author}")
            file = disnake.File("images/canny.png", filename="canny.png")
            await ctx.edit_original_message('', embed=embed, file=file)

        except requests.RequestException:
            await ctx.edit_original_message('', embed=disnake.Embed(description='Invalid image url',
                                                                    color=self.randomcolor()))

    @commands.slash_command()
    async def trump(self, ctx, *, text):
        """Make trump tweet your words"""
        await core_functions.think(ctx)
        await ImageFunctions.trump(text, "images/trump.png")
        embed = disnake.Embed(title="Donald Trump tweeted", color=self.randomcolor())
        embed.set_image(url="attachment://trump.png")

        file = disnake.File("images/trump.png", filename="trump.png")

        await ctx.edit_original_message('', embed=embed, file=file)

    @commands.slash_command()
    async def brazzers(self, ctx, usr_or_img_url):
        """Add brazzers logo to the provided image url or avatar of a member"""
        await core_functions.think(ctx)
        try:
            img_url = await self.get_img_url(ctx, usr_or_img_url)
            r = requests.get(img_url)
            with open("images/brazzers_avatar.png", "wb") as f:
                f.write(r.content)

            await ImageFunctions.brazzers("images/brazzers_avatar.png", "images/brazzers.png")

            embed = disnake.Embed(color=self.randomcolor())
            embed.set_image(url="attachment://brazzers.png")
            file = disnake.File("images/brazzers.png", filename="brazzers.png")
            await ctx.edit_original_message('', embed=embed, file=file)

        except requests.RequestException:
            await ctx.edit_original_message('', embed=disnake.Embed(description='Invalid image url',
                                                                    color=self.randomcolor()))

    @commands.slash_command()
    async def ship(self, ctx, usr1_or_img_url, usr2_or_img_url):
        """Ship two users together"""
        await core_functions.think(ctx)
        try:
            img1_url = await self.get_img_url(ctx, usr1_or_img_url)
            r1 = requests.get(img1_url)
            with open("images/ship_avatar1.png", "wb") as f1:
                f1.write(r1.content)

            img2_url = await self.get_img_url(ctx, usr2_or_img_url)
            r2 = requests.get(img2_url)
            with open("images/ship_avatar2.png", "wb") as f2:
                f2.write(r2.content)

            await ImageFunctions.ship("images/ship_avatar1.png", "images/ship_avatar2.png", "images/ship.png")

            embed = disnake.Embed()
            embed.set_image(url="attachment://ship.png")
            file = disnake.File("images/ship.png", "ship.png")
            await ctx.edit_original_message('', embed=embed, file=file)

        except requests.RequestException:
            await ctx.edit_original_message('', embed=disnake.Embed(description='Invalid image url',
                                                                    color=self.randomcolor()))

    @commands.slash_command()
    async def drake(self, ctx, text1, text2):
        """Create a drake meme"""
        await core_functions.think(ctx)
        await ImageFunctions.drake(text1, text2, "images/drake.png")

        embed = disnake.Embed(title="Drake", color=self.randomcolor())
        embed.set_image(url="attachment://drake.png")
        file = disnake.File("images/drake.png", filename="drake.png")
        await ctx.edit_original_message('', embed=embed, file=file)

    @commands.slash_command()
    async def motivation(self, ctx, *, text):
        """Create a motivation meme"""
        await core_functions.think(ctx)
        await ImageFunctions.write_motivation(text, "images/motivation.png")

        embed = disnake.Embed(title="Motivation", color=self.randomcolor())
        embed.set_image(url="attachment://motivation.png")
        file = disnake.File("images/motivation.png", filename="motivation.png")
        await ctx.edit_original_message('', embed=embed, file=file)

    @commands.slash_command()
    async def whathow(self, ctx, usr_or_img_url):
        """Create a whathow meme"""
        await core_functions.think(ctx)
        try:
            img_url = await self.get_img_url(ctx, usr_or_img_url)
            r = requests.get(img_url)
            with open("images/whathow_avatar.png", "wb") as f:
                f.write(r.content)

            await ImageFunctions.whathow("images/whathow_avatar.png", "images/whathow.png")

            embed = disnake.Embed(title="What? How?", color=self.randomcolor()).set_image(
                url="attachment://whathow.png")
            file = disnake.File("images/whathow.png", filename="whathow.png")
            await ctx.edit_original_message('', embed=embed, file=file)

        except requests.RequestException:
            await ctx.edit_original_message('', embed=disnake.Embed(description='Invalid image url',
                                                                    color=self.randomcolor()))

    @commands.slash_command()
    async def meme(self, ctx, amount: int = 1, subreddit='memes'):
        """Get some memes"""
        await core_functions.think(ctx)
        subreddit_is_nsfw = await core_functions.is_subreddit_nsfw(subreddit)
        if subreddit_is_nsfw and not ctx.channel.is_nsfw():
            await ctx.edit_original_message('', embed=disnake.Embed(
                description="You dickhead! this is not a nsfw channel.",
                color=self.randomcolor()))
        else:
            await core_functions.send_praw_posts(ctx, subreddit, amount)

    @commands.slash_command()
    async def details(self, ctx, user: disnake.Member):
        """Get the fake details of someone"""
        await core_functions.think(ctx)

        title, fullname, email, phno, pswd, status, networth, profession = getdetails_for_details_command(user)

        r = requests.get(user.display_avatar.url)
        with open("images/detail_avatar.png", "wb") as f:
            f.write(r.content)

        await ImageFunctions.detailscard(avatar="images/detail_avatar.png", name=fullname, email=email, pswd=pswd,
                                         phno=phno,
                                         virginstatus=status, networth=networth, profession=profession,
                                         save_to="images/detailCard.png")

        # em = disnake.Embed(title=title, color=disnake.colour.Colour.random())
        # em.set_image(url="attachment://detailCard.png")

        file = disnake.File("images/detailCard.png", filename="detailCard.png")
        await ctx.edit_original_message('', file=file)

    @commands.slash_command()
    async def giftnitro(self, ctx, user: disnake.Member):
        """Gift someone a fake nitro"""
        await core_functions.think(ctx)
        url = f"https://i.redd.it/a9ng95vvs8c41.png"

        em = disnake.Embed(title="Here Is Your Nitro", color=disnake.colour.Colour.random())
        em.set_image(url=url)
        await ctx.edit_original_message(user.mention, embed=em)

    @commands.slash_command()
    async def write(self, ctx, *, text):
        """Handwriting with your text"""
        await core_functions.think(ctx)
        rgb = (0, 0, 138)
        data = requests.get(
            f"https://pywhatkit.herokuapp.com/handwriting?text={text}&rgb={rgb[0]},{rgb[1]},{rgb[2]}").content

        with open('images/text_to_handwriting.png', "wb") as f:
            f.write(data)

        file = disnake.File('images/text_to_handwriting.png')
        await ctx.edit_original_message('', file=file)

    @commands.slash_command()
    async def echo(self, ctx, *, text):
        """Echos your text"""
        await core_functions.think(ctx)
        await ctx.edit_original_message(text)

    @commands.slash_command()
    async def pokemon(self, ctx, pokemon_name):
        """Get the image of a pokemon"""
        await core_functions.think(ctx)
        name = f"pokemon {pokemon_name}"
        url = f"https://i.some-random-api.ml/pokemon/{pokemon_name}.png"
        if requests.get(url).status_code == 200:
            em = disnake.Embed(title=name, color=disnake.colour.Colour.random())
            em.set_image(url=url)
            em.set_footer(text=f"Requested by {ctx.author.name}")
            await ctx.edit_original_message('', embed=em)
        else:
            await ctx.edit_original_message('', embed=disnake.Embed(
                description='This pokemon does not exists or check your spelling.'))


def setup(bot):
    bot.add_cog(Fun(bot))
