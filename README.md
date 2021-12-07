# Twitter-Complain-Bot

So this is a "Web Scrapping" project, which tweets itself mentioning the internet provider of yours, and  make a complain about the speed.

So, first we've created some necessary constants, than we've initailized a bot, which actually connects our driver and starts selenium for the use.

than from a "InternetSpeedTwitterBot" class we've built in twitter_bot file of python, we've called the method of getting speed form the speedtest website.
first we've open the website than, made  it wait for 20 secs, than clicked the info  button to  start the speedtest, after a delay of 60 secs,
we've extracted down and up  speed both and return them as a string, and saved that string in current_speed variable in main.py.

After that  we've compared the bot.down and bot.up attributes from the class to the constants of Promised_down and Promised_up.

if any one of the comparison is below the promised constant value than we set a message, and call tweet_at_provider method to post that message as a tweet to a internet provider.

We've passed  username and pass along with message, it open twitter's login page, selects useername area put username in it and pressed ENTER key, similar for the password
once it's logged it, we give a delay for a page to load  than select compose, clicked on it, than select message area, clicked on it put message in their,
and finally pressed tweet button.
