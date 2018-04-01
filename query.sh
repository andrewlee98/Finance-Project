export MONGODB_TWEET_COLLECTION=$1;
scrapy crawl TweetScraper -a query=$1;