import praw
import random
import datetime
import time
from textblob import TextBlob

# FIXME:
# copy your generate_comment functions from the week_07 lab here
def generate_comment_0():
    option_1 = ['fight climate change','reduce carbon dioxide emissions', 'reduce the mining of fossil fuels','promote renewable energy sources','fund environmental research']
    green_reason = random.choice(option_1)
    option_2=['planet','home','world','environment']
    planet = random.choice(option_2)
    option_3=['in danger','in peril','being harmed','dying','being destroyed']
    danger = random.choice(option_3)
    option_4=['power','capabilities','capacity','control']
    power = random.choice(option_4)
    option_5=['save it','keep it alive','protect it','conserve it','take care of it']
    save = random.choice(option_5)
    text = "Select a candidate who will "+ green_reason + ". Our "+ planet + " is "+ danger+ " and we need to do everything in our " + power + " to " + save + "."
    return text

#print(generate_comment_0())

def generate_comment_1():
    option_1 = ['candidate', 'leader', 'head of state', 'commander in chief','chief of state','boss']
    name = random.choice(option_1)
    option_2 = ['support','take care of','fight for','back']
    support = random.choice(option_2)
    option_3=['Foreign students','Non-US students','Intl citizens','Students from other countries']
    intl = random.choice(option_3)
    option_4=['universities','colleges','higher educational institutions','academies','schools']
    h_ed = random.choice(option_4)
    option_5=['economy','GDP','markets','wealth','prosperity']
    economy = random.choice(option_5)

    text = "Choose a "+ name + " who will " + support + " international students. " + intl+ " not only fund a significant proportion of American " + h_ed+ " but boost the American "+economy+" when they start working. Sundar Pichai, Google's CEO, was an international student."
    return text

#print(generate_comment_1())

def generate_comment_2():
    option_1 = ['support female rights','support the my body my choice movement','keep abortion safe and legal','stand with planned parenthood', 'stand with women']
    women = random.choice(option_1)
    option_2 = ['parent','guardian','mother','mom']
    parent = random.choice(option_2)
    option_3 = ['daunting','challenging','difficult','hardest','demanding']
    daunting = random.choice(option_3)
    option_4=['right','option','say','ability','capacity','power']
    right = random.choice(option_4)
    option_5=['future','life','next years of their life','destiny','fate']
    future = random.choice(option_5)
    text = "Vote for a President who will "+ women+". Becoming a " + parent + " is one of the most " + daunting + " roles in the world and women should have the "+ right+ " to decide when they want to become one. Often women become pregnant not by choice and they should have the right to decide their "+future+ "."
    return text

#print(generate_comment_2())

def generate_comment_3():
    option_1 = ['create', 'build','develop','form','construct']
    create = random.choice(option_1)
    option_2 = ['borders', 'walls','divisions','boundaries','separations']
    borders = random.choice(option_2)
    option_3 = ['severe','life-threatening','serious','tough','dangerous']
    tough = random.choice(option_3)
    option_4 = ['climate change', 'poverty', 'global warming', 'over-population']
    climate = random.choice(option_4)
    option_5 = ['fighting','drifting apart','arguing','clashing','exchanging blows']
    fighting = random.choice(option_5)
    text = "Don't vote for a President who wants to " + create +" " + borders + ". The world is currently facing some of the most "+ tough+ " challenges ranging from " + climate +" to a pandemic. Countries should be working together instead of "+fighting+ "."
    return text
#print(generate_comment_3())

def generate_comment_4():
    option_1 = ['control','contain','stop','hinder','eliminate']
    control = random.choice(option_1)
    option_2 = ['a pandemic','COVID-19','widespread disease','widespread sickness','a virus attack']
    COVID = random.choice(option_2)
    option_3 = ['The US','America','The United States of America','The States']
    us = random.choice(option_3)
    option_4 = ['richest','wealthiest','well to do','affluent','prosperous']
    richest = random.choice(option_4)
    option_5 = ['highest','largest','biggest increases','frequent spikes']
    highest = random.choice(option_5)
    text = "Do not vote for a President who has not been able to " + control+" "+ COVID + ". " + us + " is one of world's most progressive, modern, and "+ richest + " countries and yet it has one of the " + highest + " COVID case numbers in the world."
    return text

#print(generate_comment_4())

def generate_comment_5():
    option_1 = ['promote','support','advocate for','speak up for','champion']
    promote = random.choice(option_1)
    option_2 = ['equality','fairness','diversity and inclusion','social equity','D&I']
    equality = random.choice(option_2)
    option_3 = ['do not matter','are not important','are insignificant','irrelevant']
    matter = random.choice(option_3)
    option_4 = ['humans','people','humans beings','homo sapiens']
    human = random.choice(option_4)
    option_5 = ['equally','fairly','justly','equitably','identically']
    equally = random.choice(option_5)

    text = "Please do not vote for a President who does not " + promote + " " + equality + ". Color, race, or ethnicity "+matter+ " we are all "+ human+ " at the end of the day and should be treated " + equally + "."
    return text

#print(generate_comment_5())

def generate_comment():
    '''
    This function should randomly select one of the 6 functions above,
    call that function, and return its result.
    '''
    options=[generate_comment_0,generate_comment_1,generate_comment_2,generate_comment_3,generate_comment_4,generate_comment_5]
    comment = random.choice(options)
    text = comment()
    return text

# connect to reddit 
reddit = praw.Reddit('bot')

# connect to the debate thread
reddit_debate_url = 'https://www.reddit.com/r/csci040temp/comments/jmxmie/us_spies_say_the_hunter_biden_email_controversy/'
submission = reddit.submission(url=reddit_debate_url)

# each iteration of this loop will post a single comment;
# since this loop runs forever, your bot will continue posting comments forever;
# (this is what makes it a deamon);
# recall that you can press CTRL-C in the terminal to stop your bot
#
# HINT:
# while you are writing and debugging your code, 
# you probably don't want it to run in an infinite loop;
# you can change this while loop to an if statement to make the code run only once

while True: 
    try:
        # printing the current time will help make the output messages more informative
        # since things on reddit vary with time
        print()
        print('new iteration at:',datetime.datetime.now())
        print('submission.title=',submission.title)
        print('submission.url=',submission.url)

        # FIXME (task 0): get a list of all of the comments in the submission
        # HINT: this requires using the .list() and the .replace_more() functions
        submission.comments.replace_more(limit= None)
        all_comments = submission.comments.list()
        # HINT: 
        # we need to make sure that our code is working correctly,
        # and you should not move on from one task to the next until you are 100% sure that 
        # the previous task is working;
        # in general, the way to check if a task is working is to print out information 
        # about the results of that task, 
        # and manually inspect that information to ensure it is correct; 
        # in this specific case, you should check the length of the all_comments variable,
        # and manually ensure that the printed length is the same as the length displayed on reddit;
        # if it's not, then there are some comments that you are not correctly identifying,
        # and you need to figure out which comments those are and how to include them.
        print('len(all_comments)=',len(all_comments))

        # FIXME (task 1): filter all_comments to remove comments that were generated by your bot
        # HINT: 
        # use a for loop to loop over each comment in all_comments,
        # and an if statement to check whether the comment is authored by you or not
        not_my_comments = []
        my_comments = []
        for comment in all_comments:
            if str(comment.author) != 'cs-40-tk':
                not_my_comments.append(comment)
        for comment in all_comments:
            if str(comment.author) == 'cs-40-tk':
                my_comments.append(comment)

        # HINT:
        # checking if this code is working is a bit more complicated than in the previous tasks;
        # reddit does not directly provide the number of comments in a submission
        # that were not gerenated by your bot,
        # but you can still check this number manually by subtracting the number
        # of comments you know you've posted from the number above;
        # you can use comments that you post manually while logged into your bot to know 
        # how many comments there should be. 
        print('len(not_my_comments)=',len(not_my_comments))
        print ('len(my_comments)=',len(my_comments))

        # if the length of your all_comments and not_my_comments lists are the same,
        # then that means you have not posted any comments in the current submission;
        # (you bot may have posted comments in other submissions);
        # your bot will behave differently depending on whether it's posted a comment or not
        has_not_commented = len(not_my_comments) == len(all_comments)
    
        if has_not_commented:
            # FIXME (task 2)
            # if you have not made any comment in the thread, then post a top level comment
            #
            # HINT:
            # use the generate_comment() function to create the text,
            # and the .reply() function to post it to reddit
            try: 
                submission.reply(generate_comment())
                print('top level comment')
            except praw.exceptions.RedditAPIException as e:
                print(e)
                print('exception found')
                # python to wait 900 seconds before proceeding
                print('starting to sleep')
                time.sleep(900)
                print('done sleeping')
        else:
            # FIXME (task 3): filter the not_my_comments list to also remove comments that 
            # you've already replied to
            # HINT:
            # there are many ways to accomplish this, but my solution uses two nested for loops
            # the outer for loop loops over has_not_comments,
            # and the inner for loop loops over all the replies of the current comment from the outer loop,
            # and then an if statement checks whether the comment is authored by you or not
            comments_without_replies = []
            for comment in not_my_comments:
                have_replied = False
                for reply in comment.replies:
                    if str(reply.author) == 'cs-40-tk':
                        have_replied = True
                if have_replied == False:
                    comments_without_replies.append(comment)
            # HINT:
            # this is the most difficult of the tasks,
            # and so you will have to be careful to check that this code is in fact working correctly
            print('len(comments_without_replies)=',len(comments_without_replies))

            # FIXME (task 4): randomly select a comment from the comments_without_replies list,
            # and reply to that comment
            #
            # HINT:
            # use the generate_comment() function to create the text,
            # and the .reply() function to post it to reddit
            if len(comments_without_replies) != 0:  
                """
                try:
                    rancom=random.choice(comments_without_replies)
                    print('random comment id=',rancom)
                    rancom.reply(generate_comment())
                    print('replied to random comment')  
                except praw.exceptions.RedditAPIException as e:
                    print(e)
                    print('exception found')
                    # python to wait 900 seconds before proceeding
                    print('starting to sleep')
                    time.sleep(900)
                    print('done sleeping')
                """
                #Task 6: Reply to comments based on sentiment (Extra credit) 
                #Type of comment selection
                yes_options = [generate_comment_0,generate_comment_1,generate_comment_2]
                no_options = [generate_comment_3,generate_comment_4,generate_comment_5]
                y_comment = random.choice(yes_options)
                n_comment = random.choice(no_options)
                yes_comment = y_comment()
                no_comment = n_comment()

                #Task 7: Sort comments based on upvotes 
                rancom=sorted(comments_without_replies,key=lambda comment:comment.score)
                com = rancom[0]
                print('higly upvoted comment title:',com.body)

                #Textblob
                blob = TextBlob(str(com.body.lower()))
                polarity = blob.sentiment.polarity
                try: 
                    if 'biden' in com.body.lower():
                        if polarity < 0:
                            com.reply(no_comment)
                            print('replied to highly voted comment') 
                        if polarity >= 0:
                            com.reply(yes_comment)
                            print('replied to highly voted comment') 
                    elif 'trump' in com.body.lower():
                        if polarity < 0:
                            com.reply(yes_comment)
                            print('replied to highly voted comment') 
                        if polarity >= 0:
                            com.reply(no_comment)
                            print('replied to highly voted comment')
                    else: 
                        com.reply(generate_comment())
                        print('replied to comment without Trump or Biden in text')
                except praw.exceptions.RedditAPIException as e:
                    print(e)
                    print('exception found')
                    # python to wait 900 seconds before proceeding
                    print('starting to sleep')
                    time.sleep(900)
                    print('done sleeping')
                
    #Task 8: Upvote and downvote comments based on sentiments
        for comment in not_my_comments: 
            blob = TextBlob(str(comment.body.lower()))
            polarity = blob.sentiment.polarity
            if 'biden' in comment.body.lower():
                if polarity < 0:
                    comment.downvote()
                    print('comment downvoted')
                elif polarity >= 0:
                    comment.upvote()
                    print('comment upvoted')
            elif 'trump' in comment.body.lower():
                if polarity < 0:
                    comment.upvote()
                    print('comment upvoted')
                elif polarity >= 0:
                    comment.downvote()
                    print('comment downvoted')
            else: 
                pass    
        
        # Task 9: Upvote comments that contain Biden 
        for comment in not_my_comments:
            if 'biden' in comment.body.lower():
                comment.upvote()
        print('Comment with Biden upvoted')       

        #Task 10: Upvote submissions that contain Biden 
        for submission in reddit.subreddit("csci040temp").hot(limit=25):
            if 'biden' in submission.title.lower():
                submission.upvote()
        print('Submission with Biden upvoted')
        
        #Task 11: Code for posting new submissions in submission.py file --> Done
        
    except praw.exceptions.APIException as e:
        #print(e)
        print('exception found')
        # python to wait 10 seconds before proceeding
        print('starting to sleep')
        time.sleep(10)
        print('done sleeping')

    # FIXME (task 5): select a new submission for the next iteration;
    # your newly selected submission should have a 50% chance of being the original submission
    # (url in the reddit_debate_url variable)
    # and a 50% chance of being randomly selected from the top submissions to the csci040 subreddit for the past month
    # HINT: 
    # use random.random() for the 50% chance,
    # if the result is less than 0.5,
    # then create a submission just like is done at the top of this page;
    # otherwise, create a subreddit instance for the csci40 subreddit,
    # use the .top() command with appropriate parameters to get the list of all submissions,
    # then use random.choice to select one of the submissions

    chance = random.random()
    top_submissions = reddit.subreddit("csci040temp").top(time_filter='day')

    if chance < 0.5: 
        submission = reddit.submission(url=reddit_debate_url)
    else: 
        submission = random.choice(list(top_submissions))
        print('top submission id=',submission)
    
          
        
        
        
    