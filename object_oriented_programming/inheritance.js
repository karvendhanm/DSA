function Animal() {}

function Bird(name) {
    this.name = name;
}

let bird = new Bird('Larry');
console.log(bird.name);
console.log(bird.constructor);
console.log(bird.constructor === Bird)

// the instance of a custom object vanishes when we introduce a prototype.
Animal.prototype = {
    numLegs : 4,
    eat : function() {
        console.log('chow chow chow');
    }
}

function Dog(name) {
    this.name = name;
}

Dog.prototype = Object.create(Animal.prototype)
let dog = new Dog('Max');
console.log(dog.name);
console.log(dog.constructor);
console.log(dog.constructor === Dog);
console.log(dog.constructor === Object);

// we can reset the constructor type.
Dog.prototype.constructor = Dog;
console.log(dog.constructor);
console.log(dog.constructor === Dog);
console.log(dog.constructor === Object);





