let nestedArray = [
    ['deep'],
    [
        ['deeper'], ['deeper']
    ],
    [
        [
            ['deepest'], ['deepest']
        ],
        [
            [
                ['deepest-est?']
            ]
        ]
    ]
];

console.log(nestedArray[2][1][0][0][0]);
nestedArray[2][1][0][0][0] = 'deeper still';
console.log(nestedArray[2][1][0][0][0]);

let myNestedArray = [
    // Only change code below this line
    ['unshift', false, 1, 2, 3, 'complex', 'nested'],
    ['loop', 'shift', 6, 7, 1000, 'method'],
    ['concat', false, true, 'spread', 'array'],
    ['mutate', 1327.98, 'splice', 'slice', 'push'],
    ['iterate', 1.3849, 7, '8.4876', 'arbitrary', 'depth']
    // Only change code above this line
];
let crazyarr = [
    [
        ['deep'], [
            [
                'deeper'
            ]
    ], [
        [
            ['deepest']
        ]
    ]
    ]
]
myNestedArray.unshift(crazyarr);
console.log('my nested array', myNestedArray);