let firstString = "Ricky is first and can be found";
let firstRegex = /^Ricky/;
console.log('caret smbol', firstString.match(firstRegex));
let notFirst = "You can't find Ricky now.";
console.log('Cannot find ricky now', firstRegex.test(notFirst));

let theEnding = "This is a never ending story";
let storyRegex = /story$/;
storyRegex.test(theEnding);
let noEnding = "Sometimes a story will have to end";
storyRegex.test(noEnding);