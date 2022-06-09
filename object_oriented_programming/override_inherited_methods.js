function Animal() {};
Animal.prototype = {
    eat : function() {
        console.log('nom nom nom');
    }
}

function Bird() {}
Bird.prototype = Object.create(Animal.prototype);
Bird.prototype.constructor = Bird;

Bird.prototype.eat = function() {
    console.log('peck peck peck');
}

let bird = new Bird();
console.log(bird.eat());

