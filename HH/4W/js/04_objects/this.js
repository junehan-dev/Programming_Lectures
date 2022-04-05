'use strict';
let outer = {
	"name" : "out hi!",
	"inner" : {
		"name": "inner hi",
		a() {
			console.log(this.name);
		},
		'b' : () => {
			console.log(this.name, this);
		},
		'c' : function (){
				(() => {
					console.log(this.name);
				})()
		},
	},

}


outer.__proto__.name = "OBJECT hi";
outer.inner.a(); // inner hi
outer.inner.b(); // Object hi
outer.inner.c(); // inner hi


