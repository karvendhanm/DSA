let foods = {
    apples: 25,
    oranges: 32,
    plums: 28,
    bananas: 13,
    grapes: 35,
    strawberries: 27
};

let key_ = 'grapes';
console.log(key_);
// below line will not work and will return undefined
console.log(foods.key_);
console.log(foods[key_]);