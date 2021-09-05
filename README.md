# Reddit_Praw_Python
using Praw lib to scrape reddit posts


# Notes
- look into subprocess lib for multiple instances
- need to make the csv smaller
- make it auto collect data after a set period of time
- look into auto-storing data that is already gathered when i want to quit
    - would be more of a fail safe so I would not waste time/power
- move this to an offline always on device
- allow email notifications or smth, so i can get notified when done
- make plots
    - either histogram 
        - haw to bin stuff
            - want to do it on a log scale 
    - maybe scatter plot
        - its like half discrete half continuos data
- maybe do this for a single sub to sample
- using offline devices I can set up enough instances and data streaming to log all of the top subs
    - look into if the Rasp_pi is enough or if i can get this running on the new micocontroller they just released
        - down sides to this is that i need internet access everything besides the 10$ pi w has wifi, so the dongle would add to costs
    - would group smaller subs into a single instances
        - or break it across instances
- research if this has been done before and how it has been done

*Output Data Uses*
- histogram of scores/subreddit_subscribers
- best time to post
- best subs to post too
    - this would prob get skewed in smaller subs
    - would need to implement a fix for that then

**Advanced Analysis**
- using request lib do ml to distinguish between image types
    - different types of nsfw
    - using the image to generate a title for the image
        - or vise versa
