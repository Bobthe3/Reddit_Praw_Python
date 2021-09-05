import praw
import csv
import passwords
import time
import pandas as pd

#  using praw to scape reddit

reddit = praw.Reddit(
    client_id="Wnxf-3_6JD6JyblH9D-OVA",
    client_secret="oUg2U_zOiFKSBO1Dg5vqLfL4nI7ybg",
    username="praw",
    passwords=passwords.pasta,
    user_agent="prawv1"
)

subredditname = "all"
listsubnames = ["funny","all"]
# print(subredditname)

# get_write_csv(x=subredditname) # pass in the subreddit name and i will 

sub = reddit.subreddit("pythontips")
limits = sub.top(limit=1)



def submissiontitle():
    for submission in reddit.subreddit("").top(limit=10):
        print("\n-------------------")
        print(submission.title)
        print("\n-------------------")

def get_write_csv(x):
    titles =[]
    scores = []
    ids = []
    times = []
    with open('boomtest.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        for i in reddit.subreddit(x).top(limit=5):   
            scores.append(i.score)
            titles.append(i.title)
            ids.append(i.id)
            print("--")
        writer.writerow(titles)
        writer.writerow(scores)
        writer.writerow(ids)

def dirthing():
    global reddit
    x = reddit.subreddit("pythontips").top(limit=1)
    for i in x:
        print(dir(x))
        break

def commentsfunc():
    global reddit, limits
    for i in limits: 

        print(i.title)
        print(i.score)
        print(i.downs)
        print(i.ups)
        print(i.upvote_ratio)
        print(i.view_count)
        print(i.name)
        print(i.subreddit)


        i.comments.replace_more(limit=0)

        for j in i.comments.list():
            print(20*"-")
            print(j.body)
            print("Parent id", j.parent())
            print("comment id", j.id,"\n") 
            # if len(j.replies) > 0:
            #     counter = 0
            #     for h in j.replies:
            #         counter=counter+1
            #         print(">"*counter, h.body)
            #         print("Parent id", h.parent())
            #         print("comment id", h.id,"\n")
                     
# commentsfunc() # runs func

def streamingcomments(x):
    global reddit
    sub = reddit.subreddit(x)

    for comment in sub.stream.comments():
        try:
            print("--"*15)
            parentid = str(comment.parent())
            orginal = reddit.comment(id)
            print(parentid)
            print(orginal.body,"\n")
        except Exception as e:
            print("passed")
            pass

# streamingcomments(x="all")


#####################################
import csv
from itertools import chain
from datetime import datetime
import sys
import matplotlib.pyplot as plt
import numpy as np


def streamingpost(x,file_name,delay):
    global reddit
    sub = reddit.subreddit(x)

    titles =[]
    times = []
    ids = []
    over_18 = []
    link = []
    subreddit = []
    subscribers = []
    is_video = []
    author = []
    spoiler = []
    parentid =[]
    scores = []
    counter = 0
    counter_18=0

    headers = ['title','sub','sub subs','over_18','link','comments','view_count','is_video','author','time','spoiler']

    close_time = time.time() + delay

    while True:

        for i in sub.stream.submissions():
            try:
                print("--"*20)
                print(counter)
                counter = counter +1

                print("Title: ", i.title)
                print("---\nSub: ", i.subreddit)
                print("Subreddit-subs: ",i.subreddit_subscribers)
                print("Over 18: ",i.over_18)
                print("Link: www.reddit.com",i.permalink)
                print("Num comments: ", i.num_comments)
                print("Views: ", i.view_count)
                print("Is video: ",i.is_video)
                print("Author: u/",i.author)
                print("Id: ",i.id)
                print("Created: ",time.strftime("%a, %d %b %Y %H:%M:%S %Z", time.localtime(i.created))) # comverts time to human readable
                print("Is spoiler: ", i.spoiler)
                print("\n---")

                titles.append(i.title)
                ids.append(i.id)
                times.append(time.strftime("%a, %d %b %Y %H:%M:%S %Z", time.localtime(i.created)))
                over_18.append(i.over_18)
                link.append(i.permalink)
                subreddit.append(i.subreddit)
                subscribers.append(i.subreddit_subscribers)
                is_video.append(i.is_video)
                author.append(i.author)
                spoiler.append(i.spoiler)
                scores.append(i.score)

                if i.over_18 == True:
                    counter_18 = counter_18 +1

                if time.time()>close_time:
                    print(counter_18)
                    break

            except Exception as e:
                print("passed")
                print(str(e))
                pass
        

        

        if time.time()>close_time:
            with open(file_name, 'w', encoding='UTF8') as f:
                writer = csv.writer(f, dialect="excel")
                writer.writerow(ids)
                writer.writerow(titles)
                writer.writerow(author)
                writer.writerow(is_video)
                writer.writerow(spoiler)
                writer.writerow(times)
                writer.writerow(over_18)
                writer.writerow(link)
                writer.writerow(subreddit)
                writer.writerow(scores)
                writer.writerow(subscribers)
                f.close()
                print("\n\n-------------completed\nhave a good day man\n---\n")
                break
            print("donewefdfcf")
            break
    return print("the percentage of nsfw",float(counter_18/counter),"-------------\n\n")

# streamingpost(x="all",file_name = "loppa.csv",delay = 10)


#       # pass in subreddit name and how many you want 
#       delay is how many seconds u want if you put 3 seconds u get approx
        # 3 seconds = 100 posts
        # 60 seconds = ~700 posts




def ploter(open_file):

    scores = []
    subs = []
    holder = []

    with open(open_file, 'r') as read_obj:
        csv_reader = csv.reader(read_obj, delimiter="|")
        for i in csv_reader:
            holder.append(i)

    tempvar = [elem.strip("[]").split(',') for elem in holder[1]]
    scores = list(chain(*tempvar))

    tempvar = [elem.strip("[]").split(',') for elem in holder[4]]
    subs = list(chain(*tempvar))


    plt.scatter(scores, subs,marker='o')
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Scores")
    plt.ylabel("Subscibers")
    plt.show()

# ploter(open_file="boom.csv")


########################################

def time_search(file_name1,output_file):
    csv.field_size_limit(sys.maxsize)
    global reddit

    parent_ids = []
    scores = []
    ids=[]
    created_time = []
    current_time = []
    subscribers =[]
    scores_subs = []
    counter = 0
    i_turn = 0

    with open(file_name1, 'r') as read_obj:
        csv_reader = csv.reader(read_obj, delimiter="|")
        for i in csv_reader:
            parent_ids.append(i)
            counter=counter+1
            break

    print("\n\n\n\n")
    id_test = parent_ids[0]
    print("Running, Runnin, Runnin")

    # striping and cleaing the data
    # sub scriptiable with normal list notation list[0]
    tempvar = [elem.strip("[]").split(',') for elem in id_test]
    clean_id = list(chain(*tempvar))

    # getting the data for the specific id and storing it
    while(True):
        for i in clean_id:
            try:
                submission = reddit.submission(id=i)
                
                print("\n\n----------------")
                print(i)
                print(i_turn)
                i_turn = i_turn + 1
                print("Title: ",submission.title)
                print("subreddit: ",submission.subreddit)
                print("link: ",submission.permalink)
                print("score: ",submission.score)
                print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                print("/n On to the next!!!!")

                ids.append(submission.id)
                created_time.append(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(submission.created)))
                scores.append(submission.score)
                current_time.append(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                subscribers.append(submission.subreddit_subscribers)

                scores_subs.append(100*(submission.score/submission.subreddit_subscribers))


            except Exception as e:
                print(e)
                print(str(e))
                pass
        # this is outside the loop

        print("done gathering")
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        print("\n\n")

        # workin on ploting
        # ploter(x=scores_subs)

        # plt.scatter(scores, subscribers,marker='o')
        # plt.xscale("log")
        # plt.yscale("log")
        # plt.xlabel("Scores")
        # plt.ylabel("Scores")
        # plt.show()

        # storing results
        with open(output_file, 'w', encoding='UTF8') as f:
            writer = csv.writer(f, dialect="excel")
            writer.writerow(ids)
            writer.writerow(scores)
            writer.writerow(created_time)
            writer.writerow(current_time)
            writer.writerow(subscribers)
            f.close()
            print("\n\n-------------completed\nhave a good day man\n---\n")
        
        return print("counter: ", counter,"\n\n\n",scores_subs)

# enter the csv input and output
# enter csv name for the file wanted

time_search(file_name1="overnightrun.csv", output_file="boom.csv")


######################################

# now working on research data and displaying it

import numpy
import sys
def reader(file_name):
    csv.field_size_limit(sys.maxsize)
    global reddit

    parent_ids = []
    counter = 0


    with open(file_name, 'r') as read_obj:
        csv_reader = csv.reader(read_obj, delimiter="|")
        for i in csv_reader:
            parent_ids.append(i)
            counter=counter+1

    tempvar = [elem.strip("[]").split(',') for elem in parent_ids[0]]
    clean_id = list(chain(*tempvar))

    tempvar = [elem.strip("[]").split(',') for elem in parent_ids[9]]
    clean_subs = list(chain(*tempvar))

    for i in clean_id:
        print(clean_id)
        break
        
    for i in clean_subs:
        print(clean_subs)
        break

            
    print("\n\n\n----------------------------\n\n",counter)


# reader(file_name = "overnightrun.csv")