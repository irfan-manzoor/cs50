import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate
import logging

def main():
    # Configure logging
    logging.basicConfig(filename='project.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    try:
        # Get the current directory
        current_directory = os.path.dirname(os.path.abspath(__file__))
        # Set the file path for the cricket data CSV file
        csv_file_path = os.path.join(current_directory, 'data-sets', 'cricket_data.csv')
        # Read the cricket data from the CSV file
        cricket_data = read_cricket_data(csv_file_path)

        # Calculate team statistics
        team_statistics = calculate_team_statistics(cricket_data)
        logging.info("Team statistics calculated successfully.")
        print("Team Statistics:")
        # Print the team statistics
        print_table(team_statistics)

        # Visualize runs scored by each team
        visualize_runs_scored(team_statistics)

        # Calculate the best batsman and best bowler
        batsman_data = pd.read_csv(os.path.join(current_directory, 'data-sets', 'batsman_data.csv'))
        bowler_data = pd.read_csv(os.path.join(current_directory, 'data-sets', 'bowler_data.csv'))
        best_batsman = calculate_best_batsman(batsman_data)
        best_bowler = calculate_best_bowler(bowler_data)
        print("\nBest Batsman:")
        # Print the best batsman
        print_table(best_batsman)

        # Visualize batsman statistics
        visualize_batsman_stats(batsman_data)

        print("\nBest Bowler:")
        # Print the best bowler
        print_table(best_bowler)

        # Visualize bowler statistics
        visualize_bowler_stats(bowler_data)

    except Exception as e:
        # Log the error
        logging.error(f"An error occurred: {str(e)}")
        # Print error message
        print("An error occurred. Please check the log file for details.")

def read_cricket_data(csv_file_path):
    # Read cricket data from CSV file
    cricket_data = pd.read_csv(csv_file_path)
    return cricket_data

def calculate_team_statistics(cricket_data):
    # Group cricket data by team
    grouped_data = cricket_data.groupby('Team')

    team_statistics = []
    # Calculate statistics for each team
    for team, data in grouped_data:
        total_runs = data['Runs For'].sum()
        total_runs_against = data['Runs Against'].sum()
        total_overs_played = data['Overs Played'].sum()
        net_run_rate = (total_runs - total_runs_against) / total_overs_played
        team_statistics.append({'Team': team, 'Total Runs': total_runs, 'Total Runs Against': total_runs_against, 'Total Overs Played': total_overs_played, 'Net Run Rate': net_run_rate})

    return team_statistics

def print_table(data):
    # Print data as a table
    if isinstance(data, list):  # Check if data is a list of dictionaries
        sorted_data = sorted(data, key=lambda x: x['Net Run Rate'], reverse=True)
        headers = ["Team", "Total Runs", "Total Runs Against", "Total Overs Played", "Net Run Rate"]
        rows = []
        for team_stat in sorted_data:
            row = [
                team_stat['Team'],
                int(team_stat['Total Runs']),
                int(team_stat['Total Runs Against']),
                int(team_stat['Total Overs Played']),
                '{:.2f}'.format(team_stat['Net Run Rate']),
            ]
            rows.append(row)
        # Print the table
        print(tabulate(rows, headers=headers, tablefmt="grid", numalign="center", stralign="left", floatfmt=".2f"))
    else:  # If data is a single dictionary, print it as a table
        headers = list(data.keys())  # Use keys as headers
        rows = [list(data.values())]  # Convert values to a single row
        # Print the table
        print(tabulate(rows, headers=headers, tablefmt="grid", numalign="center", stralign="left", floatfmt=".2f"))

def visualize_runs_scored(team_statistics):
    # Visualize runs scored by each team
    sorted_team_statistics = sorted(team_statistics, key=lambda x: x['Net Run Rate'], reverse=True)
    teams = [team_stat['Team'] for team_stat in sorted_team_statistics]
    total_runs_for = [team_stat['Total Runs'] for team_stat in sorted_team_statistics]
    total_runs_against = [team_stat['Total Runs Against'] for team_stat in sorted_team_statistics]

    bar_width = 0.35
    x = np.arange(len(teams))

    plt.figure(figsize=(10, 6))
    plt.bar(x - bar_width/2, total_runs_for, width=bar_width, label='Runs For', color='skyblue')
    plt.bar(x + bar_width/2, total_runs_against, width=bar_width, label='Runs Against', color='salmon')

    plt.xlabel('Teams')
    plt.ylabel('Runs')
    plt.title('Runs For and Runs Against by Each Team')
    plt.xticks(x, teams, rotation=45)
    plt.legend()

    plt.tight_layout()
    plt.show()

def calculate_best_batsman(batsman_data):
    # Calculate the best batsman
    best_batsman_row = batsman_data.iloc[batsman_data['Runs'].idxmax()]
    best_batsman_dict = best_batsman_row.to_dict()
    return best_batsman_dict

def calculate_best_bowler(bowler_data):
    # Calculate the best bowler
    bowler_data['Economy'] = bowler_data['Runs Conceded'] / bowler_data['Overs']
    bowler_data = bowler_data.sort_values(by=['Wickets', 'Economy'], ascending=[False, True])
    best_bowler_row = bowler_data.iloc[0]
    best_bowler_dict = best_bowler_row.to_dict()
    return best_bowler_dict

def visualize_batsman_stats(batsman_data):
    # Visualize batsman statistics
    plt.figure(figsize=(10, 6))
    plt.bar(batsman_data['Player'], batsman_data['Runs'], color='skyblue')
    plt.xlabel('Batsman')
    plt.ylabel('Runs Scored')
    plt.title('Runs Scored by Each Batsman')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def visualize_bowler_stats(bowler_data):
    # Visualize bowler statistics
    plt.figure(figsize=(10, 6))
    plt.bar(bowler_data['Player'], bowler_data['Wickets'], color='salmon')
    plt.xlabel('Bowler')
    plt.ylabel('Wickets Taken')
    plt.title('Wickets Taken by Each Bowler')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
