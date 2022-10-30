// ES5
const person = {
    name: 'Taylor',
    sayHello: function () {
        return `Hello! my name is ${this.name}`;
    }
};

console.log(person.name);
console.log(person.sayHello());

// With  Es6
const person_ = {
    name: 'Taylor',
    sayHello() {
        return `My Name is: ${this.name}`;
    }
};

console.log(person_.name);
console.log(person_.sayHello());