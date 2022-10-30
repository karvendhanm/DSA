let Bird = function(name, color) {
    this.name = name;
    this.color = color;
    this.numLegs = 2;
}

let crow = new Bird('Raven', 'Black');
console.log(typeof crow);
console.log(crow instanceof Bird);