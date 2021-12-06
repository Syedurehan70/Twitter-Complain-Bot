from twitter_bot import InternetSpeedTwitterBot

# necessary constants
PATH = "C:/Users/syed usama rehan/chromedriver_win32/chromedriver.exe"
PROMISED_DOWN = 16
PROMISED_UP = 17.16
TWITTER_USERNAME = "@usamatest32"
TWITTER_EMAIL = "usamatest32@gmail.com"
TWITTER_PASSWORD = "Angela$32"

# class object
bot = InternetSpeedTwitterBot(executable_path=PATH)

# getting the speed of internet
current_speed = bot.get_internet_speed()

# comparing speed if low than generating message and tweeting it
if int(bot.down) < PROMISED_DOWN or int(bot.up) < PROMISED_UP:
    MESSAGE = f"Hey Internet Provider, why is my internet speed is {bot.down}/{bot.up} when i pay for {PROMISED_DOWN}down/" \
           f"{PROMISED_UP}up?"
    # method responsible for tweeting
    bot.tweet_at_provider(username=TWITTER_USERNAME, password=TWITTER_PASSWORD, message=MESSAGE)
