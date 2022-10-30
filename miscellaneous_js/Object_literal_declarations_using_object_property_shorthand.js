obj = {
    name:'John Doe',
    age:'36'
}

console.log(obj.name, obj.age);

const arrowUsage = () => 'value';
console.log(arrowUsage());


const getMousePosition = (x, y) => ({x_coord:x, y_coord:y});
console.log(getMousePosition(10, 5));

const getMousePositionLessSyntax = (x, y) => ({x, y});
console.log(getMousePositionLessSyntax(10, 5));

