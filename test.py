import passwords
import praw
import time

# test

reddit = praw.Reddit(
    client_id="Wnxf-3_6JD6JyblH9D-OVA",
    client_secret="oUg2U_zOiFKSBO1Dg5vqLfL4nI7ybg",
    username="praw",
    passwords=passwords.pasta,
    user_agent="prawv1"
)

# sub = reddit.subreddit("funny")
# limits = sub.top(limit=10)

# for i in limits:
#     print(dir(i))


def dirthing():
    global reddit
    x = reddit.subreddit("pythontips").top(limit=1)
    for i in x:
        print(dir(i))
        print(i.subreddit_subscribers)
        break

# dirthing()


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
                     
# # commentsfunc() # runs func


def stream_write(name):
    titles =[]
    scores = []
    ids = []
    times = []
    with open(name, 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        for i in reddit.subreddit(x).top(limit=5):   
            scores.append(i.score)
            titles.append(i.title)
            ids.append(i.id)
            print("--")
        writer.writerow(titles)
        writer.writerow(scores)
        writer.writerow(ids)

def stream_csv(time_out,file_name,sub_name):
    global reddit, start_time
    sub = reddit.subreddit(sub_name)
    print(sub_name)


    print(file_name)
    file_name = file_name + str(".csv")
    print(file_name)

    titles=[]
    time=[]
    names=[]
    subreddit=[]
    permalink = []
    over_18 = []
    is_spoiler = []

    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time
        if elapsed_time > time_out:
            print("\n------------time met\n\n")
            break
        else:
            with open(name, 'w', encoding='UTF8') as f:
                writer = csv.writer(f)
                for i in sub.stream.submissions():
                    try:
                        print("--"*20)
                        print(counter," this is the numeber")
                        print("Title: ", i.title)
                        print("\n---Sub: ", i.subreddit)
                        print("Over 18: ",i.over_18)
                        print("Link: www.reddit.com",i.permalink)
                        print("Num comments: ", i.num_comments)
                        print("Views: ", i.view_count)
                        print("Is video: ",i.is_video)
                        print("Author: ",i.author)
                        print("Created: ",time.strftime("%a, %d %b %Y %H:%M:%S %Z", time.localtime(i.created))) # comverts time to human readable
                        print("Is spoiler: ", i.spoiler)
                        print("\n---") 
                    except Exception as e:
                        print("passed")
                        print(str(e))
                        pass                     


# start_time = time.time()
# stream_csv(10, "beans", "all")


# start_time = time.time()
# seconds = 2

# while True:
#     times = time.time()
#     elaps = times - start_time
#     if elaps<seconds:
#         for i in range (1000000000):
#             print("done: ",i)


# import time
# delay=5    ###for 15 minutes delay 
# close_time=time.time()+delay
# while True:
#     print("done")
#       ##bla bla
#       ###bla bla
#     if time.time()>close_time:
#          break


import pandas
import csv
import matplotlib

def csvcleaner(name1,name2 = str("test.csv")):

    df = pandas.read_csv(name1)
    df = df.transpose() # needs to transpose so it looks clean
    df.sort_values(by=[2], ascending=True)
    df.to_csv(name2)
    print("done\n\n\n\n\n-------")
    print(df[2])
    df.plot.pie(x=2, subplots=True)
    return df

# csvcleaner("loppa.csv","test123.csv")



# # importing python package
# import pandas as pd
  
# # read contents of csv file
# file = pd.read_csv("gfg.csv")
# print("\nOriginal file:")
# print(file) ------------
  
# # adding header
# headerList = ['id', 'name', 'profession']
  
# # converting data frame to csv -------------
# file.to_csv("gfg2.csv", header=headerList, index=False) -------------
  
# # display modified csv file
# file2 = pd.read_csv("gfg2.csv")
# print('\nModified file:')
# print(file2)


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
        break

            
    print(parent_ids)
    print("\n\n\n----------------------------\n\n",counter)


reader(file_name = "overnightrun.csv")