import pytest
import pandas as pd
from project import read_cricket_data, calculate_team_statistics, calculate_best_batsman, calculate_best_bowler

@pytest.fixture
def sample_cricket_data():
    # Sample cricket data for testing
    data = {
        'Team': ['Team A', 'Team A', 'Team B', 'Team B'],
        'Runs For': [150, 180, 140, 160],
        'Runs Against': [140, 160, 150, 180],
        'Overs Played': [20, 25, 22, 23]
    }
    cricket_data = pd.DataFrame(data)
    return cricket_data

@pytest.fixture
def sample_batsman_data():
    # Sample batsman data for testing
    data = {
        'Player': ['Player A', 'Player B', 'Player C', 'Player D'],
        'Runs': [102, 89, 75, 121]
    }
    batsman_data = pd.DataFrame(data)
    return batsman_data

@pytest.fixture
def sample_bowler_data():
    # Sample bowler data for testing
    data = {
        'Player': ['Player X', 'Player Y', 'Player Z', 'Player W'],
        'Overs': [4.0, 3.5, 4.0, 4.0],
        'Wickets': [3, 2, 4, 1],
        'Runs Conceded': [25, 30, 20, 35]
    }
    bowler_data = pd.DataFrame(data)
    return bowler_data

def test_read_cricket_data(sample_cricket_data):
    # Test reading cricket data from CSV file
    assert sample_cricket_data.equals(read_cricket_data('data-sets/sample_data.csv'))

def test_calculate_team_statistics(sample_cricket_data):
    # Test calculating team statistics
    team_statistics = calculate_team_statistics(sample_cricket_data)
    assert len(team_statistics) == 2
    assert team_statistics[0]['Team'] == 'Team A'
    assert team_statistics[0]['Total Runs'] == 330
    assert team_statistics[0]['Total Runs Against'] == 300
    assert team_statistics[0]['Total Overs Played'] == 45
    assert team_statistics[0]['Net Run Rate'] == pytest.approx(0.66667)

def test_calculate_best_batsman(sample_batsman_data):
    # Test calculating best batsman
    best_batsman = calculate_best_batsman(sample_batsman_data)
    assert best_batsman['Player'] == 'Player D'
    assert best_batsman['Runs'] == 121

def test_calculate_best_bowler(sample_bowler_data):
    # Test calculating best bowler
    best_bowler = calculate_best_bowler(sample_bowler_data)
    assert best_bowler['Player'] == 'Player Z'
    assert best_bowler['Wickets'] == 4
    assert best_bowler['Economy'] == pytest.approx(5.00)
