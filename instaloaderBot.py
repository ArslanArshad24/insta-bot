import instaloader
from instaloader.exceptions import ProfileNotExistsException, LoginRequiredException

bot = instaloader.Instaloader()
acc = 'i_know_python'
# bot.download_profile(acc,profile_pic_only=True)


profile = instaloader.Profile.from_username(bot.context, 'username')

for story in bot.get_stories(userids=[profile.userid]):
    for item in story.get_items():
        bot.download_storyitem(item, target='downloaded_stories')
        
hashtag = instaloader.Hashtag.from_name(bot.context, 'hashtag',max_count=10,fast_update=True)
for post in hashtag.get_posts():
    bot.download_post(post, target='downloaded_hashtags')

post = instaloader.Post.from_shortcode(bot.context, 'shortcode')
print(post.caption)
print(post.date_utc)
print(post.likes)
if post.is_video:
    bot.download_post(post, target='downloaded_videos')
comments = post.get_comments()
for comment in comments:
    print(comment.text)


loader = Instaloader()
loader.load_session_from_file('USER')
loader.download_feed_posts(max_count=20, fast_update=True,post_filter=lambda post: post.viewer_has_liked)

loader.download_location(362629379, max_count=30)  # login required

bot.download_profilepic(profile=profile)
bot.download_video_thumbnails()
bot.get_location_posts(location='location number')
bot.save_location(filename='')
bot.two_factor_login(two_factor_code='')

 
followers = profile.get_followers()
for follower in followers:
    print(follower.username)

followees = profile.get_followees()
for followee in followees:
    print(followee.username)


bot.login('your_username', 'your_password')  # required to download private videos and some other


saved_posts = bot.get_saved_posts()
for post in saved_posts:
    bot.download_post(post, target='downloaded_saved_posts')
