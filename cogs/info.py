import disnake
from disnake.ext import commands


class Info(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command()
    async def ping(self, ctx):
        """Shows the bots latency aka ping"""
        embed = disnake.Embed(title="",
                              description=f'**🏓 Pong!** Latency: {round(self.bot.latency * 1000)}ms',
                              color=disnake.colour.Colour.random())
        await ctx.send(embed=embed)

    @commands.slash_command()
    async def serverinfo(self, ctx):
        """Get the info of the server"""
        guild_id = ctx.guild.id
        name = str(ctx.guild.name)
        mem_count = str(ctx.guild.member_count)
        owner_id = str(ctx.guild.owner_id)
        owner = f"<@{owner_id}>"
        creation_date = str(ctx.guild.created_at)[:10]
        icon = str(ctx.guild.icon.url)
        v_lvl = ctx.guild.verification_level
        boosts = ctx.guild.premium_subscription_count
        large = str(ctx.guild.large)
        boosters = ', '.join([x.mention for x in ctx.guild.premium_subscribers])
        guild_roles = ctx.guild.roles
        roles = [x.mention for x in guild_roles]

        embed = disnake.Embed(title=f"{name} (ID: {guild_id})", description="Here is some info about Neutella",
                              color=disnake.colour.Colour.random())
        embed.add_field(name="👑 Owner", value=f"{owner}")
        embed.add_field(name="👨‍👩‍👧 Members count", value=f"{mem_count}")
        embed.add_field(name="✅ Verification level", value=f"{v_lvl}")
        embed.set_thumbnail(url=icon)
        embed.add_field(name="Is large server", value=("Yes" if large is True else "No"))
        embed.add_field(name="💸 Boosters count", value=f"{boosts}")
        embed.add_field(name="🎭 Roles Count", value=str(len(roles)))
        embed.add_field(name="📆 Created at", value=f"{creation_date}")

        if boosts > 0:
            embed.add_field(name="💸 Boosters", value=f"{boosters}")

        await ctx.send(embed=embed)

    @commands.slash_command()
    async def about(self, ctx):
        """Get the info of bot"""
        guilds = self.bot.guilds
        owner = self.bot.owner
        owner_id = self.bot.owner_id
        build = "python3"
        framework = "disnake"
        my_github_url = 'https://github.com/daedsky'

        embed = disnake.Embed(title="About Me",
                              color=disnake.colour.Colour.random())
        embed.add_field(name="👑Owner", value=f"{owner} | Id: {owner_id}", inline=False)
        embed.add_field(name="Total guilds joined", value=f"{str(len(guilds))}", inline=False)
        embed.add_field(name="Built with", value=f"{build}", inline=False)
        embed.add_field(name="framework", value=f"{framework}", inline=False)
        embed.set_author(name=owner, url=my_github_url, icon_url=self.bot.owner.avatar.url)
        embed.add_field(
            name="Additional things",
            value=f"[[Invite Me]({self.bot.invite_url})] [[Support Server]({self.bot.server_url})] [[github]({my_github_url})]")

        embed.set_thumbnail(url=self.bot.user.avatar.url)

        await ctx.send(embed=embed)

    @commands.slash_command()
    async def whois(self, ctx, user: disnake.Member):
        """Get the info of the specified user"""
        name = user.name
        _id = str(user.id)
        role_ids = user.roles
        roles = []
        for x in role_ids:
            role = f"{x.mention}"
            roles.append(role)
        toprole = f"<@&{str(user.top_role.id)}>"
        nickname = user.nick
        onMobile = user.is_on_mobile()
        joined_at = str(user.joined_at)[:10]
        isbot = user.bot
        created_at = str(user.created_at)[:10]
        animated_avatar = user.avatar.is_animated()

        embed = disnake.Embed(title=f"{user.name}'s information",
                              description="",
                              color=disnake.colour.Colour.random())

        embed.add_field(name="👑 Name", value=f"{name} | Id: {_id}", inline=False)
        embed.add_field(name="🎃 Nickname", value=f"{nickname}", inline=False)
        embed.add_field(name="🤖 Is Bot Account", value="yes" if isbot else "no", inline=False)
        embed.add_field(name="📱 Is on Mobile", value="yes" if onMobile else "no", inline=False)
        embed.add_field(name="🖼 Is Avatar Animated", value="yes" if animated_avatar else "no",
                        inline=False)
        embed.add_field(name="🔥 Top Role", value=f"{toprole}", inline=False)
        embed.add_field(name="🎭 Obtained Roles", value=', '.join(roles), inline=False)
        embed.add_field(name="🐊 Total roles", value=f"{str(len(roles))}", inline=False)
        embed.add_field(name="📅 Account created at", value=f"{created_at}", inline=False)
        embed.add_field(name="📆 Server joined at", value=f"{joined_at}")

        embed.set_thumbnail(url=user.display_avatar.url)

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Info(bot))
