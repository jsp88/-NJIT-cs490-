first need to create git reposiory 
make sure that all softwaer is install in your Could9(C9)
    tweepy
    flask 
    python-dotenv
In C9 file path should be 
    environment/Project1/filename.py file
    environment/Project1/filename.env file
    environment/Project1/templates/filename.html
    environment/Project1/static/filename.css
In filename.py file  
    Give a path using dotenv to your .env file to fetch the following keys
        KEY=''
        KEY_SECRET=''
        TOKEN=''
        TOKEN_SECRET=''
        these keys are twitter api keys found in twitter dashboard
    Access these keys using tweepy.OAuthHandler()
    Access these Tokens using variablename.set_access_token()
    Make index method
        Make Food list that contain name of foods
        Using random.choice() choose the random food item from the food list 
        Using Cursor() serch the tweets of the that random food from twitter
        Make tweet list and time list than apped tweets and time in it
        
    Using flask.render_template() call the .html file 
    give Port and Host through aap..run()

In filename.html file
    call the filename.css
    use <h1> to give title of your webpage 
    fetch the tweets from the filename.py and print them 

In filename.css
    give apropriate look for webpage
    uding background color for body 
    text color for <h1> tag
    
   Run `python filename.py`
    
