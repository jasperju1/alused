#https://medium.com/@carrascalx/i-wrote-a-python-program-calculate-the-most-commonly-used-words-in-subreddits-heres-what-i-found-584ff946a8dc
# Loe läbi artikkel.
# Kas suudad mõista ja selgitada, mis on API?
# Kas suudad mõista ja selgitada, mis on pip?	
# Kui saad aru, mis on PRAW, siis installi see ja testi, kas töötab. (vihjed: https://praw.readthedocs.io/en/latest/getting_started/quick_start.html,
# https://www.reddit.com/prefs/apps/, https://www.reddit.com/r/redditdev/comments/5mzts3/what_do_you_put_in_for_redirect_uri_i_keep/)
# Leia analoogselt artiklist kirjeldatule enim kasutatud sõnad r/Eesti sub-redditis.


import praw
import matplotlib.pyplot as plt

reddit = praw.Reddit(
    client_id='MJIIVc_Hy1y4uBKHUVBq0g',
    client_secret='zBEcybfj_DDhchk5N1MxQVpYfR-KwQ',
    user_agent='windows:com.example.myredditapp:v1.2.3 (by u/SneakyRatSausage)'
)

# print(reddit.read_only)

words = []

commonWords = ['on', 'ja', 'et', 'ei', 'see', 'kui', 'ka', 'aga', 'siis', '', 'seda', 'oma', 'oli', 'mis', 'sa', 'saab', 'ta', 'või', 'palju', 'ole', 'ning', 'kas', 'need', 'selle', 'kes', 'ise', 'pole','mida', 'nagu', 'väga', 'ma', 'ikka', 'nüüd''ära', 'olla', 'kuidas', 'oleks',]


for submission in reddit.subreddit("Eesti").hot(limit=5):
    submission.comments.replace_more(limit=0)
    for top_level_comment in submission.comments:
        word = ""
        for letter in top_level_comment.body:
            if letter == " ":
                if word and not word[-1].isalnum():
                    word = word[:-1]
                word = word.strip().lower()
                if word not in commonWords:
                    words.append(word)
                word = ""
            else:
                word += letter

wordCount = {}

for word in words:
    if word in wordCount:
        wordCount[word] += 1
    else:
        wordCount[word] = 1


sortedList = sorted(wordCount, key = wordCount.get, reverse = True)

keyWords = sortedList[:10]
keyCount = []

for w in keyWords:
    keyCount.append(wordCount[w])

print(keyWords, keyCount)

plt.title('Top comments for r/Eesti')
plt.pie(keyCount, labels=keyWords, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')

plt.savefig('eesti.png')
# plt.show()