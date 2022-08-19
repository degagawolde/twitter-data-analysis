import json
import re
from pprint import pprint
from traceback import print_exc
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy import inspect
from sqlalchemy.dialects.mysql import mysqlconnector
from sqlalchemy.dialects import mysql
from clean_tweets_dataframe import Clean_Tweets
from preprocess_tweet_data import DataPreparation
from utils import DataLoader
from urllib.parse import quote

import streamlit as st

LABLED_SCHEMA = "labled_schema.sql"
CLEANED_SCHEMA = "cleaned_schema.sql"

CSV_PATH = "processed_tweet_data.csv"


# with open("db_cred.json", 'r') as f:
#     config = json.load(f)

# Connect to the database
connections_path = "mysql+pymysql://root:root#123@localhost/twitter_data"
engine = create_engine(connections_path)

# Create the tables
def create_tables():
    try:
        with engine.connect() as conn:
            for name in [LABLED_SCHEMA, CLEANED_SCHEMA]:
                with open(name) as file:
                    query = text(file.read())
                    conn.execute(query)
        print("Successfully created 2 tables")
    except:
        print("Unable to create the Tables")
        print(print_exc())

# Read the data
def get_data(labled=False):
    loader = DataLoader('./', CSV_PATH)
    tweets_df = loader.read_csv()
    print("Got the dataframe")
    cleaner = Clean_Tweets(tweets_df)
    cleand_df = cleaner.clean_tweet(tweets_df)
    cleand_df['hashtags'] = cleand_df['hashtags'].apply(lambda x: "".join(x))
    
    cleand_df['hashtags'] = cleand_df['hashtags'].str.replace(
        "[^a-zA-Z0-9]", " ", regex=True)
    
    cleand_df['user_mentions'] = cleand_df['user_mentions'].apply(
        lambda x: "".join(x))
    cleand_df['source'] = cleand_df['source'].str.replace(
        "[^a-zA-Z]", " ", regex=True)
    if labled:
        return cleand_df

    process = DataPreparation(cleand_df)
    labled_df = process.create_score(cleand_df)
    labled_df = process.create_scoremap(cleand_df)
    return cleand_df, labled_df

# Populate the tables
def insert_data(df: pd.DataFrame, table_name):
    try:
        with engine.connect() as conn:
            df.to_sql(name=table_name, con=conn,
                      if_exists='replace', index=False)
        print(f"Done inserting to {table_name}")
    except:
        print("Unable to insert to table")
        print(print_exc())

# Implement Querying functions
def get_table_names():
    with engine.connect() as conn:
        inspector = inspect(conn)
        names = inspector.get_table_names()
        return names


@st.cache
def get_labled_tweets():
    with engine.connect() as conn:
        labled_df = pd.read_sql_table('labled_tweets_information', con=conn)
        return labled_df


@st.cache
def get_cleaned_tweets():
    with engine.connect() as conn:
        cleand_df = pd.read_sql_table('cleaned_tweets_information', con=conn)

        return cleand_df

if __name__ == "__main__":
    create_tables()
    cleand_df, labled_df = get_data()
    print(cleand_df['hashtags'].iloc[65])
    print(cleand_df['hashtags'].iloc[66])
    print(cleand_df['hashtags'].iloc[67])
    
    print(labled_df['hashtags'].iloc[65])
    print(labled_df['hashtags'].iloc[66])
    print(labled_df['hashtags'].iloc[67])
    print(cleand_df.info())
    print(labled_df.info())
    insert_data(labled_df, "labled_tweets_information")
    insert_data(cleand_df, "cleaned_tweets_information")
