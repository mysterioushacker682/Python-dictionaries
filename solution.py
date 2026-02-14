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

def find_active_gamers(games_by_student, min_games):
    #Return a list of students who have played at least min_games different games.
    print(games_by_student)
    active_gamers = []
    for student,games in games_by_student:
        print(student)
        print(games)
        if len(games) >= min_games:
            active_gamers.append(student)
    print(active_gamers)
    return active_gamers

            

#Write a function:
#Return a dictionary where:
#	•	key → student name
#	•	value → total minutes played
def total_play_time(game_log):
    minutes_played = 0 
    playtime = {}
    for logs in game_log:
        current_name = logs["studentName"]
        if  current_name not in playtime:
            playtime[current_name] = 0
        playtime[current_name] += logs["minutesPlayed"]
    print(playtime)
    return playtime


def main():
    #games = list_games(game_log)
    #find_active_gamers(games,2)
    total_play_time(game_log)
main()
