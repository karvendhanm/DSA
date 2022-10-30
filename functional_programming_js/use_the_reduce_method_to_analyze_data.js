const users = [
    {name:'user1', age:36},
    {name:'user2', age:29},
    {name:'user3', age:5},
    {name:'user4', age:2}

]

const sumOfAges = users.reduce((sum, user) => sum + user.age, 0);
console.log(sumOfAges);

const userObj = users.reduce((obj, user) => {
    obj[user.name] = user.age;
    return obj;
}, {});

console.log(userObj);

const _userObj = users.map(user => ({name:user.name, age:user.age}));
console.log(_userObj);

