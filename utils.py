from collections import Counter
from os import chdir
from attr import has
import pandas as pd
import numpy as np
import string
from wordcloud import STOPWORDS


class DataLoader:
    def __init__(self, dir_name, file_name):
        self.dir_name = dir_name
        self.file_name = file_name

    def read_csv(self):
        chdir(self.dir_name)
        tweets_df = pd.read_csv(self.file_name)
        # chdir("JupyterNotebooks")
        return tweets_df

def del_list_indexes(l, id_to_del):
    somelist = [i for j, i in enumerate(l) if j not in id_to_del]
    return somelist


def replace_chars(text, chars):
    for char in chars:
        text = text.replace(char, '')
    return text
def most_common_words_in_tweet(cleaned_df):
    cleaned_df['clean_text'] = cleaned_df['clean_text'].astype(str)
    cleaned_df['clean_text'] = cleaned_df['clean_text'].apply(
    lambda x: x.lower())
    cleaned_df['clean_text'] = cleaned_df['clean_text'].apply(
    lambda x: x.translate(str.maketrans(' ', ' ', string.punctuation)))
    
    return ' '.join(cleaned_df.clean_text.values)


def get_most_mentioned(cleaned_df):
    user_mention = cleaned_df['user_mentions'].map(np.array).values
    all_mentions= []
    for user in user_mention:
        user = user.strip("][").split(",")
        all_mentions += user
        
    all_mentions = list(map(lambda s: s.replace(
        " ", '').replace("'", ""), all_mentions))
    user_mention = " ".join(all_mentions)
    chars = ['\ufe0f',
             '\xe1',
             '\u0688',
             '\u062d',
             '\u06a9',
             '\u0648',
             '\u0645',
             '\u0646',
             '\u0627',
             '\u0638',
             '\u0631',
             '\u067e',
             '\u0691',
             '\u062a',
             '\u0679',
             '\u062a',
             '\u0939',
             '\u0932',
             '\u094d',
             '\u093e',
             '\u092c',
             '\u094b',
             '\u0432',
             '\u043e',
             '\u0439',
             '\u043d',
             '\u0430',
             '\u0441',
             # '\ufe0',
             # '\xe1',

             ]
    user_mention = replace_chars(user_mention, chars)
    return user_mention

def get_common_hashtags(cleaned_df, top):
    hashtags = cleaned_df['hashtags'].map(np.array).values
    all_hashtags = []
    for hashtag in hashtags:
        hashtag = hashtag.strip("][").split(",")
        all_hashtags += hashtag

    all_hashtags = list(map(lambda s: s.replace(
        " ", '').replace("'", ""), all_hashtags))
    hashtags = " ".join(all_hashtags)
    chars = ['\ufe0f',
             '\xe1',
             '\u0688',
             '\u062d',
             '\u06a9',
             '\u0648',
             '\u0645',
             '\u0646',
             '\u0627',
             '\u0638',
             '\u0631',
             '\u067e',
             '\u0691',
             '\u062a',
             '\u0679',
             '\u062a',
             '\u0939',
             '\u0932',
             '\u094d',
             '\u093e',
             '\u092c',
             '\u094b',
             '\u0432',
             '\u043e',
             '\u0439',
             '\u043d',
             '\u0430',
             '\u0441',
             # '\ufe0',
             # '\xe1',

             ]
    hashtags = replace_chars(hashtags, chars)
    # hashtags = del_list_indexes(hashtags, list(range(27639, 27645)))
    # hashtags = " ".join(hashtags)#[:75066]
    # print(len(hashtags))
    # hashtags = hashtags.encode('ascii', 'ignore')
    # print(len(hashtags))
    return hashtags

def retweets_polarity(df: pd.DataFrame) -> pd.DataFrame:
    rt_count = df[df['retweet_count'] > 0]['score'].value_counts()
    non_rt_count = df[df['retweet_count'] == 0]['score'].value_counts()
    return rt_count, non_rt_count
