"""
MLB Hitting Data 
Author: Patrick Mejia
Date: 6-13-2025
"""

import requests
import polars as pl


def get_hitting_data(year: int) -> pl.DataFrame:
    try:
        url = (
            f"https://statsapi.mlb.com/api/v1/stats"
            f"?stats=season&group=hitting&gameType=R&season={year}"
        )
        response = requests.get(url)
        response.raise_for_status()
        json_data = response.json()

        records = []
        for player_stat in json_data["stats"][0]["splits"]:
            player = player_stat["player"]
            stat = player_stat["stat"]
            record = {
                "Name": f"{player['firstName']} {player['lastName']}",
                "Year": year,
                **stat
            }
            records.append(record)
    except Exception as e:
        print(f"{e}")

    df = pl.DataFrame(records)
    # print(df)

    df.write_csv(f"Stats/mlb_hitting_data_{year}.csv")
    return df

def main():
    total_df = []
    for year in range(2020, 2025):
        print(f"{year} Hitting Stats")
        df = get_hitting_data(year)
        if df.height > 0:
            total_df.append(df)

        if total_df:
            combined_df = pl.concat(total_df, how="vertical")
            combined_df.write_csv("Stats/Hitting/full_mlb_hitting_data.csv")
            print(combined_df)

if __name__ == "__main__":
    main()
