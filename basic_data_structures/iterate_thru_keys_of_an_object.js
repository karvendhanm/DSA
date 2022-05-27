// iterate through an object using an for ... in statement.

const users = {
    Alan: {
        online: false
    },
    Jeff: {
        online: true
    },
    Sarah: {
        online: false
    }
}

function getArrayOfUsers(usersObj) {
    return Object.keys(usersObj);
}

function countOnline(usersObj) {
    // Only change code below this line

    let i = 0;
    for(let user in usersObj) {
        if(usersObj[user]['online'] === true) {
            i += 1;
        }
    }
    return i;
    // Only change code above this line
}

console.log(getArrayOfUsers(users));
console.log(countOnline(users));