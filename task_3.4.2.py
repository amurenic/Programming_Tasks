human_count = int(input("Кол-во участников: "))
team_count = int(input("Кол-во человек в команде: "))
if human_count % team_count == 0:
    teams = []
    teammate_number = 0
    for _ in range(human_count // team_count):
        new_team = []
        for _ in range(team_count):
            teammate_number += 1
            new_team.append(teammate_number)
        teams.append(new_team)
    print(teams)
else:
    print(human_count, "невозможно поделить на команды по", team_count, "человек!")