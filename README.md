📚 Story

Your school has a Gaming Club. Every time a student plays a game during club hours, it is recorded.

Each play session is stored as a dictionary with:
	•	"studentName" → name of the student
	•	"gameName" → name of the game
	•	"minutesPlayed" → how many minutes they played
	•	"levelReached" → level they reached in that session

All sessions are stored inside a list called game_log.

Example:

game_log = [
    {"studentName": "Ali", "gameName": "Minecraft", "minutesPlayed": 40, "levelReached": 5},
    {"studentName": "Sara", "gameName": "Roblox", "minutesPlayed": 30, "levelReached": 3},
    {"studentName": "Ali", "gameName": "Minecraft", "minutesPlayed": 20, "levelReached": 6},
    {"studentName": "Ali", "gameName": "FIFA", "minutesPlayed": 25, "levelReached": 2},
    {"studentName": "Sara", "gameName": "Minecraft", "minutesPlayed": 15, "levelReached": 2},
]


⸻

🧠 TASK 1 – Unique Games Per Student

Write a function:

def list_games(game_log):

Return a dictionary where:
	•	key → student name
	•	value → list of unique games they played

If a student played the same game multiple times, it should appear only once in their list.

⸻

🧠 TASK 2 – Active Gamers

Write a function:

def find_active_gamers(games_by_student, min_games):

Return a list of students who have played at least min_games different games.

⸻

🧠 TASK 3 – Total Play Time

Write a function:

def total_play_time(game_log):

Return a dictionary where:
	•	key → student name
	•	value → total minutes played

All sessions count (even repeated games).

⸻

🧠 TASK 4 – Highest Level Reached

Write a function:

def highest_level(game_log):

Return a dictionary where:
	•	key → student name
	•	value → highest level they reached in any game

⸻

🎯 Bonus Challenge (Harder)

Write a function:

def top_gamer(game_log):

Return the name of the student who played the most total minutes.

If two students have the same total minutes, return any one of them.
