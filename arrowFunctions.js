const myFunc = function(j) {
    j *= 2;
    return j;
}

function myAnotherFunc(k) {
    k += 4;
    return k;
}

console.log(myFunc(6));
console.log(myAnotherFunc(8));

const myFunc1 = function() {
    const myVar = 'value';
    return myVar;
}

console.log('function myFunc1 is: ', myFunc1);
console.log('value of myFunc1 is: ', myFunc1());

const myFunc2 = () => {
    const myVar = 'value';
    return myVar;
}

console.log('value of myFunc2 is: ', myFunc2());

const myFunc3 = () => "value";
console.log('value of myFunc3 is: ', myFunc3());

console.log('the date is: ', Date());
console.log('the new date is: ', new Date());

const date_ = () => new Date();
console.log('the value of the anonymous arrow function new date is:', date_())

export {myAnotherFunc, myFunc};


