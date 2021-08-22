import praw
import csv
import passwords
import time

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
            orginal = reddit.comment(parentid)
            print(parentid)
            print(orginal.body,"\n")
        except Exception as e:
            print("passed")
            pass

# streamingcomments(x="all")

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
    counter = 0

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

                if time.time()>close_time:
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
                writer.writerow(times)
                writer.writerow(over_18)
                writer.writerow(link)
                writer.writerow(subreddit)
                writer.writerow(subscribers)
                print("\n\n-------------completed\nhave a good day man\n---\n")
                break
            break

streamingpost(x="all",file_name = "loppa.csv",delay = 3) 
#       # pass in subreddit name and how many you want 
#       delay is how many seconds u want if you put 3 seconds u get approx
        # 100 posts