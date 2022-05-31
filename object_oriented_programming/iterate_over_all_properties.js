function Bird(name, color) {
    this.name = name;
    this.color = color;
}

Bird.prototype.numLegs = 2;

buzzard = new Bird('sharp tooth', 'grey');

let ownProps = [];
let prototypeProps = [];


for(let property in buzzard) {
    if(buzzard.hasOwnProperty(property)) {
        ownProps.push(property);
    } else {
        prototypeProps.push(property);
    }
}

console.log(ownProps);
console.log(prototypeProps);