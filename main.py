"""
Valorant Match Analyzer

This project analyzes Valorant match data from a CSV file.
It calculates performance statistics such as win rate, K/D ratio,
agent performance, map performance, and headshot percentage.

Tools used:
- Python
- pandas
- matplotlib
"""


import pandas as pd
import matplotlib.pyplot as plt
import os


def load_data(file_path):
    """load the Valorant match data from a CSV file."""
    return pd.read_csv(file_path)


def validate_data(df):
    """Checks if CSV file has the required columns."""
    required_columns = [
        "date",
        "agent",
        "map",
        "kills",
        "deaths",
        "assists",
        "result",
        "headshot_percent"
    ]

    missing_columns = []

    for column in required_columns:
        if column not in df.columns:
            missing_columns.append(column)

    if missing_columns:
        print("Error: The CSV file is missing these columns:")
        for column in missing_columns:
            print(f"- {column}")
        return False

    return True


def basic_summary(df):
    """print basic performance stats such as win rate , total kills, total death and ..."""
    total_matches = len(df)
    wins = len(df[df["result"] == "Win"])
    losses = len(df[df["result"] == "Loss"])
    win_rate = wins / total_matches * 100

    total_kills = df["kills"].sum()
    total_deaths = df["deaths"].sum()
    total_assists = df["assists"].sum()

    average_kills = df["kills"].mean()
    average_deaths = df["deaths"].mean()
    average_assists = df["assists"].mean()
    average_headshot = df["headshot_percent"].mean()

    kd_ratio = total_kills / total_deaths

    print("===== Your Valorant Match Summary =====")
    print(f"Total matches: {total_matches}")
    print(f"Wins: {wins}")
    print(f"Losses: {losses}")
    print(f"Win rate: {win_rate:.2f}%")
    print()
    print(f"Total kills: {total_kills}")
    print(f"Total deaths: {total_deaths}")
    print(f"Total assists: {total_assists}")
    print()
    print(f"Average kills: {average_kills:.2f}")
    print(f"Average deaths: {average_deaths:.2f}")
    print(f"Average assists: {average_assists:.2f}")
    print(f"Average headshot %: {average_headshot:.2f}%")
    print(f"K/D ratio: {kd_ratio:.2f}")


def agent_performance(df):
    """Analyzing performance by Agent."""
    agent_stats = df.groupby("agent").agg(
        matches=("agent", "count"),
        average_kills=("kills", "mean"),
        average_deaths=("deaths", "mean"),
        average_assists=("assists", "mean"),
        average_headshot_percent=("headshot_percent", "mean"),
        wins=("result", lambda x: (x == "Win").sum())
    )

    agent_stats["win_rate"] = agent_stats["wins"] / agent_stats["matches"] * 100
    agent_stats["kd_ratio"] = agent_stats["average_kills"] / agent_stats["average_deaths"]

    print("\n===== Agent Performance =====")
    print(agent_stats.round(2))

    return agent_stats


def map_performance(df):
    """Analyzing performance by map."""
    map_stats = df.groupby("map").agg(
        matches=("map", "count"),
        wins=("result", lambda x: (x == "Win").sum()),
        average_kills=("kills", "mean"),
        average_deaths=("deaths", "mean"),
        average_assists=("assists", "mean"),
        average_headshot_percent=("headshot_percent", "mean")
    )

    map_stats["win_rate"] = map_stats["wins"] / map_stats["matches"] * 100
    map_stats["kd_ratio"] = map_stats["average_kills"] / map_stats["average_deaths"]

    print("\n===== Map Performance =====")
    print(map_stats.round(2))

    return map_stats


def create_charts(df, agent_stats, map_stats):
    """Create and save charts here"""
    os.makedirs("charts", exist_ok=True)

    # Chart 1: Kills per match
    plt.figure()
    plt.plot(df["date"], df["kills"], marker="o")
    plt.title("Kills Per Match")
    plt.xlabel("Date")
    plt.ylabel("Kills")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("charts/kills_per_match.png")
    plt.close()

    # Chart 2: Agent win rate
    plt.figure()
    agent_stats["win_rate"].plot(kind="bar")
    plt.title("Win Rate by Agent")
    plt.xlabel("Agent")
    plt.ylabel("Win Rate (%)")
    plt.tight_layout()
    plt.savefig("charts/agent_win_rate.png")
    plt.close()

    # Chart 3: Map win rate
    plt.figure()
    map_stats["win_rate"].plot(kind="bar")
    plt.title("Win Rate by Map")
    plt.xlabel("Map")
    plt.ylabel("Win Rate (%)")
    plt.tight_layout()
    plt.savefig("charts/map_win_rate.png")
    plt.close()

    # Chart 4:Shows Headshot percentage per match
    plt.figure()
    plt.plot(df["date"], df["headshot_percent"], marker="o")
    plt.title("Headshot Percentage Per Match")
    plt.xlabel("Date")
    plt.ylabel("Headshot %")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("charts/headshot_percent_per_match.png")
    plt.close()

    # Chart 5: K/D ratio by map
    plt.figure()
    map_stats["kd_ratio"].plot(kind="bar")
    plt.title("K/D Ratio by Map")
    plt.xlabel("Map")
    plt.ylabel("K/D Ratio")
    plt.tight_layout()
    plt.savefig("charts/map_kd_ratio.png")
    plt.close()


    print("\nCharts saved in the 'charts' folder.")



def main():
    file_path = "data/matches.csv"

    df = load_data(file_path)

    if not validate_data(df):
        return

    basic_summary(df)
    agent_stats = agent_performance(df)
    map_stats = map_performance(df)

    create_charts(df, agent_stats, map_stats)


def validate_data(df):
    """Check if the CSV file has the required columns."""
    required_columns = [
        "date",
        "agent",
        "map",
        "kills",
        "deaths",
        "assists",
        "result",
        "headshot_percent"
    ]

    missing_columns = []

    for column in required_columns:
        if column not in df.columns:
            missing_columns.append(column)

    if missing_columns:
        print("Error: The CSV file is missing these columns:")
        for column in missing_columns:
            print(f"- {column}")
        return False

    return True



if __name__ == "__main__":
    main()