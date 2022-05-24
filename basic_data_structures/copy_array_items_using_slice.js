// Rather than modifying an array, slice() copies or extracts a given number of elements to a new array
// slice() takes only 2 parameters — the first is the index at which to begin extraction,
// and the second is the index at which to stop extraction (extraction will occur up to,
// but not including the element at this index)

let weatherConditions = ['rain', 'snow', 'sleet', 'hail', 'clear'];
let todaysWeather = weatherConditions.slice(1, 3);

console.log('weatherConditions', weatherConditions);
console.log('todaysWeather', todaysWeather);

