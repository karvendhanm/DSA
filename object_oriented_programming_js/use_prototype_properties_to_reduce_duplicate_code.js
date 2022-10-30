Bird.prototype.numLegs = 2;

function Bird(name, color) {
    this.name = name;
    this.color = color;
}

let buzzard = new Bird('hook', 'dirty brown');

console.log(buzzard.numLegs);