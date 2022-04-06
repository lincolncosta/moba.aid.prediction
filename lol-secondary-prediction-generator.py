import pandas as pd
from dateutil.relativedelta import relativedelta
from tqdm import tqdm
from datetime import datetime as dt
import csv


def processGames(game, side):

    if isinstance(game, str):

        datacompleteness = df[(df['gameid'] == game) & (df['side'] == side)
                              & (df['position'] == 'top')].datacompleteness.values[0]
        if datacompleteness != 'complete':
            return

        # BLUE TEAM
        top = df[(df['gameid'] == game) & (df['side'] == side)
                 & (df['position'] == 'top')].champion.values[0]
        topPlayer = df[(df['gameid'] == game) & (df['side'] == side) & (
            df['position'] == 'top')].playername.values[0]
        if (topPlayer != 'unknown player'):
            top = int(
                df_champions.loc[df_champions['id'] == top]['key'])
        else:
            return

        jungle = df[(df['gameid'] == game) & (df['side'] == side) & (
            df['position'] == 'jng')].champion.values[0]
        junglePlayer = df[(df['gameid'] == game) & (
            df['side'] == side) & (df['position'] == 'jng')].playername.values[0]
        if (junglePlayer != 'unknown player'):
            jungle = int(
                df_champions.loc[df_champions['id'] == jungle]['key'])
        else:
            return

        mid = df[(df['gameid'] == game) & (df['side'] == side)
                 & (df['position'] == 'mid')].champion.values[0]
        midPlayer = df[(df['gameid'] == game) & (df['side'] == side) & (
            df['position'] == 'mid')].playername.values[0]
        if (midPlayer != 'unknown player'):
            mid = int(
                df_champions.loc[df_champions['id'] == mid]['key'])
        else:
            return

        carry = df[(df['gameid'] == game) & (df['side'] == side) & (
            df['position'] == 'bot')].champion.values[0]
        carryPlayer = df[(df['gameid'] == game) & (
            df['side'] == side) & (df['position'] == 'bot')].playername.values[0]
        if (carryPlayer != 'unknown player'):
            carry = int(
                df_champions.loc[df_champions['id'] == carry]['key'])
        else:
            return

        supp = df[(df['gameid'] == game) & (df['side'] == side) & (
            df['position'] == 'sup')].champion.values[0]
        suppPlayer = df[(df['gameid'] == game) & (
            df['side'] == side) & (df['position'] == 'sup')].playername.values[0]
        if (suppPlayer != 'unknown player'):
            supp = int(
                df_champions.loc[df_champions['id'] == supp]['key'])
        else:
            return

        # RESULT
        kills = df[(df['gameid'] == game) & (df['side'] == side)
                   & (df['position'] == 'team')].teamkills.values[0]
        deaths = df[(df['gameid'] == game) & (df['side'] == side)
                    & (df['position'] == 'team')].teamdeaths.values[0]
        towers = df[(df['gameid'] == game) & (df['side'] == side)
                    & (df['position'] == 'team')].towers.values[0]
        dragons = df[(df['gameid'] == game) & (df['side'] == side)
                     & (df['position'] == 'team')].dragons.values[0]
        heralds = df[(df['gameid'] == game) & (df['side'] == side)
                     & (df['position'] == 'team')].heralds.values[0]
        barons = df[(df['gameid'] == game) & (df['side'] == side)
                    & (df['position'] == 'team')].barons.values[0]
        inhibitors = df[(df['gameid'] == game) & (df['side'] == side)
                        & (df['position'] == 'team')].inhibitors.values[0]
        firstBlood = df[(df['gameid'] == game) & (df['side'] == side)
                        & (df['position'] == 'team')].firstblood.values[0]
        firstTower = df[(df['gameid'] == game) & (df['side'] == side)
                        & (df['position'] == 'team')].firsttower.values[0]
        firstHerald = df[(df['gameid'] == game) & (df['side'] == side)
                         & (df['position'] == 'team')].firstherald.values[0]

        if side == 'Blue':
            flagSide = 1
        else:
            flagSide = 0

        # WRITING TO DATASET FILE
        with open('outputs/lol/secondary-prediction.csv', mode='a', newline="", encoding='utf-8') as datasetSecondary2022:
            datasetWriter = csv.writer(datasetSecondary2022, delimiter=',')
            datasetWriter.writerow([game, flagSide, topPlayer, top, junglePlayer, jungle, midPlayer, mid, carryPlayer,
                                   carry, suppPlayer, supp, kills, deaths, firstBlood, firstTower, firstHerald, dragons, barons, inhibitors, towers, heralds])


df = pd.read_csv("data/secondary-prediction/mess_dataset_22.csv")
df21 = df.copy()
df_champions = pd.read_csv('data/dataset_champions.csv')
games = df21.gameid.drop_duplicates()
sides = ['Blue', 'Red']

header = 'game,side,topPlayer,top,junglePlayer,jungle,midPlayer,mid,carryPlayer,carry,suppPlayer,supp,kills,deaths,firstBlood,firstTower,firstHerald,dragons,barons,inhibitors,towers,heralds\n'
with open('outputs/lol/secondary-prediction.csv', mode='a', encoding='utf-8') as dataset:
    dataset.write(header)

for game in tqdm(games):
    for side in sides:
        processGames(game, side)
