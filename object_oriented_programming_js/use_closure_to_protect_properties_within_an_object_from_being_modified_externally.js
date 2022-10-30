function Bird() {
    this.name = 'Larry';
}

let bird = new Bird();
console.log(bird.name);
bird.name = 'Donald';
console.log(bird.name);

function Dog() {
    let name = 'Max';

    this.getName = function() {
        return name;
    }

    // setName isn't working.
    this.setName = function(name) {
        name = name;
    }
}

let dog = new Dog();
console.log(dog.getName());
dog.setName('Floki');
console.log(dog.getName());





