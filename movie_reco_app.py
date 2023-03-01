import pandas as pd

# import movie dataset
credits_df = pd.read_csv('tmdb_5000_credits.csv')
movies_df = pd.read_csv('tmdb_5000_movies.csv')

# combine two files
credits_df.columns = ['id', 'title', 'cast', 'crew']
movies_df = movies_df.merge(credits_df, on='id')
