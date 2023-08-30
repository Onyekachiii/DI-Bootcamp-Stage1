//1. Analyze the code below. What will be the output?
const person = {
    name: 'John Doe',
    age: 25,
    location: {
        country: 'Canada',
        city: 'Vancouver',
        coordinates: [49.2827, -123.1207]
    }
}

const {name, location: {country, city, coordinates: [lat, lng]}} = person;

console.log(`I am ${name} from ${city}, ${country}. Latitude(${lat}), Longitude(${lng})`);


//2. Using the code below, destructure the parameter inside the function and return a string as the example seen below:
//output : 'Your full name is Elie Schoppik'

function displayStudentInfo(objUser){
    const {first, last} = objUser;
     //destructuring
    console.log(`Your full name is ${first} ${last}`);
   
}

displayStudentInfo({first: 'Elie', last:'Schoppik'});


//3. Using this object const users = { user1: 18273, user2: 92833, user3: 90315 }
//a. Using methods taught in class, turn the users object into an array:

const users = { user1: 18273, user2: 92833, user3: 90315 }
const arr = Object.entries(users);
console.log(arr);

//b. Modify the outcome of part a, by multipling the user’s ID by 2.

const arr2 = arr.map((item) => {
    return [item[0], item[1]*2]
})
console.log(arr2);


//4. Analyze the code below. What will be the output?

class Person {
    constructor(name) {
      this.name = name;
    }
  }
  
  const member = new Person('John');
  console.log(typeof member);


//  5. Using the Dog class below:
// Analyze the options below. Which constructor will successfully extend the Dog class?

class Dog {
    constructor(name) {
      this.name = name;
    }
  };

class Labrador extends Dog {
    constructor(name, size) {
      super(name);
      this.size = size;
    }
  };

//  6. Evaluate these (ie True or False)
[2] === [2] //false
{} === {} //false

// What is, for each object below, the value of the property number and why?
const object1 = { number: 5 }; //5
const object2 = object1; //5
const object3 = object2; //5
const object4 = { number: 5}; //5

object1.number = 4; //4
console.log(object2); //4
console.log(object3); //4
console.log(object4); //5

// Create a class Animal with the attributes name, type and color
class Animal {
    constructor(name, type, color) {
        this.name = name;
        this.type = type;
        this.color = color;
    }
}


// Create a class Mamal that extends from the Animal class. Inside the class, add a method called sound(). This method takes a parameter: the sound the animal makes, and returns the details of the animal (name, type and color) as well as the sound it makes
class Mamal extends Animal {
    constructor(name, type, color) {
        super(name, type, color);
    }
    sound(sound) {
        return `${this.name} is a ${this.color} ${this.type} and it sounds ${sound}`;
    }
}


// Create a farmerCow object that is an instance of the class Mamal. The object accepts a name, a type and a color and calls the sound method that “moos” her information
let farmerCow = new Mamal("Milky", "cow", "black"); 
console.log(farmerCow.sound("moo"));



