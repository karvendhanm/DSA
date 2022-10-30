const restParameter = (...args) => "The function has " + args.length + " paramters";

console.log(restParameter(1, 2, 3, 4));
console.log(restParameter(1, null, [3, 4, 5], {}, {name:"Karvendhan", employer:"Amazon"}));

function restParamter1(...args) {
    let sum = 0;
    for(let i=0; i < args.length; i++) {
        sum += args[i];
    }
    return sum;
}

function restParamterReduce(...args) {
    return args.reduce((a,b) => a+b, 0);
}

function restParamterMap(...args) {
    return args.reduce(a => a*3, 0);
}

console.log('The sum of the given numbers', restParamter1(1, 2, 3, 4));
console.log('The sum of the given numbers restParamterReduce', restParamterReduce(1, 2, 3, 4));
console.log('The sum of the given numbers restParamterMap', restParamterMap(1, 2, 3, 4));

