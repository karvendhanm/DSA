function Bird(name) {
    this.name = name;
}

console.log('typeof Bird', typeof Bird);
console.log('typeof Bird prototype', typeof Bird.prototype);

console.log(Object.prototype.isPrototypeOf(Bird.prototype));