import praw
import time

# FIXME:
# connect to reddit 
reddit = praw.Reddit('bot_6')

#while True:


already_posted = []
link_post_count = 0
total_post_count = 0

for submission in reddit.subreddit('politics').hot(limit=100):
    if submission.url in already_posted:
        print('already posted')
    else:
        already_posted.append(submission.url)
        url = submission.url
        title = submission.title
        reddit.subreddit('BotTownHW4').submit(title, url=url)
        link_post_count += 1
        total_post_count += 1
        print('link_post_count=', link_post_count)
        print('total_post_count=', total_post_count)
        time.sleep(600)


self_post_count = 0
for submission in reddit.subreddit('america').hot(limit=100):
    if submission.url in already_posted:
        print('already posted')
    else:
        already_posted.append(submission.url)
        title = submission.title
        selftext = submission.selftext
        reddit.subreddit('BotTownHW4').submit(title, selftext=selftext)
        self_post_count += 1
        total_post_count += 1
        print('self_post_count=', self_post_count)
        print('total_post_count=', total_post_count)
        time.sleep(600)