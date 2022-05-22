let penguin = "Penguin";
let pumpkin = "Pumpkin";
let pattern = /P(engu|umpk)in/;
console.log(penguin.match(pattern));
console.log(pumpkin.match(pattern));

// Fix the regex so that it checks for the names of Franklin Roosevelt or Eleanor Roosevelt in a case sensitive manner
// and it should make concessions for middle names.

let myString = "Eleanor Roosevelt";
let myregex = /^(Eleanor|Franklin)\s*[a-zA-z.]*?\s*Roosevelt$/;
let result = myregex.test(myString);
console.log('the roosevelts', result);

