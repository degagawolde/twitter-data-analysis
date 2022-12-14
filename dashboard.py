import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

from mysql_manager import get_labled_tweets
from mysql_manager import get_cleaned_tweets
from utils import get_common_hashtags, get_most_mentioned, most_common_words_in_tweet, retweets_polarity
from wordcloud import STOPWORDS, WordCloud
from nltk.corpus import stopwords

import nltk
nltk.download('stopwords')

STOP_WORDS = list(set(stopwords.words('english')).union(['t', 'rt', 'ti', 'vk', 'to',
                                                         'co','dqlw', 'z', 'nd', 'm', 
                                                         's', 'kur', 'u', 'o', 'd']).union(STOPWORDS))

st.title('Twitter Data Analysis')
st.markdown("""
    This app performs simple global twitter analysis
    * **Python libraries:** base64, pandas, streamlit
    * **Data Source:** [Twitter Da]
            
            """)
st.sidebar.header("Actions")
select_action = st.sidebar.selectbox('Ojective',list(reversed([
    'Explaratory Data Analysis',
    'Sentimental Analysis',
    'Topic Modeling'])))

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.

def get_pie_plot(labels, values):
    fig = go.Figure(
        go.Pie(
            labels=labels,
            values=values,
            hoverinfo="label+percent"
        ))
    fig.update_traces(textfont_size=20)
    fig.update_layout(legend=dict(font=dict(size=20)),
                      hoverlabel=dict(font_size=16))
    return fig

def get_wordcloud(words):
    wordcloud = WordCloud(stopwords=STOP_WORDS, width=800,
                          height=400).generate(words)
    wordcloud = wordcloud.to_image()

    return wordcloud

# @st.cache
def load_labled_data():
    return get_labled_tweets()


# @st.cache
def load_cleaned_data():
    return get_cleaned_tweets()


labled_df = load_labled_data()
cleaned_df = load_cleaned_data()

# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...finished!')

if st.checkbox('Show Labled Data'):
    st.subheader('Labled Data')
    st.dataframe(labled_df)

if st.checkbox('Show Cleaned Data'):
    st.subheader('Cleaned Data')
    st.dataframe(cleaned_df)

st.subheader('Hashtags wordcloud - the most common hashtags')
hashtags = get_common_hashtags(cleaned_df, len(cleaned_df))

ht_wordcloud = get_wordcloud(hashtags)
st.image(ht_wordcloud)

st.subheader('UserMentions wordcloud - the most mentioned users')
mentions = get_most_mentioned(cleaned_df)

mnt_wordcloud = get_wordcloud(mentions)
st.image(mnt_wordcloud)

tweet_words = most_common_words_in_tweet(cleaned_df)
print(len(tweet_words))
tweets_wordcloud = get_wordcloud(tweet_words)
print(type(tweets_wordcloud))
st.subheader('Tweet wordcloud - most common words in the tweets')
st.image(tweets_wordcloud)

# get_tweet_words(cleaned_df)
st.subheader('Tweet sources')
st.bar_chart(cleaned_df['source'].value_counts(), height=500)

st.subheader(
    "The 3 most common sources(Web, iPhone and Android).\nAnd the sentiment from each looks like this")
sources_df = labled_df[labled_df['source'].isin(
    ["twitter web app", "twitter for android", "twitter for iphone"])]
sources = sources_df.groupby('source')['score'].value_counts()
fig2 = get_pie_plot(sources.keys(), sources)
st.plotly_chart(fig2, width=100)

common_source = st.sidebar.multiselect(
    'Tweet Source', 
    [x for x in sources_df['source'].value_counts().keys()], 
    [y for y in sources_df['source'].value_counts().keys()])

common_source = st.sidebar.multiselect(
    'Tweet Source',
    [x for x in sources_df['source'].value_counts().keys()],
    [y for y in sources_df['source'].value_counts().keys()])

# plot sentiment
st.subheader('Tweet Sentiments(positive VS negative)')
sentiment_ratio = labled_df['score'].value_counts()

fig = get_pie_plot(sentiment_ratio.keys(), sentiment_ratio)
st.plotly_chart(fig)

st.subheader('Retwetted vs non-Retweeted tweets polarity')
# retweeted, non_retweeted = st.columns(2)
rt_count, non_rt_count = retweets_polarity(labled_df)
rt_fig = get_pie_plot(rt_count.keys(), rt_count)
non_rt_fig = get_pie_plot(non_rt_count.keys(), non_rt_count)
# with retweeted:
st.plotly_chart(rt_fig, width=50)

# with non_retweeted:
st.plotly_chart(non_rt_fig, width=50)
