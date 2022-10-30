function Bird(name) {
    this.name = name;
}

function Dog(name) {
    this.name = name;
}

Bird.prototype = {
    constructor: Bird,
    describe: function() {
        console.log("my name is: " + this.name);
    }
}

Dog.prototype = {
    constructor: Dog,
    describe: function() {
        console.log("my name is : " + this.name);
    }
}

let pelican = new Bird('Larry');
let borderCoolie = new Dog('Max');

console.log(pelican.describe());
console.log(borderCoolie.describe());



