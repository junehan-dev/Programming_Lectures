class Person {
	constructor(name, v) {
		this.name = name;
		this.age = v;
	}
	speak() {
		console.log(this.name);
	}
	get age() {
		return this._age;
	}
	set age(v) {
		this._age = v;
	}
		
}

a = new Person("class");

console.log(a.age);

a.speak();
