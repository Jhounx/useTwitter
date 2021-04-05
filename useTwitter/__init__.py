import requests 
from json import loads
from time import sleep

class useTwitter:
    url = 'https://api.twitter.com'
    botFunc = []
    lastPosts = []

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0',
        'Accept': '*/*',
        'Accept-Language': 'pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'x-twitter-auth-type': 'OAuth2Session',
        'x-twitter-client-language': 'en',
        'x-twitter-active-user': 'yes',
        'x-csrf-token': '05937734b769d60e96c90833b0419723',
        'Origin': 'https://twitter.com',
        'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
        'Referer': 'https://twitter.com/',
        'Connection': 'close'
    }
    
    def __init__(self, auth_token): 
        self.cookies = {
            'personalization_id':"v1_u6ytKonxLxhzowTihGlUfQ==",
            'guest_id':'v1%3A158852046331539754',
            '_ga':'GA1.2.1163999564.1588520463',
            'dnt':'1', 
            'ads_prefs':"HBISAAA=",
            'kdt':'OkydXEi6Gzwut68hjIfzwaZ4nyVRO18MOq6nx9oV',
            'remember_checked_on':'1', 
            'twid':'u%3D1125459223696019456',
            'auth_token':auth_token,
            'csrf_same_site_set':'1',
            'rweb_optin':'side_no_out',
            'csrf_same_site':'1',
            'night_mode':'1', 
            'des_opt_in':'N', 
            '__utma':'191792890.1163999564.1588520463.1589309979.1589309979.1', 
            '__utmz':'191792890.1589309979.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)', 
            'mbox':'session#22d1ae8adc6743e2a8c0ea120dba5f90#1589555339|PC#22d1ae8adc6743e2a8c0ea120dba5f90.17_0#1652798281', 
            'ct0':'05937734b769d60e96c90833b0419723', 
            '_gid':'GA1.2.53081779.1596923736'
        }

    def search(self, searchText, count=20): #Search 
        params = {
            'include_profile_interstitial_type':'1',
            'include_blocking':'1',
            'include_blocked_by':'1',
            'include_followed_by':'1',
            'include_want_retweets':'1',
            'include_mute_edge':'1',
            'include_can_dm':'1',
            'include_can_media_tag':'1',
            'skip_status':'1',
            'cards_platform':'Web-12',
            'include_cards':'1',
            'include_ext_alt_text':'true',
            'include_quote_count':'true',
            'include_reply_count':'1',
            'tweet_mode':'extended',
            'include_entities':'true',
            'include_user_entities':'true',
            'include_ext_media_color':'true',
            'include_ext_media_availability':'true',
            'send_error_codes':'true',
            'simple_quoted_tweet':'true',
            'q':searchText,
            'count':count,
            'query_source':'typed_query',
            'pc':'1',
            'spelling_corrections':'1',
            'ext':'mediaStats,highlightedLabel'
        }
        req = requests.get(self.url+'/2/search/adaptive.json', params=params, headers=self.headers, cookies=self.cookies)
        return loads(req.text)['globalObjects']['tweets']
    
    def homeTweet(self, text): #Tweet in your home
        data = {
            'include_profile_interstitial_type':'1',
            'include_blocking':'1',
            'include_blocked_by':'1',
            'include_followed_by':'1',
            'include_want_retweets':'1',
            'include_mute_edge':'1',
            'include_can_dm':'1',
            'include_can_media_tag':'1',
            'skip_status':'1',
            'cards_platform':'Web-12',
            'include_cards':'1',
            'include_ext_alt_text':'true',
            'include_quote_count':'true',
            'include_reply_count':'1',
            'tweet_mode':'extended',
            'simple_quoted_tweet':'true',
            'trim_user':'false',
            'include_ext_media_color':'true',
            'include_ext_media_availability':'true',
            'auto_populate_reply_metadata':'false',
            'batch_mode':'off',
            'status':text
        }

        req = requests.post(self.url+'/1.1/statuses/update.json',data=data, headers=self.headers, cookies=self.cookies)
        return loads(req.text)

    def commentTweet(self, tweetId, text): #Comment tweet
        data = {
            'include_profile_interstitial_type':'1',
            'include_blocking':'1',
            'include_blocked_by':'1',
            'include_followed_by':'1',
            'include_want_retweets':'1',
            'include_mute_edge':'1',
            'include_can_dm':'1',
            'include_can_media_tag':'1',
            'skip_status':'1',
            'cards_platform':'Web-12',
            'include_cards':'1',
            'include_ext_alt_text':'true',
            'include_quote_count':'true',
            'include_reply_count':'1',
            'tweet_mode':'extended',
            'simple_quoted_tweet':'true',
            'trim_user':'false',
            'include_ext_media_color':'true',
            'include_ext_media_availability':'true',
            'auto_populate_reply_metadata':'true',
            'batch_mode':'subsequent',
            'in_reply_to_status_id':tweetId,
            'status':text
        }

        req = requests.post(self.url+'/1.1/statuses/update.json', data=data, headers=self.headers, cookies=self.cookies)
        return loads(req.text)

    def likeTweet(self, tweetId): #Favorite Tweet
        data = {
            'tweet_mode':'extended',
            'id':tweetId
        }
        req = requests.post(self.url+'/1.1/favorites/create.json', data=data, headers=self.headers, cookies=self.cookies)
        return loads(req.text)
    
    def getNotif(self, count=20): #Get your notifications 
        params = {
            'include_profile_interstitial_type':'1',
            'include_blocking':'1',
            'include_blocked_by':'1',
            'include_followed_by':'1',
            'include_want_retweets':'1',
            'include_mute_edge':'1',
            'include_can_dm':'1',
            'include_can_media_tag':'1',
            'skip_status':'1',
            'cards_platform':'Web-12',
            'include_cards':'1',
            'include_ext_alt_text':'true',
            'include_quote_count':'true',
            'include_reply_count':'1',
            'tweet_mode':'extended',
            'include_entities':'true',
            'include_user_entities':'true',
            'include_ext_media_color':'true',
            'include_ext_media_availability':'true',
            'send_error_codes':'true',
            'simple_quoted_tweet':'true',
            'count':count,
            'ext':'mediaStats%2ChighlightedLabel'
        }
        req = requests.get(self.url+'/2/notifications/all.json', params=params, headers=self.headers, cookies=self.cookies)
        glob = loads(req.text)['globalObjects']
        data = {
            "tweets": glob['tweets'],
            "users": glob['users']
            }
        return data

    def retweet(self, tweetId): #Retweet Post
        data = {
            'tweet_mode':'extended',
            'id': tweetId
        }

        req = requests.post(self.url+'/1.1/statuses/retweet.json', data=data, headers=self.headers, cookies=self.cookies)
        return loads(req.text)

    def destroyTweet(self, tweetId): #delete some of your tweet

        data = {
            'tweet_mode':'extended',
            'id':tweetId
        }

        req = requests.post(self.url+'/1.1/statuses/destroy.json', data=data, headers=self.headers, cookies=self.cookies)
        return loads(req.text)

    #BOT FUNCTIONS

    def addFuntion(self, func): # Add Bot function 
        self.botFunc.append(func)
        return True

    def bot(self): #Execute all bot functions
        for func in self.botFunc:
            func(self)

    def start(self, timer=15): #Start Bot in while True with the time sleep
        while True:
            self.bot()
            sleep(timer)
            
