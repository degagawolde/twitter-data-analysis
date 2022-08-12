from clean_tweets_dataframe import Clean_Tweets
from extract_dataframe import read_json
import unittest
import pandas as pd
import sys
import os

sys.path.append(os.path.abspath(os.path.join("./..")))

# put here the path to where you placed the file e.g. ./sampletweets.json.
sampletweets_df = "processed_tweet_data.csv"
clean_tweet_df = pd.read_csv(sampletweets_df)


class TestCleanTweet(unittest.TestCase):
    """
		A class for unit-testing function in the clean_tweets_dataframe.py file

		Args:
        -----
			unittest.TestCase this allows the new class to inherit
			from the unittest module
	"""

    def setUp(self) -> pd.DataFrame:
        self.clt = Clean_Tweets(clean_tweet_df[:5])
        self.df = clean_tweet_df[:5]
        self.numerical_columns = ['polarity', 'subjectivity',
                                  'retweet_count', 'favorite_count',
                                  'followers_count', 'friends_count']

    def test_drop_unwanted_rows(self):
        self.assertIsNotNone(
            self.clt.drop_duplicate(self.df)
        )

    def test_convert_to_numbers(self):
        for column in self.numerical_columns[:2]:
            self.assertEqual(str(self.df[column].dtype), 'float64')
        for column in self.numerical_columns[2:]:
            self.assertEqual(str(self.df[column].dtype), 'int64')

if __name__ == "__main__":
    unittest.main()
