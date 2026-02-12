game_log = [
    {"studentName": "Ali", "gameName": "Minecraft", "minutesPlayed": 40, "levelReached": 5},
    {"studentName": "Sara", "gameName": "Roblox", "minutesPlayed": 30, "levelReached": 3},
    {"studentName": "Ali", "gameName": "Minecraft", "minutesPlayed": 20, "levelReached": 6},
    {"studentName": "Ali", "gameName": "FIFA", "minutesPlayed": 25, "levelReached": 2},
    {"studentName": "Sara", "gameName": "Minecraft", "minutesPlayed": 15, "levelReached": 2},
]
def list_games(game_log):
    unique_games = {}
    for game in game_log:
        name = game["studentName"]
        game_name = game["gameName"]
        if name not in unique_games:
            unique_games[name] = []
        if game_name not in unique_games[name]:
            unique_games[name].append(game_name)
    print(unique_games)
    return unique_games

list_games(game_log)