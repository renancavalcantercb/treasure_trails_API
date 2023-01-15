import glob
from datetime import date
import pandas as pd
import requests
from exceptions.UserNotFound import UserNotFound


def get_treasures_trails_data(nickname: str) -> pd.DataFrame:
    today = date.today()
    runescape_api_url = f"https://secure.runescape.com/m=hiscore/index_lite.ws?player={nickname.lower()}"
    try:
        response = requests.get(runescape_api_url.format("Treasure Trails"))
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            raise UserNotFound(nickname)
        else:
            raise e

    treasure_trails_data = response.text.splitlines()[-5:]
    treasure_trails_df = pd.DataFrame(
        [line.split(",") for line in treasure_trails_data],
        columns=["rank", "quantity"],
    )
    treasure_trails_df["date"] = pd.to_datetime(today)
    treasure_trails_df["tier"] = ["Easy", "Medium", "Hard", "Elite", "Master"]
    treasure_trails_df = treasure_trails_df.rename(columns={'rank': 'rank_number', 'quantity': 'quantity_completed'})
    treasure_trails_df = treasure_trails_df.sort_values(by=['date'])
    treasure_trails_df = treasure_trails_df.set_index(["date"])
    treasure_trails_df.to_csv(f"{nickname}_{date.today()}.csv")
    return treasure_trails_df


def get_historical_treasure_trails(nickname: str) -> pd.DataFrame:
    try:
        csv_files = glob.glob("*.csv")
        nickname_csv_files = [
            csv_file for csv_file in csv_files if nickname in csv_file
        ]
        if not nickname_csv_files:
            raise UserNotFound(nickname)
        historical_treasure_trails_df = pd.concat(
            [pd.read_csv(csv_file, index_col=0, parse_dates=['date']) for csv_file in nickname_csv_files],
            ignore_index=True
        )
        historical_treasure_trails_df = historical_treasure_trails_df.sort_values(by=['date'])
        historical_treasure_trails_df.to_csv(f"{nickname}_historical.csv")
        return historical_treasure_trails_df
    except Exception as e:
        print(e)
