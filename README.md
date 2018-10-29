# Twitter-Recommender
This application twitter users similar to a certain target user. The metric the application based its search on was the target user's most frequently used hashtag. 


Running the app:

1. Clone the repo
2. I'm assuming you are using Mac or Unix systems. Open your terminal and navigate to the directory where you've downloaded the repo.
3. Enter python3 -i ' user = User(twitter_user)' where user is the handle of whoever you choose.
4. Due to modular issues, python's networkx package failed to plot results. So include a method that displayes the data the app found in the terminal.
5. Type in 'user.display_related_users()' to see all the users related to the appication's target user.
