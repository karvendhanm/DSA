function Bird(name) {
    this.name = name;
}

let duck = new Bird('Larry');

console.log(Bird.prototype.isPrototypeOf(duck));