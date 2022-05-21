let username = "AB1";
let userCheck = /^[a-zA-Z][a-zA-Z][a-zA-Z]*\d*$|^[a-zA-Z][a-zA-Z]$|^[a-zA-Z]\d\d+$/;
let result = userCheck.test(username);
console.log('login restrictions', result);