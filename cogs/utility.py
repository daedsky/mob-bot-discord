import os
import disnake
from disnake.ext import commands
import qrcode
import requests
from bs4 import BeautifulSoup
import wikipedia
import core_functions


class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.randomcolor = disnake.Colour.random

    @commands.slash_command(name="reddit")
    async def __reddit(self, ctx, subreddit, amount: int = 1):
        """Gives a post from the specified subreddit."""
        is_nsfw = await core_functions.is_subreddit_nsfw(subreddit)
        if is_nsfw and not ctx.channel.is_nsfw():
            await ctx.edit_original_message('', embed=disnake.Embed(
                description="You dickhead! this is not a nsfw channel.",
                color=disnake.Colour.random()))
        else:
            await core_functions.send_praw_posts(ctx, subreddit, amount)

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
    async def qr(self, ctx, text, fill_color= 'black', bg_color = 'white'):
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
        img.save('temp/qr.png')

        file = disnake.File('temp/qr.png')
        await ctx.send(file=file)

    @commands.slash_command()
    async def image(self, ctx, query):
        """Get the image of the specified person or thing"""
        await core_functions.think(ctx)
        try:
            """Gives the image of the specified person/thing"""
            url = "https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/Search/ImageSearchAPI"

            search = query

            querystring = {"pageNumber": "1", "pageSize": "10", "q": f"{search}", "autoCorrect": "true"}

            headers = {
                'x-rapidapi-key': os.getenv('image_rapidapi_key'),
                'x-rapidapi-host': os.getenv('image_rapidapi_host')
            }

            response = requests.request("GET", url, headers=headers, params=querystring)

            link = response.text
            idx = link.index('http')

            the_link = link[idx:].split('"')

            real_link = the_link[0]
            embed = disnake.Embed(color=disnake.colour.Colour.random())
            embed.set_image(url=real_link)

            await ctx.edit_original_message('', embed=embed)
        except ValueError:
            await ctx.edit_original_message('', embed=disnake.Embed(description='Not found', color=self.randomcolor()))

    @commands.slash_command()
    async def wiki(self, ctx, query):
        """Get the wikipedia summary"""
        query = query.replace(' ', '+').strip()

        url = f"https://google.com/search?q={query}"

        html = requests.get(url).text

        soup = BeautifulSoup(html, 'html5lib')

        result = soup.find_all('a')

        try:
            all_link = []

            for links in result:
                link = links['href']

                if 'https://en.wikipedia.org/wiki/' in link:
                    link = link.replace('/url?q=', '')

                    all_link.append(link)

            str_link = str(all_link[0])
            idx = str_link.index('&')
            str_link = str_link[:idx]

            wiki_topic = str_link[30:idx]

            info = wikipedia.summary(wiki_topic, sentences=2)

            await ctx.send(embed=disnake.Embed(color=self.randomcolor(), description=info))

        except IndexError:
            await ctx.send("sorry! couldn't fetch results")

    @commands.slash_command(dm_permission=False)
    @commands.check_any(commands.has_permissions(ban_members=True), commands.has_permissions(administrator=True),
                        commands.is_owner())
    async def showbans(self, ctx):
        """Show the users who are banned from this server"""
        baned_useers = await ctx.guild.bans()

        names = []
        c = 1
        for x in baned_useers:
            user = str(x.user)
            _id = str(x.user.id)
            user = f"{c}. {user} | ID: {_id}"
            names.append(user)
            c += 1

        users = '\n'.join(names)
        embed = disnake.Embed(title="Banned users in this server",
                              description=users,
                              color=disnake.colour.Colour.random())
        await ctx.send(embed=embed)

    @showbans.error
    async def showbans_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            embed = disnake.Embed(description="You need `ban members` permission to run this command.",
                                  color=disnake.Colour.random())
            await ctx.send(embed=embed)

    @commands.has_permissions(manage_emojis=True)
    @commands.slash_command(dm_permission=False)
    async def add_emoji(self, ctx, emoji_name: str, image_url: str):
        """Add an emoji to the server by providing the emoji image/gif url"""
        emj = requests.get(image_url).content

        emoji = await ctx.guild.create_custom_emoji(name=emoji_name, image=emj)
        await ctx.send(embed=disnake.Embed(description=f'successfully add <:{emoji.name}:{emoji.id}> to the server.',
                                           color=disnake.Colour.green()))
        await ctx.message.delete()


def setup(bot):
    bot.add_cog(Utility(bot))
