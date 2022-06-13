import disnake
from disnake.ext import commands


class Help(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    def get_commands_from_cog(self, cog):
        cmd = self.bot.get_cog(cog).get_slash_commands()
        str_cmd = [f'`{x.name}`' for x in cmd]
        cmds = '\n'.join(str_cmd)
        return cmds

    @commands.slash_command()
    async def help(self, ctx, category=''):
        category = category.lower()
        if category == '':
            embed = disnake.Embed(title='Mob bot command categories', color=disnake.Colour.yellow())
            embed.add_field(name=':smiley: Fun', value='Have fun with dozens of fun commands.')
            embed.add_field(name=':information_source: Info', value='Get information.')
            embed.add_field(name=':shield: Moderation', value='Use your admin rights for moderating the server.')
            embed.add_field(name=':rabbit: Animals', value='Get some cute animals.')
            embed.add_field(name=':underage: NSFW', value='Get some adult & naughty pics/gifs.')
            embed.add_field(name=':hammer_and_pick: Utility', value='Some powerful utility commands.')

        elif category == 'fun':
            commands = self.get_commands_from_cog('Fun')
            embed = disnake.Embed(title=':smiley: Fun commands', color=disnake.Colour.yellow(), description=commands)

        elif category == 'info':
            commands = self.get_commands_from_cog('Info')
            embed = disnake.Embed(title=':information_source: Info commands', color=disnake.Colour.yellow(), description=commands)

        elif category == 'moderation':
            commands = self.get_commands_from_cog('Moderation')
            embed = disnake.Embed(title=':shield: Moderation commands', color=disnake.Colour.yellow(), description=commands)

        elif category == 'animals':
            commands = self.get_commands_from_cog('Animals')
            embed = disnake.Embed(title=':rabbit: Animal commands', color=disnake.Colour.yellow(), description=commands)

        elif category == 'nsfw':
            commands = self.get_commands_from_cog('Nsfw')
            embed = disnake.Embed(title=':underage: NSFW commands', color=disnake.Colour.yellow(), description=commands)

        elif category == 'utility':
            commands = self.get_commands_from_cog('Utility')
            embed = disnake.Embed(title=':hammer_and_pick: Utility commands', color=disnake.Colour.yellow(), description=commands)

        else:
            embed = disnake.Embed(description='Invalid category', color=disnake.Colour.yellow())

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Help(bot))
