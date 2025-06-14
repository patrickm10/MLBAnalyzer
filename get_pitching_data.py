"""
MLB Pitching Data
Author: Patrick Mejia
Date: 6-13-2025
"""

import requests
import polars as pl

def get_pitching_data(year: int) -> pl.DataFrame:
    """
    Gets the pitching data by year.

    Args:
        year (int): The year of the rankings.

    Returns:
        pl.DataFrame: A Polars DataFrame of pitching stats.
    """
    try:
        url = (
            f"https://statsapi.mlb.com/api/v1/stats"
            f"?stats=season&group=pitching&gameType=R&season={year}"
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

        df = pl.DataFrame(records)
    
    except Exception as e:
        print(f"Error fetching pitching data for {year}: {e}")
        return pl.DataFrame()

    print(df)
    df.write_csv(f"Stats/Pitching/mlb_pitching_data_{year}.csv")
    return df

def main():
    total_df = []

    for year in range(2020, 2025):
        print(f"{year} Pitching Stats")
        df = get_pitching_data(year)
        if df.height > 0:
            total_df.append(df)

    if total_df:
        combined_df = pl.concat(total_df, how="vertical")
        combined_df.write_csv("Stats/Pitching/full_mlb_pitching_data.csv")
        print("Combined CSV saved as: Stats/full_mlb_pitching_data.csv")
    else:
        print("No pitching data found.")

if __name__ == "__main__":
    main()
