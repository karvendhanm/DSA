// destructuring assignment to extract values from an object

obj = {
    name:'Karvendhan',
    employer:'Amazon',
    maritalStatus:'Married'
}

console.log('the value of employer is: ', obj.employer);
console.log(obj.hasOwnProperty('maritalStatus'));

const {name, employer, maritalStatus} = obj;
console.log('the name is: ', name);
console.log('the employer is: ', employer);
console.log('the maritalStatus is: ', maritalStatus);

// assigning a new variable name while destructuring.
const {name:userName, employer:boss} = obj;
console.log('the username and the employer name is: ', userName, boss);

