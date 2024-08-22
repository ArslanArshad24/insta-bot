from instabot import Bot

name = ''
passw = ''

bot = Bot()
bot.login(username=name, password=passw)
bot.upload_photo('man.jpg',caption='Hacking Man', )

bot.follow('Elon Musk')

bot.send_message('Hello, i AM Hacking Man',['Adnan','Ahmad'])


followers =  bot.get_user_followers('HackinG Man')
for follower in followers:
    follower_info = bot.get_user_info(follower)
    
bot.unfollow_everyone()
bot.unfollow_non_followers()

######################## Advance Bot Methods %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

bot = Bot()
bot.login(username=name, password= passw,proxy='Proxies', use_cookie='cokkies', cookie_fname='cookies.txt', force = False)
bot.logout()

### GET ABOUT USER
bot.get_user_id_from_username('name')
bot.get_username_from_user_id('user_id')
# bot.get_your_medias('username or user_id')
bot.get_user_followers(user_id='user_id')
bot.get_user_following(user_id='user_id')

### GET MEDIA
bot.get_media_id_from_link('link')
bot.get_link_from_media_id('id')
bot.get_user_medias(user_id='username => get last 20 medias',filtration=True,is_comment=True)
bot.get_hashtag_medias(hashtag='arslan',filtration=True)

### GET USERS
bot.get_timeline_users()
bot.get_hashtag_users(hashtag='arslan')
bot.get_comment_likers(comment_id='')
bot.get_media_commenters(media_id='')

### GET Comments
bot.get_media_comments(media_id='',only_text=False)
bot.get_media_comments_all(media_id='',only_text=False)

# Likes
bot.like(media_id='')
bot.like_medias(media_ids=['',''])

bot.like_comment(comment_id='')

bot.like_timeline()

bot.like_user(user_id='',filtration=True) # it will like last post
bot.like_users(user_ids=['',''],filtration=True)


bot.like_hashtag(hashtag='')


bot.unlike(media_id='')
bot.unlike_medias(media_ids=(['','','']))


#%%% Follows
bot.follow(user_id='')
bot.follow_users(user_ids=['','',''])

bot.unfollow(user_id='')
bot.unfollow_users(user_ids=['','',''])

bot.unfollow_non_followers()

#%%% Photos
bot.upload_photo(photo='',caption='Nice Pic')
bot.upload_story_photo(photo='')
bot.upload_video(video='',caption='')

bot.download_photo(media_id='',folder='photos',filename=None)
bot.download_photos(medias=['','',''])
bot.download_stories(username='')
bot.download_video(media_id='',folder='videos')


#### %%%%%%%%%%%%%%%%%%%%%%% Default Value %%%%%%%%%%%%%%%%%%%%%%%%%% 
bot = Bot(max_likes_to_like=200, #If the media has more likes then this value — it will be ignored and not be liked.
          max_followers_to_follow=2000,
          min_followers_to_follow=10,
          max_following_to_follow=10000,
          min_following_to_follow=10,
          max_followers_to_following_ratio=10,
          max_following_to_followers_ratio=2,
          min_media_count_to_follow=3,
          stop_words=['shop', 'store', 'free'],
          max_likes_per_day=1000,
          max_unlikes_per_day=1000,
          max_follows_per_day=350,
          max_unfollows_per_day=350,
          max_comments_per_day=100,
          filter_users=True,
          filter_business_accounts=True,
          filter_verified_accounts= True,
          max_following_to_block=2000,
          like_delay=10,
          unlike_delay=10,
          follow_delay=30,
          unfollow_delay=30,
          comment_delay=60,
        # whitelist='whitelist.txt'
        # blacklist='blacklist.txt',
        # comments_file='comments.txt'
        # base_path='./',
        # stop_words=['shop', 'store', 'free'],
          )