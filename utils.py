from collections import Counter
from os import chdir
from attr import has
import pandas as pd
import numpy as np
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


def get_tweet_words(df):
    # custom_stopwords = ['t', 'rt', 'ti', 'vk', 'to', 'co',
    #                 'dqlw', 'z', 'nd', 'm', 's', 'kur', 'u', 'o', 'd']#,
    #                 # "will", "new", "amp"]
    # STOP_WORDS = STOPWORDS.union(custom_stopwords)
    df['clean_text'] = df['clean_text'].apply(
        lambda x: [item for item in x.split()])
    sentence_list = df['clean_text'].to_list()
    words = []
    for ele in sentence_list:
        for w in ele:
            words.append(w.strip("#"))
    # print(STOPWORDS)
    words = " ".join(words)
    return words
    # word_list = [sent for sent in sentence_list]
    # print(word_list[:5])
    # texts = df['original_text'].values
    # print(texts)


def retweets_polarity(df: pd.DataFrame) -> pd.DataFrame:
    rt_count = df[df['retweet_count'] > 0]['score'].value_counts()
    non_rt_count = df[df['retweet_count'] == 0]['score'].value_counts()
    return rt_count, non_rt_count
