create table labled_tweets_information(
    created_at	Date, 
    source text ,	
    clean_text text,	
    polarity float,	
    subjectivity float,	
    lang CHAR(4),
    favorite_count int	,
    retweet_count int,
    original_author text,
    followers_count	int,
    friends_count	int,
    possibly_sensitive BOOLEAN,	
    hashtags	text,
    user_mentions	text,
    place	text,
    score text,
    scoremap int);

