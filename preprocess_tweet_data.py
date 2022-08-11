import pandas as pd
import string
from gensim import corpora

def text_category(p) -> str:
    if p < 0:
        return 'negative'
    elif p == 0:
        return 'neutral'
    else:
        return 'positive'
    
class DataPreparation:
    def __init__(self,df:pd.DataFrame)->pd.DataFrame:
        self.df = df
    def create_score(self,df:pd.DataFrame)->pd.DataFrame:
        df['score'] = df['polarity'].apply(text_category)
        return df
    def create_scoremap(self, df: pd.DataFrame) -> pd.DataFrame:
        #remove the neutral rows
        df = df[df['polarity']!=0] 
        df.reset_index()
        df['scoremap'] = df['score'].apply(
            lambda x: 0 if x == 'negative' else 1)
        return df
    
    def preprocess_data(self):

        #text Preprocessing
        tweets_df = self.df.loc[self.df['lang'] == "en"]
        
        #convert to string and to lowercase
        tweets_df['clean_text'] = tweets_df['clean_text'].astype(str)
        tweets_df['clean_text'] = tweets_df['clean_text'].apply(
        lambda x: x.lower())
        
        #remove punctuation from the text
        tweets_df['clean_text'] = tweets_df['clean_text'].apply(
        lambda x: x.translate(str.maketrans(' ', ' ', string.punctuation)))
 
        #Converting tweets to list of words For feature engineering
        sentence_list = [tweet for tweet in tweets_df['clean_text']]
        word_list = [sent.split() for sent in sentence_list]
        # print(word_list)

        #Create dictionary which contains Id and word 
        word_to_id = corpora.Dictionary(word_list) #generate unique tokens
        # we can see the word to unique integer mapping
        
        # using bag of words(bow), we create a corpus that contains the word id and its frequency in each document.
        corpus_1= [word_to_id.doc2bow(tweet) for tweet in word_list]
        # TFIDF

        return word_list, word_to_id, corpus_1
        