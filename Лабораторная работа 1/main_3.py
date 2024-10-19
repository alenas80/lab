list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]
col_players = len(list_players)

team_2 = list_players[col_players // 2:]
team_1 = list_players[:col_players // 2]

print(team_1)
print(team_2)