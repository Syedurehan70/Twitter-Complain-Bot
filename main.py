from twitter_bot import InternetSpeedTwitterBot
import os

# necessary constants
PATH = os.environ.get("your_selenium_web_driver_path")
PROMISED_DOWN = 16
PROMISED_UP = 17.16
TWITTER_USERNAME = os.environ.get("your_twitter_username")
TWITTER_EMAIL = os.environ.get("your_twitter_email")
TWITTER_PASSWORD = os.environ.get("your_twitter_pass")

# class object
bot = InternetSpeedTwitterBot(executable_path=PATH)

# getting the speed of internet
current_speed = bot.get_internet_speed()

# comparing speed if low than generating message and tweeting it
if int(bot.down) < PROMISED_DOWN or int(bot.up) < PROMISED_UP:
    # tweeting message
    MESSAGE = f"Hey Internet Provider, why is my internet speed is {bot.down}/{bot.up} when i pay for {PROMISED_DOWN}down/" \
           f"{PROMISED_UP}up?"

    # method responsible for tweeting
    bot.tweet_at_provider(username=TWITTER_USERNAME, password=TWITTER_PASSWORD, message=MESSAGE)
