# from collections import Counter
# from operator import itemgetter

# def tournamentWinner(competitions, results):
#     # Write your code here.
#     results = [1 if result == 0 else 0 for result in results]
#     winners = []

#     for idx, competition in enumerate(competitions):
#         winners.append(competition[results[idx]])

#     tmp = sorted(dict(Counter(winners)).items(), key=itemgetter(1), reverse=True)

#     return tmp[0][0]


def find_tournament_winner(_dict):
    winning_team = ""
    winning_score = 0
    for team, score in _dict.items():
        if score > winning_score:
            winning_team = team
            winning_score = score
    return winning_team


def tournamentWinner(competitions, results):
    # Write your code here.
    tournament_pts_standing = {}
    results = [1 if result == 0 else 0 for result in results]

    for idx in range(len(competitions)):
        winning_team = competitions[idx][results[idx]]
        if winning_team in tournament_pts_standing:
            tournament_pts_standing[winning_team] += 3
        else:
            tournament_pts_standing[winning_team] = 3

    return find_tournament_winner(tournament_pts_standing)


competitions = [
    ['HTML', 'C#'],
    ['C#', 'Python'],
    ['Python', 'HTML']
]
results = [0, 0, 1]
tournamentWinner(competitions, results)
