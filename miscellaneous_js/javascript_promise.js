const myPromise = new Promise((resolve, reject) => {
    let responseFromServer=false;

    if(responseFromServer) {
        resolve('We got the data');
    } else {
        reject('Data not received');
    }
});

// result is triggered only by Promise constructor function ends in a resolve.
// The Promise constructor function ending in reject will not invoke the then
myPromise.then(result => {
    console.log(result);
})

// catch is the method used when your promise has been rejected. It is executed immediately after a
// promise's reject method is called. Here’s the syntax:
myPromise.catch(error=> {
    console.log(error);
})