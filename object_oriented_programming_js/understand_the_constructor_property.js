function Bird(name, color) {
    this.name = name;
    this.color = color;
}

let greatIndianBuzzard = new Bird('Great Indian Buzzard', 'brown');
console.log(greatIndianBuzzard.name);
console.log(greatIndianBuzzard.color);

function Dog(name, color) {
    this.name = name;
    this.color = color;
}

let greatDane = new Dog('Great Dane', 'fawn');
console.log(greatDane.name);
console.log(greatDane.color);

console.log(greatIndianBuzzard.constructor == Bird);
console.log(greatDane.constructor == Dog);

function joinBirdFraternity(canditate) {
    if(canditate.constructor == Bird) {
        return true;
    } else {
        return false;
    }
}

console.log(joinBirdFraternity(greatIndianBuzzard));
console.log(joinBirdFraternity(greatDane));

