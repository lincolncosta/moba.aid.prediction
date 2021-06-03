import pandas as pd
import csv

df_champions = pd.read_csv('data/dataset_champions.csv')
df_crawler = pd.read_csv('outputs/dataset_20210515.csv')

games = df_crawler['game'].drop_duplicates()


def generate_dataset_banned_champions():
    return


def generate_dataset_full():
    return


def generate_dataset_picked_champions_players_statistics():
    return


def generate_dataset_picked_champions():
    return


def generate_dataset_dataset_players_statistics():
    for game in games:
        
        # BLUE TEAM
        bluetopwr = str(float(df_crawler[(df_crawler['game'] == game)].bluetopwr.values[0].strip('%'))/100)
        bluetopgp = df_crawler[(df_crawler['game'] == game)].bluetopgp.values[0]
        bluetopkda = df_crawler[(df_crawler['game'] == game)].bluetopkda.values[0]

        bluejunglewr = str(float(df_crawler[(df_crawler['game'] == game)].bluejunglewr.values[0].strip('%'))/100)
        bluejunglegp = df_crawler[(df_crawler['game'] == game)].bluejunglegp.values[0]
        bluejunglekda = df_crawler[(df_crawler['game'] == game)].bluejunglekda.values[0]

        bluemidwr = str(float(df_crawler[(df_crawler['game'] == game)].bluemidwr.values[0].strip('%'))/100)
        bluemidgp = df_crawler[(df_crawler['game'] == game)].bluemidgp.values[0]
        bluemidkda = df_crawler[(df_crawler['game'] == game)].bluemidkda.values[0]

        blueadcwr = str(float(df_crawler[(df_crawler['game'] == game)].blueadcwr.values[0].strip('%'))/100)
        blueadcgp = df_crawler[(df_crawler['game'] == game)].blueadcgp.values[0]
        blueadckda = df_crawler[(df_crawler['game'] == game)].blueadckda.values[0]

        bluesupportwr = str(float(df_crawler[(df_crawler['game'] == game)].bluesupportwr.values[0].strip('%'))/100)
        bluesupportgp = df_crawler[(df_crawler['game'] == game)].bluesupportgp.values[0]
        bluesupportkda = df_crawler[(df_crawler['game'] == game)].bluesupportkda.values[0]

        # RED TEAM
        redtopwr = str(float(df_crawler[(df_crawler['game'] == game)].redtopwr.values[0].strip('%'))/100)
        redtopgp = df_crawler[(df_crawler['game'] == game)].redtopgp.values[0]
        redtopkda = df_crawler[(df_crawler['game'] == game)].redtopkda.values[0]

        redjunglewr = str(float(df_crawler[(df_crawler['game'] == game)].redjunglewr.values[0].strip('%'))/100)
        redjunglegp = df_crawler[(df_crawler['game'] == game)].redjunglegp.values[0]
        redjunglekda = df_crawler[(df_crawler['game'] == game)].redjunglekda.values[0]

        redmidwr = str(float(df_crawler[(df_crawler['game'] == game)].redmidwr.values[0].strip('%'))/100)
        redmidgp = df_crawler[(df_crawler['game'] == game)].redmidgp.values[0]
        redmidkda = df_crawler[(df_crawler['game'] == game)].redmidkda.values[0]

        redadcwr = str(float(df_crawler[(df_crawler['game'] == game)].redadcwr.values[0].strip('%'))/100)
        redadcgp = df_crawler[(df_crawler['game'] == game)].redadcgp.values[0]
        redadckda = df_crawler[(df_crawler['game'] == game)].redadckda.values[0]

        redsupportwr = str(float(df_crawler[(df_crawler['game'] == game)].redsupportwr.values[0].strip('%'))/100)
        redsupportgp = df_crawler[(df_crawler['game'] == game)].redsupportgp.values[0]
        redsupportkda = df_crawler[(df_crawler['game'] == game)].redsupportkda.values[0]

        result = df_crawler[(df_crawler['game'] == game)].result.values[0]

        with open('data/dataset_players_statistics.csv', mode='a', newline="") as dataset_players_statistics:
            datasetWriter = csv.writer(dataset_players_statistics, delimiter=',')
            datasetWriter.writerow([game,bluetopgp,bluetopwr,bluetopkda,bluejunglegp,bluejunglewr,bluejunglekda,bluemidgp,bluemidwr,bluemidkda,blueadcgp,blueadcwr,blueadckda,bluesupportgp,bluesupportwr,bluesupportkda,redtopgp,redtopwr,redtopkda,redjunglegp,redjunglewr,redjunglekda,redmidgp,redmidwr,redmidkda,redadcgp,redadcwr,redadckda,redsupportgp,redsupportwr,redsupportkda,result])     

# generate_dataset_dataset_players_statistics()
