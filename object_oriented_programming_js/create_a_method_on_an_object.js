let duck = {
    name: "aflac",
    numLegs: 2,
    sayName : function() {return `my name is ${this.name}.`}
}

console.log(duck.sayName());