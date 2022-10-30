let user = {
    'name' : 'Karvendhan',
    'age' : 36,
    'employer' : 'Amazon'
}

// deleting an object property.
console.log(user);
delete user.age;
console.log(user);

console.log('name' in user);
console.log(user.hasOwnProperty('employer'));



