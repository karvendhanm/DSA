// Another principle of functional programming is to always declare your dependencies explicitly.
// This means if a function depends on a variable or object being present, then pass that variable or
// object directly into the function as an argument.

// So far, we have seen two distinct principles for functional programming:
// Don't alter a variable or object - create new variables and objects and return them if need be from a function.
// Hint: using something like const newArr = arrVar, where arrVar is an array will simply create a reference to the
// existing variable and not a copy. So changing a value in newArr would change the value in arrVar.

// Declare function parameters - any computation inside a function depends only on the arguments passed to the function,
// and not on any global object or variable. Adding one to a number is not very exciting, but we can apply these
// principles when working with arrays or more complex objects.

// The global variable
const bookList = ["The Hound of the Baskervilles", "On The Electrodynamics of Moving Bodies",
    "Philosophiæ Naturalis Principia Mathematica", "Disquisitiones Arithmeticae"];

// Change code below this line
function add(bookList, bookName) {

    const bookListNew = [...bookList];
    bookListNew.push(bookName);
    return bookListNew;

    // Change code above this line
}

// Change code below this line
function remove(bookList, bookName) {
    const bookListNew = [...bookList];
    const book_index = bookListNew.indexOf(bookName);
    if (book_index >= 0) {

        bookListNew.splice(book_index, 1);
        return bookListNew;

        // Change code above this line
    }
}

console.log(add(bookList, 'To kill a mocking bird'));
console.log(remove(bookList, 'To kill a mocking bird'));