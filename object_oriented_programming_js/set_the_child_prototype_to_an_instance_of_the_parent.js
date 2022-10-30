function Animal(name) {
    this.name = name;
}

Animal.prototype = {
    numLegs : 4,
    eat : function() {
        console.log('chow chow chow');
    }
}

function Bird(name) {
    this.name = name;
}
Bird.prototype = Object.create(Animal.prototype);

let bird = new Bird('Larry');
console.log(bird.name);
console.log(bird.eat());