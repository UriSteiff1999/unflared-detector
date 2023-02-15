import praw

reddit = praw.Reddit(client_id="tkXtoI5QUKY51kSk5K5Csg",
    client_secret="0RnA83BWimV0zGIhc14zxV78U6WWkg",
    user_agent="chrome",) # replace 'bot_name' with your bot's name

subreddit = reddit.subreddit('askmiddleeast')

for comment in subreddit.stream.comments(skip_existing=True):
    if not comment.author_flair_text:
        comment.reply("Don't be a stranger, flair up")
