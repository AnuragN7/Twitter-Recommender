# Twitter-Recommender
This application twitter users similar to a certain target user. The metric the application based its search on was the target user's most frequently used hashtag. 


Running the app:

1. Clone the repo
2. I'm assuming you are using Mac or Unix systems. Open your terminal and navigate to the directory where you've downloaded the repo. Make sure you enter the twitter-recommender directory.
3. Enter 'python3 -i User.py'
4. Once you're in the interpreter, type in 'user = User(twitter_handle)' where twitter_handle is whoever's handle you want to use.
5. Due to modular issues, python's networkx package failed to plot results. So include a method that displayes the data the app found in the terminal.
6. Type in 'user.display_related_users()' to see all the users related to the application's target user.

I decided not include my twitter credentials due to the sensitivity of the data. If you want to be able use the app, you'll need to register your own application and use those credentials to leverage the twitter api.
