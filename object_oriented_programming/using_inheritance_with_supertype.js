// describe function is used in the prototypes of both Bird and Dog.
// By creating supertype we can avoid this and confirm to DRY principles.



function Bird(name) {
    this.name = name;
}

function Dog(name) {
    this.name = name;
}

Bird.prototype = {
    constructor: Bird
}

Dog.prototype = {
    constructor: Dog
}

function Animal() {}

Animal.prototype = {
    constructor: Animal,
    describe: function() {
        console.log("my name is : " + this.name);
    }
}

let penguin = new Bird('Larry');
console.log(penguin.describe());

