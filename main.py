import praw
import csv
import passwords


def submissiontitle():
    for submission in reddit.subreddit("").top(limit=10):
        print("\n-------------------")
        print(submission.title)
        print("\n-------------------")

def get_write_csv(x):
    titles =[]
    scores = []
    ids = []
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
print(subredditname)

# get_write_csv(x=subredditname) # pass in the subreddit name and i will 

sub = reddit.subreddit("pythontips")
limits = sub.top(limit=1)


for i in limits:

    print(i.title)
    print(i.score)
    print(i.downs)
    print(i.ups)
    print(i.comments)

    comments = i.comments.list()

    print("Parent id", i.parent())
    print("comment id", i.id,"\n") 
    for j in comments:
        print(20*"-")
        print(j.body)
        if len(j.replies) > 0:
            for h in j.replies:
                print(">>", h.body)
                     


