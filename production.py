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
                print("Parent_id: ",i.parentid)
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
                writer = csv.writer(f)
                writer.writerow(titles)
                writer.writerow(ids)
                writer.writerow(author)
                writer.writerow(is_video)
                writer.writerow(spoiler)
                writer.writerow(times)
                writer.writerow(over_18)
                writer.writerow(link)
                writer.writerow(subreddit)
                writer.writerow(subscribers)
                f.close()
                print("\n\n-------------completed\nhave a good day man\n---\n")
                break 
            with open("counter.csv", 'w') as file1:
                dw = csv.DictWriter(file1, delimiter=',', 
                        fieldnames=headers)
                dw.writeheader()
                file1.writerow(counter)
                file1.writerow(counter_18)
                break
            break
  
    return print("the percentage of nsfw: ",float(counter_18/counter))

# streamingpost(x="all",file_name = "loppa.csv",delay = 5)

# pass in subreddit name and how many you want 
# delay is how many seconds u want if you put 3 seconds u get approx
# 3 seconds = 100 posts
# 60 seconds = ~700 posts



import csv
from itertools import chain
from datetime import datetime
import sys


def time_search(file_name1,output_file):
    csv.field_size_limit(sys.maxsize)
    global reddit

    parent_ids = []
    scores = []
    ids=[]
    created_time = []
    current_time = []
    counter = 0

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


    while(True):
        for i in clean_id:
            try:
                submission = reddit.submission(id=i)
                
                print("\n\n----------------")
                print(i)
                print("Title: ",submission.title)
                print("subreddit: ",submission.subreddit)
                print("link: ",submission.permalink)
                print("score: ",submission.score)
                print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                print("\n")

                ids.append(submission.id)
                created_time.append(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(submission.created)))
                scores.append(submission.score)
                current_time.append(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


            except Exception as e:
                print(e)
                print(str(e))
                pass

        with open(output_file, 'w', encoding='UTF8') as f:
            writer = csv.writer(f, dialect="excel")
            writer.writerow(ids)
            writer.writerow(scores)
            writer.writerow(created_time)
            writer.writerow(current_time)
            f.close()
            print("\n\n-------------completed\nhave a good day man\n---\n")
            break
        return print("counter: ", counter)


# enter the csv input and output
# enter csv name for the file wanted

time_search(file_name1="overnightrun.csv", output_file="overnightrun_export.csv")