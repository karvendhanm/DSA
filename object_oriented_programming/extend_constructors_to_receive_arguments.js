function Bird(name, color) {
    this.name = name;
    this.color = color;
    this.numLegs = 2;
}

let bluebird = new Bird('raven', 'black');
console.log(bluebird.color);