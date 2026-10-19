# Valorant Match Analyzer

A beginner-friendly Python data analysis project that analyzes Valorant match performance from a CSV file.

## Features

- Calculates total matches, wins, losses, and win rate
- Calculates total kills, deaths, assists, and K/D ratio
- Shows average headshot percentage
- Analyzes performance by agent
- Analyzes performance by map
- Calculates K/D ratio by map
- Saves performance charts as PNG files

## Tools Used

- Python
- pandas
- matplotlib

## Dataset Format

The CSV file should contain the following columns:

date,agent,map,kills,deaths,assists,result,headshot_percent

### How to run:

First install : py -m pip install -r requirements.txt

then you can run the program !


#### Output :

The program prints performance tables in the terminal and saves charts in the charts/ folder.

Generated charts include:

Kills per match
Agent win rate
Map win rate
Headshot percentage per match
K/D ratio by map

##### Goal of the Project:

The goal of this project is to practice Python, pandas, data analysis, and data visualization using a gaming/esports-related dataset.