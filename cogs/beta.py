import disnake
from disnake.ext import commands
import asyncio
import core_functions


class Beta(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.randomcolor = disnake.Colour.random

    @commands.slash_command(dm_permission=False)
    async def reqtospeak(self, ctx, user: disnake.Member = None):
        """Ask a user to speak"""
        if user is None:
            await ctx.send(embed=disnake.Embed(color=self.randomcolor(),
                                               description=f"Mention someone to request! eg: `/reqtospeak @person`"))
        elif user:
            if user.voice:
                await user.request_to_speak()
                await ctx.send(embed=disnake.Embed(color=self.randomcolor(),
                                                   description=f"{user} is requested to speak by {ctx.author}"))
            else:
                await ctx.send(embed=disnake.Embed(color=self.randomcolor(),
                                                   description=f"{user} is not connected to any stage channel"))
        else:
            await ctx.send(embed=disnake.Embed(color=self.randomcolor(),
                                               description=f"{user} is not connected to a stage channel"))

    @commands.slash_command(guild_ids=[840468981551071232])
    async def emojify(self, ctx, *, text):
        """Write your text in form of emojis."""
        await core_functions.think(ctx)
        alphabet = {'a': '<:ascii_a:855729634057912400>', 'b': '<:ascii_b:855729635525394502>',
                    'c': '<:ascii_c:855729637409292298>', 'd': '<:ascii_d:855729639741718548>',
                    'e': '<:ascii_e:855729642257514496>', 'f': '<:ascii_f:855729643910201354>',
                    'g': '<:ascii_g:855729657361072151>', 'h': '<:ascii_h:855729658976141313>',
                    'i': '<:ascii_i:855729660821241876>', 'j': '<:ascii_j:855729662609195008>',
                    'k': '<:ascii_k:855729664828112926>', 'l': '<:ascii_l:855729678866186241>',
                    'm': '<:ascii_m:855729681390764032>', 'n': '<:ascii_n:855729683228655626>',
                    'o': '<:ascii_o:855729685080965140>', 'p': '<:ascii_p:855729687253876796>',
                    'q': '<:ascii_q:855729700495425576>', 'r': '<:ascii_r:855729702923927583>',
                    's': '<:ascii_s:855729706477158410>', 't': '<:ascii_t:855729708419645460>',
                    'u': '<:ascii_u:855729710151106581>', 'v': '<:ascii_v:855729722108674068>',
                    'w': '<:ascii_w:855729724118794251>', 'x': '<:ascii_x:855729726160109579>',
                    'y': '<:ascii_y:855729727847137290>', 'z': '<:ascii_z:855729730137489408>',
                    '1': "1️⃣", '2': "2️⃣", '3': "3️⃣", '4': "4️⃣", '5': "5️⃣", '6': "6️⃣",
                    '7': "7️⃣", '8': "8️⃣", '9': "9️⃣", '0': "0️⃣", "?": "❓", "!": "❗",
                    " ": "<:blank:855730267305803776>"}

        text = text.lower()
        emojifyied = ''
        for e in text:
            if e in alphabet.keys():
                emojifyied += alphabet[e]
            else:
                emojifyied += e

        await ctx.edit_original_message(emojifyied)

    @commands.slash_command(guild_ids=[840468981551071232])
    @commands.check_any(commands.has_permissions(manage_roles=True), commands.has_permissions(administrator=True))
    async def mute(self, ctx: disnake.CommandInteraction, user: disnake.Member, time: str, *, reason: str):
        """makes the person unable to send messages and speak in voice channels"""
        muted_role = disnake.utils.get(ctx.guild.roles, name="Muted")

        embed = disnake.Embed(title=f":white_check_mark: Muted {user.name}",
                              description=f"**Reason**: {reason}\n**Muted by**:{ctx.author.mention} for {time}",
                              color=disnake.colour.Colour.random())

        user_mute_embed = disnake.Embed(description=f"""**You have been muted in {ctx.guild.name}**
                                            **Reason**: {reason}\n**Muted by**:{ctx.author.mention} for {time}""",
                                        color=disnake.Colour.random())

        unmute_embed = disnake.Embed(title="Mute Over",
                                     description=f"{user.mention} **is now unmuted**",
                                     color=disnake.colour.Colour.random())

        user_unmute_embed = disnake.Embed(description=f"**You arn now unmuted in {ctx.guild.name}. Enjoy!**",
                                          color=disnake.Colour.random())

        if muted_role is None:
            perms = disnake.Permissions.none()
            perms.update(view_channel=True, connect=True)
            muted_role = await ctx.guild.create_role(name="Muted", permissions=perms, colour=disnake.Colour.red())
            await ctx.send(embed=disnake.Embed(
                description="As I didn't found any 'Muted' role in this server so I created one myself. "
                            "If you want to mute a admin/mod that have lower role than me then consider using "
                            "the `forcemute` command."))
            # for channel in ctx.guild.channels:
            #     await channel.set_permissions(muted_role, speak=False, send_messages=False, read_messages=True,
            #                                   read_message_history=True)


        if "sec" in time:
            duration_in_seconds = float(time[:-3])

            await user.add_roles(muted_role)
            await ctx.send(embed=embed)
            await user.send(embed=user_mute_embed)

            await asyncio.sleep(duration_in_seconds)

            await user.remove_roles(muted_role)
            await ctx.send(embed=unmute_embed)
            await user.send(embed=user_unmute_embed)

        elif "min" in time:
            duration_in_seconds = float(time[:-3]) * 60

            await user.add_roles(muted_role)
            await ctx.send(embed=embed)
            await user.send(embed=user_mute_embed)

            await asyncio.sleep(duration_in_seconds)

            await user.remove_roles(muted_role)
            await ctx.send(embed=unmute_embed)
            await user.send(embed=user_unmute_embed)

        elif "hrs" in time:
            duration_in_seconds = float(time[:-3]) * 60 * 60

            await user.add_roles(muted_role)
            await ctx.send(embed=embed)
            await user.send(embed=user_mute_embed)

            await asyncio.sleep(duration_in_seconds)

            await user.remove_roles(muted_role)
            await ctx.send(embed=unmute_embed)
            await user.send(embed=user_unmute_embed)

        elif "day" in time:
            duration_in_seconds = float(time[:-3]) * 86400

            await user.add_roles(muted_role)
            await ctx.send(embed=embed)
            await user.send(embed=user_mute_embed)

            await asyncio.sleep(duration_in_seconds)

            await user.remove_roles(muted_role)
            await ctx.send(embed=unmute_embed)
            await user.send(embed=user_unmute_embed)

        elif "notime" == time:
            await user.add_roles(muted_role)
            await ctx.send(embed=embed)
            await user.send(embed=user_mute_embed)
        else:
            embed = disnake.Embed(
                title="Mute command",
                description="provide some time to mute! \n"
                            "eg: `/mute @preson 45sec`, \n"
                            "`/mute @person 2min`,\n"
                            "`/mute @person 24hrs`\n"
                            "`/mute @person notime` - mutes person until you manually unmute them`\n"
                            "/mute @person [time] [reason]`",
                                  color=disnake.colour.Colour.random())
            await ctx.send(embed=embed)

    @mute.error
    async def mute_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            embed = disnake.Embed(description="You need `manage roles` permission to run this command.",
                                  color=disnake.Colour.random())
            await ctx.send(embed=embed)

    @commands.slash_command(guild_ids=[840468981551071232])
    @commands.check_any(commands.has_permissions(manage_roles=True), commands.has_permissions(administrator=True))
    async def forcemute(self, ctx, user: disnake.Member = None, time=None, *, reason="No reason provided"):
        """effective when a user already has some kind of role (beta)"""
        if user is None:
            embed = disnake.Embed(title="Mute command",
                                  description=f"""mention someone to mute! 
                                  eg: `/fmute @preson 45sec`,
                                      `/fmute @person 2min`,
                                      `/fmute @person 24hrs`,
                                      `/fmute @person notime` -mutes person until you manually unmute them
                                      `/fmute @person [time] [reason]`""",
                                  color=disnake.colour.Colour.random())
            await ctx.send(embed=embed)

        elif time is None:
            embed = disnake.Embed(title="Mute command",
                                  description=f"""provide some time to mute!
                                  eg: `/fmute @preson 45sec`,
                                      `/fmute @person 2min`,
                                      `/fmute @person 24hrs`
                                      `/fmute @person notime` -mutes person until you mannually unmute them
                                      `/fmute @person [time] [reason]`""",
                                  color=disnake.colour.Colour.random())
            await ctx.send(embed=embed)

        else:
            muted_role = disnake.utils.get(ctx.guild.roles, name="Muted")

            embed = disnake.Embed(title=f":white_check_mark: Muted {user.name}",
                                  description=f"**Reason**: {reason}\n**Muted by**:{ctx.author.mention} for {time}",
                                  color=disnake.colour.Colour.random())

            user_mute_embed = disnake.Embed(description=f"""**You have been muted in {ctx.guild.name}**
                                            **Reason**: {reason}\n**Muted by**:{ctx.author.mention} for {time}""",
                                            color=disnake.Colour.random())

            unmute_embed = disnake.Embed(title="Mute Over",
                                         description=f"{user.mention} **is now unmuted**",
                                         color=disnake.colour.Colour.random())

            user_unmute_embed = disnake.Embed(description=f"**You arn now unmuted in {ctx.guild.name}. Enjoy!**",
                                              color=disnake.Colour.random())

            if muted_role is None:
                muted_role = await ctx.guild.create_role(name="Muted")
                for channel in ctx.guild.channels:
                    await channel.set_permissions(muted_role, speak=False, send_messages=False, read_messages=True,
                                                  read_message_history=True)

            if "sec" in time:
                duration_in_seconds = float(time[:-3])
                roles = user.roles

                for role in roles:
                    rl = disnake.utils.get(ctx.guild.roles, name=role.name)
                    if str(rl) != "@everyone":
                        await user.remove_roles(rl)

                await user.add_roles(muted_role)
                await ctx.send(embed=embed)
                await user.send(embed=user_mute_embed)

                await asyncio.sleep(duration_in_seconds)
                for role in roles:
                    rl = disnake.utils.get(ctx.guild.roles, name=role.name)
                    if str(rl) != "@everyone":
                        await user.add_roles(rl)
                await user.remove_roles(muted_role)
                await ctx.send(embed=unmute_embed)
                await user.send(embed=user_unmute_embed)

            elif "min" in time:
                duration_in_seconds = float(time[:-3]) * 60
                roles = user.roles

                for role in roles:
                    rl = disnake.utils.get(ctx.guild.roles, name=role.name)
                    if str(rl) != "@everyone":
                        await user.remove_roles(rl)

                await user.add_roles(muted_role)
                await ctx.send(embed=embed)
                await user.send(embed=user_mute_embed)

                await asyncio.sleep(duration_in_seconds)

                for role in roles:
                    rl = disnake.utils.get(ctx.guild.roles, name=role.name)
                    if str(rl) != "@everyone":
                        await user.add_roles(rl)

                await user.remove_roles(muted_role)
                await ctx.send(embed=unmute_embed)
                await user.send(embed=user_unmute_embed)

            elif "hrs" in time:
                duration_in_seconds = float(time[:-3]) * 60 * 60
                roles = user.roles

                for role in roles:
                    rl = disnake.utils.get(ctx.guild.roles, name=role.name)
                    if str(rl) != "@everyone":
                        await user.remove_roles(rl)

                await user.add_roles(muted_role)
                await ctx.send(embed=embed)
                await user.send(embed=user_mute_embed)

                await asyncio.sleep(duration_in_seconds)

                for role in roles:
                    rl = disnake.utils.get(ctx.guild.roles, name=role.name)
                    if str(rl) != "@everyone":
                        await user.add_roles(rl)

                await user.remove_roles(muted_role)
                await ctx.send(embed=unmute_embed)
                await user.send(embed=user_unmute_embed)

            elif "days" in time:
                duration_in_seconds = float(time[:-3]) * 86400
                roles = user.roles

                for role in roles:
                    rl = disnake.utils.get(ctx.guild.roles, name=role.name)
                    if str(rl) != "@everyone":
                        await user.remove_roles(rl)

                await user.add_roles(muted_role)
                await ctx.send(embed=embed)
                await user.send(embed=user_mute_embed)

                await asyncio.sleep(duration_in_seconds)

                for role in roles:
                    rl = disnake.utils.get(ctx.guild.roles, name=role.name)
                    if str(rl) != "@everyone":
                        await user.add_roles(rl)

                await user.remove_roles(muted_role)
                await ctx.send(embed=unmute_embed)
                await user.send(embed=user_unmute_embed)

            elif "notime" == time:
                await user.add_roles(muted_role)
                await ctx.send(embed=embed)
                await user.send(embed=user_mute_embed)
            else:
                embed = disnake.Embed(title="Mute command",
                                      description=f"""provide some time to mute!
                                                  eg: `/fmute @preson 45sec`,
                                                      `/fmute @person 2min`,
                                                      `/fmute @person 24hrs`
                                                      `/fmute @person notime` -mutes person until you manually unmute them
                                                      `/fmute @person [time] [reason]`""",
                                      color=disnake.colour.Colour.random())
                await ctx.send(embed=embed)

    @forcemute.error
    async def forcemute_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            embed = disnake.Embed(description="You need `manage roles` permission to run this command.",
                                  color=disnake.Colour.random())
            await ctx.send(embed=embed)

    @commands.slash_command(guild_ids=[840468981551071232])
    @commands.check_any(commands.has_permissions(manage_roles=True), commands.has_permissions(administrator=True))
    async def unmute(self, ctx, user: disnake.Member = None):
        if user is None:
            embed = disnake.Embed(
                description=f"Mention the person to unmute! try: `/unmute @person`",
                color=disnake.Colour.random())
            await ctx.send(embed=embed)
        else:
            muted_role = disnake.utils.get(ctx.guild.roles, name="Muted")
            await user.remove_roles(muted_role)
            embed = disnake.Embed(title=f":white_check_mark: Unmuted {user.name}",
                                  description=f"{user.mention} got unmuted by {ctx.author.mention}",
                                  color=disnake.colour.Colour.random())
            await ctx.send(embed=embed)
            user_embed = disnake.Embed(
                description=f"{user.mention}, **You are now unmuted in {ctx.guild.name} by {ctx.author.name}",
                color=disnake.colour.Colour.random())
            await user.send(embed=user_embed)

    @unmute.error
    async def unumute_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            embed = disnake.Embed(description="You need `manage roles` permission to run this command.",
                                  color=disnake.Colour.random())
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Beta(bot))