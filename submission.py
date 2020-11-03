import praw
import random
import time

# connect to reddit 
reddit = praw.Reddit('bot')
reddit.validate_on_submit = True

for i in range (20):
    try: 
        top_submissions_2 = reddit.subreddit("politics").top(time_filter='month')
        pick_submission = random.choice(list(top_submissions_2))
        titles = pick_submission.title
        print('New submission title=',titles)
        urls = pick_submission.url
        reddit.subreddit("csci040temp").submit(titles,url=urls) 
    except praw.exceptions.RedditAPIException as e:
            print(e)
            print('exception found')
            # python to wait 900 seconds before proceeding
            print('starting to sleep')
            time.sleep(900)
            print('done sleeping')