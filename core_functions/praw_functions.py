import asyncpraw
import os
import random


async def fetch_post(subreddit: str, amount: int):
    reddit = asyncpraw.Reddit(client_id=os.getenv('praw_client_id'),  # praw client id
                              client_secret=os.getenv('praw_client_secret'),  # praw client secret
                              username=os.getenv('praw_username'),  # reddit username
                              password=os.getenv('praw_password'),  # reddit password
                              user_agent=os.getenv('praw_user_agent'))  # write here anything

    posts = dict()
    subreddit = await reddit.subreddit(subreddit)

    for x in range(amount):
        all_subs = []

        async for submission in subreddit.top(limit=200):
            all_subs.append(submission)
        random_sub = random.choice(all_subs)
        name = random_sub.title
        url = random_sub.url
        posts[url] = name

    await reddit.close()
    return posts


async def is_subreddit_nsfw(subreddit):
    reddit = asyncpraw.Reddit(client_id=os.getenv('praw_client_id'),  # praw client id
                              client_secret=os.getenv('praw_client_secret'),  # praw client secret
                              username=os.getenv('praw_username'),  # reddit username
                              password=os.getenv('praw_password'),  # reddit password
                              user_agent=os.getenv('praw_user_agent'))  # write here anything

    subreddit = await reddit.subreddit(subreddit)
    await subreddit.load()
    if subreddit.over18:
        return True
    return False
