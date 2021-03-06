To query tweets, run `./query.sh <query>`

	where `<query>` is a list of keywords seperated by comma (`,`). The query can be any thing (keyword, hashtag, etc.) you want to search in [Twitter Search](https://twitter.com/search-home). `TweetScraper` will crawl the search results of the query and save the tweet content and user information. You can also use the following operators in each query (from [Twitter Search](https://twitter.com/search-home)):
	
| Operator | Finds tweets... |
| --- | --- |
| twitter search | containing both "twitter" and "search". This is the default operator. |
| **"** happy hour **"** | containing the exact phrase "happy hour". |
| love **OR** hate | containing either "love" or "hate" (or both). |
| beer **-** root | containing "beer" but not "root". |
| **#** haiku | containing the hashtag "haiku". |
| **from:** alexiskold | sent from person "alexiskold". |
| **to:** techcrunch | sent to person "techcrunch". |
| **@** mashable | referencing person "mashable". |
| "happy hour" **near:** "san francisco" | containing the exact phrase "happy hour" and sent near "san francisco". |
| **near:** NYC **within:** 15mi | sent within 15 miles of "NYC". |
| superhero **since:** 2010-12-27 | containing "superhero" and sent since date "2010-12-27" (year-month-day). |
| ftw **until:** 2010-12-27 | containing "ftw" and sent up to date "2010-12-27". |
| movie -scary **:)** | containing "movie", but not "scary", and with a positive attitude. |
| flight **:(** | containing "flight" and with a negative attitude. |
| traffic **?** | containing "traffic" and asking a question. |
| hilarious **filter:links** | containing "hilarious" and linking to URLs. |
| news **source:twitterfeed** | containing "news" and entered via TwitterFeed |


For example you could run `./query.sh #bitcoin`. 

The resulting tweets would then be saved in Mongo under database `TweetScraper` and collection `#bitcoin`
