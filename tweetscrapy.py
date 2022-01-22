import os
import pandas as pd

# Below are two ways of scraping using CLI commands.
# Comment or uncomment as you need. If you currently run the script as is it will scrape both queries
# then output two different csv files.


# Query by text search
# Setting variables to be used in format string command below
tweet_count = 100
text_query = "metaverse"
since_date = "2021-08-26"
until_date = "2021-08-31"

# Using OS library to call CLI commands in Python
os.system('snscrape --jsonl --max-results {} --since {} twitter-search "{} until:{}"> metaverse.json'.format(tweet_count, since_date, text_query, until_date))

# Reads the json generated from the CLI command above and creates a pandas dataframe
tweets_df2 = pd.read_json('metaverse.json', lines=True)

# Displays first 5 entries from dataframe
# tweets_df2.head()

# Export dataframe into a CSV
tweets_df2.to_csv('metaverse.csv', sep=',', index=False)