import xai
import pandas as pd

df = pd.read_csv('../../outputs/lol/dataset_players_statistics.csv')
bal_df = xai.balance(df, "result", upsample=0.8)