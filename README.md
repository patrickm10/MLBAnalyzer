# MLB Analyzer

Author: Patrick Mejia  
Date: June 13, 2025  

A Python-based data collection tool that scrapes official **MLB hitting and pitching statistics** from the MLB Stats API, formats them using Polars, and exports the results into CSV files organized by year or combined across seasons.

## Features

- Collects **season-level MLB stats** for both hitters and pitchers
- Supports multiple years in one run
- Adds a `Year` column to each record
- Outputs to a single combined CSV file per stat type
- Cleanly handles API errors and empty responses

## Requirements

- Python 3.9+
- [Polars](https://pola-rs.github.io/polars/)
- `requests` library

Install dependencies:

```bash
pip install polars requests

<pre> mlb_stats_project/ │ ├── hitting/ │ ├── hitting_stats.py # Script to fetch hitting stats │ ├── 2020.csv │ ├── 2021.csv │ ├── 2022.csv │ ├── 2023.csv │ ├── 2024.csv │ └── mlb_hitting_data_all_years.csv │ ├── pitching/ │ ├── pitching_stats.py # Script to fetch pitching stats │ ├── 2020.csv │ ├── 2021.csv │ ├── 2022.csv │ ├── 2023.csv │ ├── 2024.csv │ └── mlb_pitching_data_all_years.csv │ ├── README.md # Project documentation ├── requirements.txt # (Optional) Python dependencies </pre>
