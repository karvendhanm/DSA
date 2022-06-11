const prepareGreenTea = () => "greenTea";
const prepareBlackTea = () => "blackTea";

const getTea = (prepareTea, numCups) => {
    const teaCups = [];

    for(let cups = 1; cups <= numCups; cups++) {
        const teaCup = prepareTea();
        teaCups.push(teaCup);
    }

    return teaCups;
}

const tea4GreenTeamFCC = getTea(prepareGreenTea, 27)
const tea4BlackTeamFcc = getTea(prepareBlackTea, 13)

console.log(tea4GreenTeamFCC,
    tea4BlackTeamFcc);