import datetime
import algorithms as algos


def add_game_history(history, winner, players, ai_mode):
    history.append({
        'date': datetime.datetime.now().strftime('%Y-%m-%d %H:%M'),  # Up to minutes
        'winner': "AI" if ai_mode and winner == "AI" else winner,
        'player1': players[0],
        'player2': players[1] if not ai_mode else "AI",
        'draw': winner is None
    })


def display_game_history(history):
    history = algos.quicksort(history, 'date')
    print("\nGame History (sorted by date):")
    for game in history:
        result = "Draw" if game['draw'] else f"{game['winner']} won"
        print(f"{game['date']} - {game['player1']} vs {game['player2']}: {result}")
    return history


# Search for a specific game in the history
# Search for all games involving a specific player
def search_game_history(history):
    print("\nSearch for a game in the history.")
    player_name = input("Enter the player's name (case-insensitive): ").strip().capitalize()
    sorted_history = algos.quicksort(history, 'date')
    found_games = []

    # Check if the player is part of the game (case-insensitive)
    for game in sorted_history:
        if player_name.lower() in [game['player1'].lower(), game['player2'].lower()]:
            found_games.append(game)

    if found_games:
        print(f"\nGames involving '{player_name}':")
        for game in found_games:
            result = "Draw" if game['draw'] else f"{game['winner']} won"
            print(f"{game['date']} - {game['player1']} vs {game['player2']}: {result}")
    else:
        print("No games found involving that player.")