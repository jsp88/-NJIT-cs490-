1) First need to create git reposiory 

2)Make sure that all softwaer is install in your Could9(C9)
    tweepy
    flask 
    python-dotenv
3)In C9 file path should be 
    environment/Project1/filename.py file
    environment/Project1/filename.env file
    environment/Project1/templates/filename.html
    environment/Project1/static/filename.css
4)In filename.py file  
5)Give a path using dotenv to your .env file to fetch the following keys
        KEY=''
        KEY_SECRET=''
        TOKEN=''
        TOKEN_SECRET=''
        these keys are twitter api keys found in twitter dashboard
 6)  Access these keys using tweepy.OAuthHandler()
 7)   Access these Tokens using variablename.set_access_token()
 8)   Make index method
 9)   Make Food list that contain name of foods
 10)  Using random.choice() choose the random food item from the food list 
 11)  Using Cursor() serch the tweets of the that random food from twitter
 12)  Make tweet list and time list than apped tweets and time in it
        
 13)  Using flask.render_template() call the .html file 
 14)  Give Port and Host through aap..run()

15)  In filename.html file
16)  Call the filename.css
17)  Use <h1> to give title of your webpage 
18)  Fetch the tweets from the filename.py and print them 

19)  In filename.css
20)  Give apropriate look for webpage
21)  Give apropriate background color for body 
22)  Text color for <h1> tag
    
23)  Run `python filename.py`
    
