function Bird(name, color) {
    this.name = name;
    this.color = color;
}

Bird.prototype.numLegs = 2;
Bird.prototype.eat = function () {
    console.log('nom nom nom');
}
Bird.prototype.describe = function() {
    console.log('my name is '+ this.name);
}


let sparrow = new Bird('Sparrow', 'mottled')

console.log(sparrow.constructor === Bird);
console.log(sparrow instanceof Bird);

console.log(sparrow.numLegs);
console.log(sparrow.eat());
console.log(sparrow.describe());

function Dog(name, color) {
    this.name = name;
    this.color = color;
}

Dog.prototype = {
    'numLegs' : 2,
    'eat' : function() {
        console.log('nom nom nom');
    },
    'describe' : function() {
        console.log('my name is '+ this.name);
    }
}

let bullDog = new Dog("Bull dog", 'fawn');

console.log(bullDog.describe());