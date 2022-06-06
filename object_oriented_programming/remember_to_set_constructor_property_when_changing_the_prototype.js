function Dog(name) {
    this.name = name;
}

let mastiff = new Dog('Giant');

console.log(mastiff.constructor === Dog);

Dog.prototype = {
    numLegs : 2,
    eat : function() {
        console.log('chow chow chow');
    }
}

let Labrador = new Dog('Max');
// since the prototype was manually declared, constructor property below will not work.
console.log(Labrador.constructor === Dog);
console.log(Labrador.constructor === Object);
console.log(Labrador instanceof Dog);
console.log(Labrador.name);
console.log(Labrador.eat());

// prototype overwriting constructor property can be overcome by declaring the constructor property inside the prototype.
console.log('Creating the Reptile class');
function Reptile(name) {
    this.name = name;
}

Reptile.prototype = {
    constructor: Reptile,
    numLegs: 4,
    sound: function() {
        console.log('grrr... grrr... grrr....');
    }
}

let alligator = new Reptile('fingerSnatcher');
console.log(alligator.constructor === Reptile);

