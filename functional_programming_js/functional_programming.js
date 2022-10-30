const prepareTea = () => "greenTea";

const getTea = (numCups) => {
    const teaCups = [];

    for(let cups = 1; cups <= numCups; cups++) {
        teaCups.push(prepareTea());
    }

    return teaCups;
}

console.log(getTea(40));



