class HolbertonClass {
  constructor(size, location, founder) {
    this.size = size;
    this.location = location;
    this.founder = founder;
  }

  get size() {
    return this._size;
  }

  set size(newSize) {
    this._size = newSize;
  }

  get location() {
    return this._location;
  }

  set location(newLocation) {
    this._location = newLocation;
  }

  get founder() {
    return this._founder;
  }

  set founder(newFounder) {
    this._founder = newFounder;
  }
}

class StudentHolberton {
  constructor(name, age, gender, _holbertonClass) {
    this.name = name;
    this.age = age;
    this.gender = gender;
    this._holbertonClass = _holbertonClass;
  }

  get name() {
    return this._name;
  }

  set name(newName) {
    this._name = newName;
  }

  get age() {
    return this._age;
  }

  set age(newAge) {
    this._age = newAge;
  }

  get gender() {
    return this._gender;
  }

  set gender(newGender) {
    this._gender = newGender;
  }

  get holbertonClass() {
    return this._holbertonClass;
  }

  set holbertonClass(newHolbertonClass) {
    this._holbertonClass = newHolbertonClass;
  }

  get fullStudentDescription() {
    return `${this._name} is a ${this._age}-year-old ${this._gender} enrolled in the ${this._holbertonClass.size} class at the ${this._holbertonClass.location} location. The ${this._holbertonClass.size} class was founded by ${this._holbertonClass.founder}.`;
  }
}

const holberton = new HolbertonClass(28, "San Francisco", "Sylvain Kalache");
const student1 = new StudentHolberton("John Doe", 22, "male", holberton);
const student2 = new StudentHolberton("Jane Smith", 23, "female", holberton);
const student3 = new StudentHolberton("Bob Johnson", 25, "male", holberton);
const student4 = new StudentHolberton("Linda Davis", 24, "female", holberton);
const student5 = new StudentHolberton("Mike Wilson", 21, "male", holberton);