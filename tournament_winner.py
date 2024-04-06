from collections import Counter
from operator import itemgetter

def tournamentWinner(competitions, results):
    # Write your code here.
    results = [1 if result == 0 else 0 for result in results]
    winners = []

    for idx, competition in enumerate(competitions):
        winners.append(competition[results[idx]])

    tmp = sorted(dict(Counter(winners)).items(), key=itemgetter(1), reverse=True)

    return tmp[0][0]


competitions = [
    ['HTML', 'C#'],
    ['C#', 'Python'],
    ['Python', 'HTML']
]
results = [0, 0, 1]
tournamentWinner(competitions, results)
