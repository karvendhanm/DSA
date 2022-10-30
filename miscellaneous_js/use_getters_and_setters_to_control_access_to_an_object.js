class Book {
    constructor(author) {
        this._author = author;
    }

    get writer() {
        return this._author;
    }

    set writer(updatedAuthor) {
        this._author = updatedAuthor;
    }
}

const novel = new Book('anonymous');
console.log('the author of the novel is: ', novel.writer);
novel.writer = 'Leo Tolstoy';
console.log('the updated author of the novel is: ', novel.writer);


// Only change code below this line
class Thermostat {
    constructor(temperature){
        this._temperature = (5/9) * (temperature - 32);
    }

    get temperature() {
        return this._temperature;
    }

    set temperature(temperature) {
        this._temperature = temperature;
    }
}

// Only change code above this line

const thermos = new Thermostat(76); // Setting in Fahrenheit scale
let temp = thermos.temperature; // 24.44 in Celsius
thermos.temperature = 26;
temp = thermos.temperature; // 26 in Celsius



