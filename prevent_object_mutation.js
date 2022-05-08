let obj = {
    name:"FreeCodeCamp",
    review:"Awesome"
}

console.log(obj.name);
console.log(obj['review']);
console.log(obj.hasOwnProperty('name'));
console.log(obj.hasOwnProperty('review'));
console.log(obj.hasOwnProperty('karvendhan'));

// Object.freeze makes the object immutable.
Object.freeze(obj);
obj.review = "bad"
obj.newProp = "test"

console.log('the new review value of the object is: ', obj['review']);
console.log('the new newProp value of the object is: ', obj['newProp']);
console.log('The object value is: ', obj);




