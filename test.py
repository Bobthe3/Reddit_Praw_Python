import passwords
import praw
reddit = praw.Reddit(
    client_id="Wnxf-3_6JD6JyblH9D-OVA",
    client_secret="oUg2U_zOiFKSBO1Dg5vqLfL4nI7ybg",
    username="praw",
    passwords=passwords.pasta,
    user_agent="prawv1"
)
sub = reddit.subreddit("funny")
limits = sub.top(limit=10)

for i in limits:
    print(dir(i))