// Even a function can have an instance like a class in python.
var SpaceShuttle = function(targetPlanet){
    this.targetPlanet = targetPlanet;
}

var zeus = new SpaceShuttle('Jupiter');
var venus = new SpaceShuttle('Venus')

console.log(typeof SpaceShuttle);
console.log(typeof zeus);
console.log(SpaceShuttle.targetPlanet); // undefined
console.log(zeus.targetPlanet); // Jupiter
console.log(venus.targetPlanet); // Venus

class SpaceShuttle1 {
    constructor(targetPlanet) {
        this.targetPlanet = targetPlanet;
    }
}

const zeus1 = new SpaceShuttle1('Jupiter');
console.log('the value of zeus1 targetPlanet is: ', zeus1.targetPlanet);
