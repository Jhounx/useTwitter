## useTwitter

**useTwitter** a class for using Twitter easily in order to help create bots for the social network.

## useTwitter Methods

* `__init__(auth_token, publicId)` - Receives the `auth_token` cookie in string.

* `search(searchText, count=20)` - Method responsible for doing research on Twitter. It receives a string to be searched and an optional parameter `count` that sets the number of return tweets (Default is 20).

* `homeTweet(text)` - Method responsible for tweeting something on your profile. It receives a string which is the text in which it will be tweeted. 

* `commentTweet(tweetId, text)` - Method responsible to comment some tweet. It receives a string `(tweetId)` that would be the post's identification ID and the text in which it will be commented.


* `likeTweet(tweetId)` - Method responsible for favoring some tweet. It receives a string `(tweetId)` that would be the post's identification ID.

* `getNotif(count=20)` - Method responsible for returning your last notifications, you can set the return amount with the `count` parameter.

* `retweet(tweetId)` - Method responsible for retweeting any tweet. It receives a string `(tweetId)` that would be the post's identification ID.

* `destroyTweet(tweetId)` - Method responsible for deleting some tweet. It receives a string `(tweetId)` that would be the post's identification ID.

## useTwitter BOT Methods

* `addFuntion(func)` - It receives a function that is included in a list of functions that will be performed by the bot.

* `bot()` - Performs all functions in the bot's function list

* `start(timer)` - The looping of executions of the functions that are in the list of functions begins. The timer parameter sets the time interval that the `bot ()` function will be executed (Default is 15 seconds).





