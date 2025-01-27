import praw

reddit = praw.Reddit(
    client_id='MJIIVc_Hy1y4uBKHUVBq0g',
    client_secret='zBEcybfj_DDhchk5N1MxQVpYfR-KwQ',
    user_agent='windows:com.example.myredditapp:v1.2.3 (by u/SneakyRatSausage)'
)

# print(reddit.read_only)

words = []

for submission in reddit.subreddit('Eesti').hot(limit=10):
    submission.comments.replace_more(limit=0)
    for top_level_comment in submission.comments:
        word = ''
        for letter in top_level_comment.body:
            if(letter == ' '):
                if(word and not word[-1].isalnum()):
                    word = word [:1]
                words.append(word.strip())
                word = ''
            else:
                word += letter

wordCount = {}

for word in words:
    if word in wordCount:
        wordCount[word] += 1
    else:
        wordCount[word] = 1

sortedList = sorted(wordCount, key = wordCount.get, reverse = True)
sortedList = sortedlist[:10]
print(sortedList)