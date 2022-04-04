"use strict";

let		_private_to_module = "PRIVATE KEY";

console.log(_private_to_module);

module.exports.keys = [
	_private_to_module,
];

// let


let threeUser = [
	{
		"name":	"test1"
	},{
		"name":	"test1"
	},{
		"name":	"test1",
		"age":	23,
		"g": "M",
	}
];

let [huey, dewey, louie] = threeUser;
console.log(huey.name, dewey, louie);

let {name, age, g} = louie;
console.log(name, age, g);
