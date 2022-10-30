function Animal(name) {
    this.name = name;
}

Animal.prototype = {
    numLegs : 4,
    eat : function() {
        console.log('chow chow chow')
    }
}

let dog = new Animal('Max');
console.log(dog.name);
console.log(dog.numLegs);
console.log(dog.eat());

let animal = Object.create(Animal.prototype);
console.log(animal.eat());

