import disnake.errors
from disnake.ext import commands
from core_functions import read_json


class AutoResponder(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def get_commands_of_a_cog(self, cog):
        cmd = self.bot.get_cog(cog).get_commands()
        strCmd = [f"{str(x)}" for x in cmd]
        return strCmd

    @commands.Cog.listener()
    async def on_message(self, message):
        bot = self.bot
        msg = message.content.lower()

        data = read_json("data/disable_auto_responder.json")

        if message.author != bot.user and not message.author.bot and str(message.guild.id) in data:

            TheCogs = ['Animals', 'Fun', 'Moderation', 'ApiDependentCommands', 'Info', 'AnimeNsfw', 'RealNsfw',
                       'Utility', 'Settings']

            AllCommands = []
            for c in TheCogs:
                __Commands = self.get_commands_of_a_cog(c)
                AllCommands.extend(__Commands)

            prefix_data = read_json("data/prefixes.json")
            if str(message.guild.id) in prefix_data:
                prefix = prefix_data[str(message.guild.id)]
            else:
                prefix = "Mob "

            if (prefix not in msg and not any([x for x in AllCommands if x in msg])):
                try:
                    if 'thank' in msg or 'thx' in msg:
                        await message.channel.send("""No need to say thank you instead, instead you can give your ass for fuck
                         to needy people 😜.""")

                    elif "i'm handsome" in msg or "i am handsome" in msg or "you are handsome" in msg or "you're handsome" in msg:
                        await message.add_reaction("🤣")

                    elif msg.startswith("i am "):
                        await message.channel.send(f"Hi {msg[5:]}, I'm dad.")

                    elif msg.startswith("i'm "):
                        await message.channel.send(f"Hi {msg[4:]}, I'm dad.")

                    elif 'baap ko mat sikha' in msg:
                        await message.channel.send(f"{message.author.name} tu napunsak h bhosdike.")

                    elif 'bau lai na sikha' in msg:
                        await message.channel.send(f"{message.author.name} ta xakka hos mugi.")

                    elif "bau hu" in msg:
                        await message.channel.send(f"{message.author.name} ta xakka hos radi.")

                    elif "don't teach your father" in msg:
                        await message.channel.send(f"{message.author.name} you got no dick burh.")

                    elif "tera baap hu" in msg or "baap hu tera" in msg:
                        await message.channel.send(f"{message.author.name} tu napunsak h bhosdike.")

                    elif "i'm your dad" in msg or "i am your dad" in msg or "i'm ur dad" in msg or "i am ur dad" in msg:
                        await message.channel.send(f"{message.author.mention}, hey! you don't even have a dick")

                    elif "motherfucker" in msg or "mother fucker" in msg:
                        await message.channel.send(f"{message.author.name} son of a bitch")

                    elif "ag lund mera" in msg or "lund mera" in msg or "loda mera" in msg:
                        await message.channel.send(f"{message.author.name} tere paas lund hi nhi hai")

                    elif "lund lele mera" in msg or "lund lele" in msg or "loda lele mera" in msg or "loda lele" in msg:
                        await message.channel.send(f"{message.author.name} tu lele mera")

                    elif "randi k bacche" in msg or "randi k " in msg:
                        await message.channel.send(f"{message.author.name} xakke k bacche")

                    elif "lado chus" in msg or "mero lado chusnus" in msg:
                        await message.channel.send(f"{message.author.name} ta mero chus")

                    elif "betichod" in msg or "beti chod" in msg:
                        await message.channel.send("chal be bokacoda")

                    elif "fucker" in msg or "fuker" in msg:
                        await message.channel.send("are you all motherfuckers")

                    elif "fuck you" in msg or "fuck u" in msg:
                        await message.channel.send(f"{message.author.name} Fuck you 3000. 🤪")

                    elif "fuck off" in msg:
                        await message.channel.send(f"{message.author.name}, I appericiate")

                    elif "maa chuda" in msg:
                        await message.channel.send(f"teri maa chudau?")

                    elif "teri maki chut" in msg or "teri makichut" in msg:
                        await message.channel.send(f"aur teri maka bhosda")

                    elif "maka bhosda" in msg or "teri maka bhosda" in msg:
                        await message.channel.send(f"teri maka loda")

                    elif "makichut" in msg or "maki chut" in msg or "maki choot" in msg:
                        await message.channel.send(f"{message.author.name} teri maka lund")

                    elif "khada " in msg:
                        await message.channel.send(f"mera vi")

                    elif "chuda" in msg:
                        await message.channel.send(f"maa chudao bhosdiwalo")

                    elif "jerk" in msg:
                        await message.channel.send("fu*k off jerks")

                    elif "kuch vi bolo" in msg or "kuch vi kaho" in msg or 'kuch v bolo' in msg or 'kuch v khao' in msg:
                        await message.channel.send("Rajan Bhosdika 😜")

                    elif "fuck" in msg:
                        await message.channel.send("Sorry, I don't fu*k assholes ")

                    elif "shit" in msg:
                        await message.channel.send("no need to say it, I already know")

                    elif "asshole" in msg:
                        await message.channel.send("yeah, I know 🙄")

                    elif "bitch" in msg:
                        await message.channel.send("talking about your mom?")

                    elif "madharchod" in msg or "madarchod" in msg:
                        await message.channel.send("abe laude apna kaam kr, bhosdike")

                    elif "bhenchod" in msg or "benchod" in msg or "bahenchod" in msg:
                        await message.channel.send("dhat teri maki ch*t")

                    elif "laude" in msg:
                        await message.channel.send("yahi patak k chod denge, chal nikal madharch*d")

                    elif "bhen k lode" in msg or "behen k l*de" in msg or "bahen k lode" in msg:
                        await message.channel.send(f"{message.author.name} xakke")

                    elif "lode" in msg:
                        await message.channel.send(f"{message.author.name} khali ka injection lele apni gand mai")

                    elif "bsdk" in msg or "bhosdike" in msg:
                        await message.channel.send(f"{message.author.name} not you but Tejaswi is chuttad.")

                    elif "bhosdi" in msg:
                        await message.channel.send("abe laude apna kaam kr")

                    elif "bhosdika" in msg:
                        await message.channel.send("arre bhai bhosdika toh rajan hai")

                    elif "bhosda" in msg:
                        await message.channel.send("Gali mat de, ye lauda friendly server h. No gali allowed 😉.")

                    elif "abe sale" in msg or "abe saale" in msg:
                        await message.channel.send("hey! don't abuse, be straight like me")

                    elif "saale" in msg:
                        await message.channel.send('no it\'s "sale madarchod"')

                    elif "gandu" in msg:
                        await message.channel.send("Tu gandu, tera baap gandu")

                    elif "gand" in msg:
                        await message.channel.send("jaa be laude")

                    elif "chaman" in msg:
                        await message.channel.send("chaman chutiya")

                    elif "chutiya" in msg:
                        await message.channel.send("tu chutiya, tera baap chutiya")

                    elif "chutiye" in msg:
                        await message.channel.send("lund buddhi")

                    elif "chut" in msg or "choot" in msg:
                        await message.channel.send(f"{message.author.name} Teri maki chut maru 😝.")

                    elif "lund" in msg:
                        await message.channel.send(f"gand m daale")

                    elif "dickhead" in msg:
                        await message.channel.send(f"{message.author.name} cunt")

                    elif "dick" in msg:
                        await message.channel.send("pussy")

                    elif "chodu" in msg:
                        await message.channel.send("teri maka bhosda khodu")

                    elif "bokachoda" in msg:
                        await message.channel.send(f"{message.author.name} maarbo kaane baajbo dhone")

                    elif "bakrichod" in msg:
                        await message.channel.send(f"{message.author.name} chipkali chod")

                    elif "chod" in msg:
                        await message.channel.send("bhosdike, chodna mera kaam hai")

                    elif "pussy" in msg:
                        await message.channel.send("my gandfather loved pussy")

                    elif "fuddi" in msg:
                        await message.channel.send("my gandfather loved fuddi")

                    elif "kese" in msg or "kaise" in msg:
                        await message.channel.send("lode se")

                    elif "jhatu" in msg:
                        await message.channel.send(f"Meri buggy tera ghoda {message.author.mention} bhen ka loda")

                    elif "jhat" in msg or "jhaat" in msg:
                        await message.content.send("jhat k pille")

                    elif "loda" in msg:
                        await message.channel.send("tere baap ki gand mai foda aur tu bhen ka loda")

                    elif "lodu" in msg:
                        await message.channel.send(f"lodu {message.author.name}, lodu {message.author.name}")

                    elif "mugi" in msg:
                        await message.channel.send(f"{message.author.name} machikne gedo kha")

                    elif "machikne" in msg:
                        await message.channel.send(f"{message.author.name} bhak radya xora")

                    elif "randi" in msg or "randy" in msg:
                        await message.channel.send("mugi tero budi randi")

                    elif "gedo" in msg:
                        await message.channel.send("kati gedo gedo garya, halka mugi pani garam")

                    elif "geda" in msg:
                        await message.channel.send("gedo")

                    elif "lado" in msg:
                        await message.channel.send(f"{message.author.name} gedo kha")

                    elif "cunt" in msg:
                        await message.channel.send("you really need a high five... on your face... with a chair")

                    elif "moron" in msg:
                        await message.channel.send(f"{message.author.name}'s mom should have swallowed")

                    elif "nigga" in msg:
                        await message.channel.send('niggi')

                    elif "chik" in msg:
                        await message.channel.send("sabka sab machikne")

                    elif msg.startswith('f') and len(msg) == 1:
                        await message.channel.send('f')

                    elif "hello" in msg:
                        await message.channel.send("Hi, motherfucker 😜")

                    elif msg.startswith("hi"):
                        await message.channel.send("Hello, motherfucker 😜")

                except disnake.errors.Forbidden:
                    await message.guild.leave()
                    print(f"left {message.guild}")
                except AttributeError:
                    print("no gali in dm")


def setup(bot):
    bot.add_cog(AutoResponder(bot))
