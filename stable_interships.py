# O(n^2) time | O(n^2) space
# when n is the length of teams array or the length of interns array
def stableInternships(interns, teams):
    # Write your code here.
    chosenInterns = {}
    freeInterns = [x for x in range(len(interns))]
    currentInternChoices = [0 for x in range(len(interns))]
    teamMaps = []
    for team in teams:
        rank = {}
        for _idx, internNumber in enumerate(team):
            rank[internNumber] = _idx
        teamMaps.append(rank)

    while freeInterns:
        internNum = freeInterns.pop()
        internTeamPreference = interns[internNum][currentInternChoices[internNum]]
        currentInternChoices[internNum] += 1

        if internTeamPreference not in chosenInterns:
            chosenInterns[internTeamPreference] = internNum
            continue

        previousInternNum = chosenInterns[internTeamPreference]
        previousInternRanking = teamMaps[internTeamPreference][previousInternNum]
        currentInternRanking = teamMaps[internTeamPreference][internNum]

        if currentInternRanking < previousInternRanking:
            freeInterns.append(previousInternNum)
            chosenInterns[internTeamPreference] = internNum
        else:
            freeInterns.append(internNum)
    return [[intern, team] for team, intern in chosenInterns.items()]


interns = [
    [0, 1, 2],
    [2, 1, 0],
    [1, 2, 0]
  ]
teams = [
    [2, 1, 0],
    [0, 1, 2],
    [0, 2, 1]
  ]

print(stableInternships(interns, teams))

