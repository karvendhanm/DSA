const nested_obj = {
    name:'karvendhan',
    family:{
        wife:'nandhini',
        children:'Aathuran, Aathavan'
    }
}

console.log('the nested object is: ', nested_obj);
const {name, family:{wife, children}} = nested_obj;
console.log('the name and family values are', name, wife, children);

const {name:name1, family:{wife:betterHalf, children:rebirth}} = nested_obj;
console.log('the name and family values are', name1, betterHalf, rebirth);