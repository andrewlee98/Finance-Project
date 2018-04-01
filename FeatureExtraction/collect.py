from twitterscraper import query_tweets
import json
import re
import datetime as dt

if __name__ == '__main__':

    data = query_tweets("eth", limit=100, begindate=dt.date(2018,2,16), enddate=dt.date.today())

    tweetlist = []

    # writing tweets to file while cleaning
    with open("raw_tweets.txt", encoding='utf-8', mode = "w") as f:
        for tweet in data:
            time = str(tweet.timestamp)

            # filter out non-ASCII
            if not bool(re.search('^[\x00-\x7F]+$', tweet.text)):
                continue

            #remove links
            text = re.sub(r"http\S+", "", tweet.text)
            text = text.replace('\n', ' ').replace('\r', '')

            # write to file
            f.write(time + "\n")
            f.write(text + "\n")
            f.write("-------------------------------\n\n")

            tweetlist.append((text,time))

    print(str(len(tweetlist)) + " good tweets from " + str(len(data)))

    # labeling
    with open("labeled_clean_tweets.txt", encoding='utf-8', mode = "w") as l:
        for tup in tweetlist:

            print(tup[1])
            print(tup[0])
            senti = input("0, 1, or 2: ")

            # write to file using ~~~ as delimiter
            l.write(tup[1])
            l.write("\n")
            l.write(tup[0])
            l.write("\n")
            l.write(senti)
            l.write("\n")

            print("-------------------------------\n\n")
