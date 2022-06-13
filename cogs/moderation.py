import disnake
from disnake.ext import commands
from core_functions import Confirm


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.randomcolor = disnake.Colour.random

    @commands.slash_command()
    @commands.check_any(commands.has_permissions(kick_members=True), commands.has_permissions(administrator=True))
    async def kick(self, ctx, user: disnake.Member, reason):
        """Kick a member from the server"""
        await user.kick(reason=reason)
        kick_ = disnake.Embed(title=f":white_check_mark: Kicked {user.name}!",
                              description=f"**Reason**: {reason}\n**kicked by**: {ctx.author.mention}",
                              color=0x9b59b6)
        get_kick = disnake.Embed(title=f"You have been kicked from {ctx.guild.name}",
                                 description=f"**Reason**: {reason}\n**kicked by**: {ctx.author.mention}",
                                 color=0x9b59b6)
        await ctx.channel.send(embed=kick_)
        await user.send(embed=get_kick)

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            embed = disnake.Embed(description="You need `kick members` permission to run this command.",
                                  color=disnake.Colour.random())
            await ctx.send(embed=embed)

    @commands.slash_command()
    @commands.check_any(commands.has_permissions(ban_members=True), commands.has_permissions(administrator=True))
    async def ban(self, ctx, user: disnake.Member, *, reason):
        """Ban a member from the server"""
        await user.ban(reason=reason)
        ban_ = disnake.Embed(title=f":white_check_mark: Banned {user.name}",
                             description=f"**Reason**: {reason}\n**Banned by**: {ctx.author.mention}",
                             color=disnake.colour.Colour.random())
        get_ban = disnake.Embed(title=f":white_check_mark: You have been banned from {ctx.guild.name}",
                                description=f"**Reason**: {reason}\n**banned by**: {ctx.author.mention}",
                                color=disnake.colour.Colour.random())
        await ctx.channel.send(embed=ban_)
        await user.send(embed=get_ban)

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            embed = disnake.Embed(description="You need `ban members` permission to run this command.",
                                  color=disnake.Colour.random())
            await ctx.send(embed=embed)

    @commands.slash_command()
    @commands.check_any(commands.has_permissions(administrator=True))
    async def nuke(self, ctx):
        """Deletes all messages form current channel"""
        confirm_view = Confirm()
        await ctx.send("Are you sure you want to nuke this channel. **All messages of this channel will be deleted**",
                       view=confirm_view)
        await confirm_view.wait()
        if confirm_view.value:
            newchannel = await ctx.channel.clone(name=ctx.channel.name)
            await ctx.channel.delete()

            em = disnake.Embed(title=f'CHANNEL NUKED by {ctx.author.name}', color=0x3498db)
            em.set_image(url='https://media.giphy.com/media/RKUVT8fPMsRfa/giphy.gif')

            await newchannel.send(embed=em)
        elif confirm_view.value is None:
            await ctx.send("Time out...")
        else:
            await ctx.send("Channel Nuke cancelled.")

    @nuke.error
    async def nuke_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            embed = disnake.Embed(description="You need `administrator` permission to run this command.",
                                  color=disnake.Colour.random())
            await ctx.send(embed=embed)

    @commands.slash_command()
    @commands.check_any(commands.has_permissions(manage_messages=True), commands.has_permissions(administrator=True))
    async def purge(self, ctx, amount: int):
        """Deletes given number of messages from current channel"""
        await ctx.channel.purge(limit=(amount + 1))
        embed = disnake.Embed(title=f"Purged ✅",
                              description=f'✅ purged {amount} messages by {ctx.author.mention}',
                              color=disnake.colour.Colour.random())
        await ctx.send(embed=embed, delete_after=15)

    @purge.error
    async def purge_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            embed = disnake.Embed(description="You need `manage messages` permission to run this command.",
                                  color=disnake.Colour.random())
            await ctx.send(embed=embed)

    @commands.check_any(commands.has_permissions(ban_members=True), commands.has_permissions(administrator=True))
    @commands.slash_command()
    async def unban(self, ctx, user):
        """Unban a user from the server"""
        if "#" in user:
            banned_users = await ctx.guild.bans()
            member_name, member_discriminator = user.split("#")

            for ban_entry in banned_users:
                user = ban_entry.user

                if (user.name, user.discriminator) == (member_name, member_discriminator):
                    await ctx.guild.unban(user)
                    await ctx.send(f'Unbanned {user.mention}')
        elif isinstance(int(user), int):
            banned_users = await ctx.guild.bans()
            userid = int(user)
            for ban_entry in banned_users:
                baned_user = ban_entry.user

                if userid == int(baned_user.id):
                    await ctx.guild.unban(baned_user)
                    await ctx.send(f'Unbanned {baned_user}')

    @ban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            embed = disnake.Embed(description="You need `ban members` permission to run this command.",
                                  color=disnake.Colour.random())
            await ctx.send(embed=embed)

    @commands.slash_command()
    @commands.check_any(commands.has_permissions(manage_roles=True), commands.has_permissions(administrator=True))
    async def give_role(self, ctx, user: disnake.Member, role: disnake.Role, reason='No reason provided'):
        """Gives the specified role to the specified user"""
        await user.add_roles(role, reason=reason)

        await ctx.send(embed=disnake.Embed(description=f"{ctx.author} gave {role} role to {user}",
                                           color=disnake.Colour.random()))
        print('success')

    @give_role.error
    async def giverole_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            embed = disnake.Embed(description="You need `manage roles` permission to run this command.",
                                  color=disnake.Colour.random())
            await ctx.send(embed=embed)

        elif isinstance(error, commands.CommandInvokeError):
            await ctx.send(embed=disnake.Embed(
                description='Provided role is a higher role than mine. So Either give me a higher role '
                            'or make mine role higher than the provided role to be '
                            'able to execute the command.', color=disnake.Colour.random()))

    @commands.slash_command()
    @commands.check_any(commands.has_permissions(manage_roles=True), commands.has_permissions(administrator=True))
    async def remove_role(self, ctx, user: disnake.Member, role: disnake.Role):
        """Removes the specified role from the specified user"""
        # _role = disnake.utils.get(ctx.guild.roles, id=role.id)
        await user.remove_roles(role)
        await ctx.send(embed=disnake.Embed(description=f"{ctx.author} romoved {role} role from {user}",
                                           color=self.randomcolor()))

    @remove_role.error
    async def remove_role_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            embed = disnake.Embed(description="You need `manage roles` permission to run this command.",
                                  color=disnake.Colour.random())
            await ctx.send(embed=embed)

    @commands.slash_command()
    @commands.check_any(commands.has_permissions(move_members=True), commands.has_permissions(administrator=True))
    async def move(self, ctx, user: disnake.Member, *, voice_channel: disnake.VoiceChannel):
        """Move a member from joined voice channel to specified voice channel."""
        if user.voice:
            await user.move_to(channel=voice_channel)
            await ctx.send(embed=disnake.Embed(description=f"{user.name} moved to {voice_channel} by {ctx.author}",
                                               color=self.randomcolor()))
        else:
            await ctx.send(embed=disnake.Embed(color=self.randomcolor(),
                                               description=f"error! {user} is not connected any voice channel"))

    @move.error
    async def move_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            embed = disnake.Embed(description="You need `move members` permission to run this command.",
                                  color=disnake.Colour.random())
            await ctx.send(embed=embed)

    @commands.slash_command()
    @commands.check_any(commands.has_permissions(deafen_members=True), commands.has_permissions(administrator=True))
    async def deafen(self, ctx, user: disnake.Member):
        """Deafen a member joined in a voice channel"""
        if user.voice:
            await user.edit(deafen=True)
            await ctx.send(
                embed=disnake.Embed(color=self.randomcolor(), description=f"{user} is deafened by {ctx.author}"))
        else:
            await ctx.send(embed=disnake.Embed(color=self.randomcolor(),
                                               description=f"error! {user} is not connected to any voice channel"))

    @deafen.error
    async def deafen_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            embed = disnake.Embed(description="You need `deafen members` permission to run this command.",
                                  color=disnake.Colour.random())
            await ctx.send(embed=embed)

    @commands.slash_command()
    @commands.check_any(commands.has_permissions(deafen_members=True), commands.has_permissions(administrator=True))
    async def undeafen(self, ctx, user: disnake.Member):
        """Undeafen a member"""
        await user.edit(deafen=False)
        await ctx.send(embed=disnake.Embed(color=self.randomcolor(),
                                           description=f"{user} is undeafened by {ctx.author}"))

    @undeafen.error
    async def undeafen_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            embed = disnake.Embed(description="You need `deafen members` permission to run this command.",
                                  color=disnake.Colour.random())
            await ctx.send(embed=embed)

    @commands.slash_command()
    @commands.check_any(commands.has_permissions(mute_members=True), commands.has_permissions(administrator=True))
    async def suppress(self, ctx, user: disnake.Member):
        """Mutes the user in voice channel"""
        await user.edit(mute=True)
        await ctx.send(embed=disnake.Embed(color=self.randomcolor(),
                                           description=f"{user} got muted in voice channel by {ctx.author}"))

    @suppress.error
    async def suppress_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            embed = disnake.Embed(description="You need `mute members` permission to run this command.",
                                  color=disnake.Colour.random())
            await ctx.send(embed=embed)

    @commands.slash_command()
    @commands.check_any(commands.has_permissions(mute_members=True), commands.has_permissions(administrator=True))
    async def unsuppress(self, ctx, user: disnake.Member):
        """Unmutes the user in voice channel"""
        await user.edit(mute=False)
        await ctx.send(embed=disnake.Embed(color=self.randomcolor(),
                                           description=f"{user} got unmuted in voice channel by {ctx.author}"))

    @unsuppress.error
    async def unsuppress_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            embed = disnake.Embed(description="You need `mute members` permission to run this command.",
                                  color=disnake.Colour.random())
            await ctx.send(embed=embed)

    @commands.slash_command()
    @commands.check_any(commands.has_permissions(move_members=True), commands.has_permissions(administrator=True))
    async def disconnect_user(self, ctx, user: disnake.Member):
        """Disconnect a user from a voice channel"""
        await user.move_to(channel=None)
        await ctx.send(embed=disnake.Embed(
            color=self.randomcolor(),
            description=f"{user} has been disconnected from voice channel by {ctx.author}"))

    @disconnect_user.error
    async def dis_user_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            embed = disnake.Embed(description="You need `move members` permission to run this command.",
                                  color=disnake.Colour.random())
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Moderation(bot))
