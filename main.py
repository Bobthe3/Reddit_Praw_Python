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

# streamingcomments(x="politics")

def streamingpost(x,num):
    global reddit
    sub = reddit.subreddit(x)
    counter = 0
    for i in sub.stream.submissions():
        try:
            if counter !=num:
                print("--"*20)
                counter = counter + 1
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

            if counter == num:
                print("\n\n-------------completed\nhave a good day man\n---\n")
                break
        except Exception as e:
            print("passed")
            print(str(e))
            pass

streamingpost(x="all",num=20) # pass in subreddit name and how many you want 