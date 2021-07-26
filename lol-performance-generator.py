import pandas as pd
from dateutil.relativedelta import relativedelta
from tqdm import tqdm
from datetime import datetime as dt
import csv


def gatherPlayerInfo(player, champion, formatedStartDate, formatedEndDate, game, position):

    gp = 0
    wr = 0
    kda = 0

    matches = df[(df['player'] == player) & (df['position'] == position) & (df['date'] >= formatedStartDate) & (
        df['date'] <= formatedEndDate) & (df['gameid'] != game) & (df['champion'] == champion)]
    if len(matches):
        matches_won = matches[(matches['side'] == 'Blue') & (matches['result'] == 1) | (
            matches['side'] == 'Red') & (matches['result'] == 0)]
        kills = matches['kills'].sum()
        deaths = matches['deaths'].sum() if matches['deaths'].sum() != 0 else 1
        assists = matches['assists'].sum()
        kda = (kills + assists)/deaths
        gp = len(matches)
        wr = len(matches_won)/len(matches)

    return gp, round(wr, 2), round(kda, 2)


def processGames(game):

    if isinstance(game, str):

        # GAME DATETIME
        endDate = dt.strptime(
            df[(df['gameid'] == game)].date.values[0], '%Y-%m-%d %H:%M:%S')
        startDate = endDate - relativedelta(months=6)
        formatedEndDate = endDate.strftime('%Y-%m-%d %H:%M:%S')
        formatedStartDate = startDate.strftime('%Y-%m-%d %H:%M:%S')

        # BLUE TEAM
        blueTop = df[(df['gameid'] == game) & (df['side'] == 'Blue')
                     & (df['position'] == 'top')].champion.values[0]
        blueTopPlayer = df[(df['gameid'] == game) & (df['side'] == 'Blue') & (
            df['position'] == 'top')].player.values[0]
        if (blueTopPlayer != 'unknown player'):
            crawler = gatherPlayerInfo(
                blueTopPlayer, blueTop, formatedStartDate, formatedEndDate, game, 'top')
            blueTop = int(
                df_champions.loc[df_champions['id'] == blueTop]['key'])
            if (crawler):
                blueTopGP = crawler[0]
                blueTopWR = crawler[1]
                blueTopKDA = crawler[2]
            else:
                return
        else:
            return

        blueJungle = df[(df['gameid'] == game) & (df['side'] == 'Blue') & (
            df['position'] == 'jng')].champion.values[0]
        blueJunglePlayer = df[(df['gameid'] == game) & (
            df['side'] == 'Blue') & (df['position'] == 'jng')].player.values[0]
        if (blueJunglePlayer != 'unknown player'):
            crawler = gatherPlayerInfo(
                blueJunglePlayer, blueJungle, formatedStartDate, formatedEndDate, game, 'jng')
            blueJungle = int(
                df_champions.loc[df_champions['id'] == blueJungle]['key'])
            if (crawler):
                blueJungleGP = crawler[0]
                blueJungleWR = crawler[1]
                blueJungleKDA = crawler[2]
            else:
                return
        else:
            return

        blueMid = df[(df['gameid'] == game) & (df['side'] == 'Blue')
                     & (df['position'] == 'mid')].champion.values[0]
        blueMidPlayer = df[(df['gameid'] == game) & (df['side'] == 'Blue') & (
            df['position'] == 'mid')].player.values[0]
        if (blueMidPlayer != 'unknown player'):
            crawler = gatherPlayerInfo(
                blueMidPlayer, blueMid, formatedStartDate, formatedEndDate, game, 'mid')
            blueMid = int(
                df_champions.loc[df_champions['id'] == blueMid]['key'])
            if (crawler):
                blueMidGP = crawler[0]
                blueMidWR = crawler[1]
                blueMidKDA = crawler[2]
            else:
                return
        else:
            return

        blueCarry = df[(df['gameid'] == game) & (df['side'] == 'Blue') & (
            df['position'] == 'bot')].champion.values[0]
        blueCarryPlayer = df[(df['gameid'] == game) & (
            df['side'] == 'Blue') & (df['position'] == 'bot')].player.values[0]
        if (blueCarryPlayer != 'unknown player'):
            crawler = gatherPlayerInfo(
                blueCarryPlayer, blueCarry, formatedStartDate, formatedEndDate, game, 'bot')
            blueCarry = int(
                df_champions.loc[df_champions['id'] == blueCarry]['key'])
            if (crawler):
                blueCarryGP = crawler[0]
                blueCarryWR = crawler[1]
                blueCarryKDA = crawler[2]
            else:
                return
        else:
            return

        blueSupp = df[(df['gameid'] == game) & (df['side'] == 'Blue') & (
            df['position'] == 'sup')].champion.values[0]
        blueSuppPlayer = df[(df['gameid'] == game) & (
            df['side'] == 'Blue') & (df['position'] == 'sup')].player.values[0]
        if (blueSuppPlayer != 'unknown player'):
            crawler = gatherPlayerInfo(
                blueSuppPlayer, blueSupp, formatedStartDate, formatedEndDate, game, 'sup')
            blueSupp = int(
                df_champions.loc[df_champions['id'] == blueSupp]['key'])
            if (crawler):
                blueSuppGP = crawler[0]
                blueSuppWR = crawler[1]
                blueSuppKDA = crawler[2]
            else:
                return
        else:
            return

        # RED TEAM
        redTop = df[(df['gameid'] == game) & (df['side'] == 'Red')
                    & (df['position'] == 'top')].champion.values[0]
        redTopPlayer = df[(df['gameid'] == game) & (df['side'] == 'Red') & (
            df['position'] == 'top')].player.values[0]
        if (redTopPlayer != 'unknown player'):
            crawler = gatherPlayerInfo(
                redTopPlayer, redTop, formatedStartDate, formatedEndDate, game, 'top')
            redTop = int(df_champions.loc[df_champions['id'] == redTop]['key'])
            if (crawler):
                redTopGP = crawler[0]
                redTopWR = crawler[1]
                redTopKDA = crawler[2]
            else:
                return
        else:
            return

        redJungle = df[(df['gameid'] == game) & (df['side'] == 'Red') & (
            df['position'] == 'jng')].champion.values[0]
        redJunglePlayer = df[(df['gameid'] == game) & (
            df['side'] == 'Red') & (df['position'] == 'jng')].player.values[0]
        if (redJunglePlayer != 'unknown player'):
            crawler = gatherPlayerInfo(
                redJunglePlayer, redJungle, formatedStartDate, formatedEndDate, game, 'jng')
            redJungle = int(
                df_champions.loc[df_champions['id'] == redJungle]['key'])
            if (crawler):
                redJungleGP = crawler[0]
                redJungleWR = crawler[1]
                redJungleKDA = crawler[2]
            else:
                return
        else:
            return

        redMid = df[(df['gameid'] == game) & (df['side'] == 'Red')
                    & (df['position'] == 'mid')].champion.values[0]
        redMidPlayer = df[(df['gameid'] == game) & (df['side'] == 'Red') & (
            df['position'] == 'mid')].player.values[0]
        if (redMidPlayer != 'unknown player'):
            crawler = gatherPlayerInfo(
                redMidPlayer, redMid, formatedStartDate, formatedEndDate, game, 'mid')
            redMid = int(df_champions.loc[df_champions['id'] == redMid]['key'])
            if (crawler):
                redMidGP = crawler[0]
                redMidWR = crawler[1]
                redMidKDA = crawler[2]
            else:
                return
        else:
            return

        redCarry = df[(df['gameid'] == game) & (df['side'] == 'Red') & (
            df['position'] == 'bot')].champion.values[0]
        redCarryPlayer = df[(df['gameid'] == game) & (
            df['side'] == 'Red') & (df['position'] == 'bot')].player.values[0]
        if (redCarryPlayer != 'unknown player'):
            crawler = gatherPlayerInfo(
                redCarryPlayer, redCarry, formatedStartDate, formatedEndDate, game, 'bot')
            redCarry = int(
                df_champions.loc[df_champions['id'] == redCarry]['key'])
            if (crawler):
                redCarryGP = crawler[0]
                redCarryWR = crawler[1]
                redCarryKDA = crawler[2]
            else:
                return
        else:
            return

        redSupp = df[(df['gameid'] == game) & (df['side'] == 'Red')
                     & (df['position'] == 'sup')].champion.values[0]
        redSuppPlayer = df[(df['gameid'] == game) & (df['side'] == 'Red') & (
            df['position'] == 'sup')].player.values[0]
        if (redSuppPlayer != 'unknown player'):
            crawler = gatherPlayerInfo(
                redSuppPlayer, redSupp, formatedStartDate, formatedEndDate, game, 'sup')
            redSupp = int(
                df_champions.loc[df_champions['id'] == redSupp]['key'])
            if (crawler):
                redSuppGP = crawler[0]
                redSuppWR = crawler[1]
                redSuppKDA = crawler[2]
            else:
                return
        else:
            return

        # RESULT
        result = df[(df['gameid'] == game) & (df['side'] == 'Red')
                    & (df['position'] == 'sup')].result.values[0]

        # WRITING TO DATASET FILE
        with open('outputs/dataset_players_statistics.csv', mode='a', newline="") as dataset2021:
            datasetWriter = csv.writer(dataset2021, delimiter=',')
            datasetWriter.writerow([game, blueTopGP, blueTopWR, blueTopKDA, blueJungleGP, blueJungleWR, blueJungleKDA, blueMidGP, blueMidWR, blueMidKDA, blueCarryGP, blueCarryWR, blueCarryKDA, blueSuppGP, blueSuppWR,
                                    blueSuppKDA, redTopGP, redTopWR, redTopKDA, redJungleGP, redJungleWR, redJungleKDA, redMidGP, redMidWR, redMidKDA, redCarryGP, redCarryWR, redCarryKDA, redSuppGP, redSuppWR, redSuppKDA, result])


df = pd.read_csv("data/mess_dataset_20&21.csv")
df21 = df.copy()
df21 = df21[(df21['date'] >= '2021-01-01')]
df_champions = pd.read_csv('data/dataset_champions.csv')
games = df21.gameid.drop_duplicates()

header = 'game,blueTopGP,blueTopWR,blueTopKDA,blueJungleGP,blueJungleWR,blueJungleKDA,blueMidGP,blueMidWR,blueMidKDA,blueADCGP,blueADCWR,blueADCKDA,blueSupportGP,blueSupportWR,blueSupportKDA,redTopGP,redTopWR,redTopKDA,redJungleGP,redJungleWR,redJungleKDA,redMidGP,redMidWR,redMidKDA,redAdcGP,redAdcWR,redAdcKDA,redSupportGP,redSupportWR,redSupportKDA,result\n'
with open('outputs/dataset_players_statistics.csv', mode='a') as dataset:
    dataset.write(header)

for game in tqdm(games):
    processGames(game)
