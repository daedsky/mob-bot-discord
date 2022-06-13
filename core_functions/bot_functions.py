import random
import disnake
from .praw_functions import fetch_post


async def think(ctx):
    await ctx.send('Mob bot is thinking...')

async def send_praw_posts(ctx, subreddit: str, amount: int):
    await think(ctx)
    if amount > 11:
        await ctx.edit_original_message('', embed=disnake.Embed(description="Max limit is 10",
                                                                color=disnake.Colour.random()))
    else:
        posts = await fetch_post(subreddit, amount)

        c = 0
        for url in posts:
            name = posts[url]
            em = disnake.Embed(title=name, color=disnake.colour.Colour.random(), url=url)
            em.set_image(url=url)
            em.set_footer(text=f"Requested by {ctx.author}")
            if c == 0:
                await ctx.edit_original_message('', embed=em)
            else:
                await ctx.send(embed=em)
            c += 1

def getdetails_for_details_command(user):
    title = f"Details of {user.name}"
    last_list = ['madharchod', 'chutiya', 'bhosdika', 'bakrichod', 'lodu', 'gandu', 'chodu', 'randi',
                 'sins', 'bokachoda', 'betichod', 'lodu', 'mugi', 'radya xora', 'lund buddhi',
                 'motherfucker', 'cocksucker', 'the bitch', 'asshole', 'xakka', 'the gay']
    last_name = random.choice(last_list)
    full_name = f'{user.name} {last_name}'

    lsname = random.choice(last_list)
    rnum = random.randint(123, 9670)
    email = f"{user.name}{lsname}{rnum}@gmail.com"

    ph_num = str(random.randint(8000000000, 9999999999))

    passes = [f"mai_{lsname}_@12345", f"I'm_{lsname}_hu@12345"]
    pswd = random.choice(passes)

    status = ["virgin", "mutthal", "nibba", "depressed for sex", "tharki", "bhadwa", "tharak on it's peak",
              "apna haath gajan nath"]

    stat = random.choice(status)

    Networth = f"${random.randint(-10000, 10000)}"
    professions = ["vikari", "chamiya", "tiktoker", "fucker", "depak kalal ka chela",
                   "ambani ki najayej aulad", "scammer", "chor"]
    prof = random.choice(professions)

    return title, full_name, email, ph_num, pswd, stat, Networth, prof
