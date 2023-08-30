//1. Create a function called compareToTen(num) that takes a number as an argument.
//      The function should return a Promise:
//      the promise resolves if the argument is less than or equal to 10
//      the promise rejects if argument is greater than 10.

function compareToTen(num) {
    return new Promise((resolve, reject) => {
        if (num <= 10) {
            resolve("The number is less than or equal to 10");
        } else {
            reject("The number is greater than 10");
        }
    })
}
compareToTen(15);
compareToTen(8);

// 2. Create a promise that resolves itself in 4 seconds and returns a “success” string.

function resolveInFourSeconds() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve("success");
        }, 4000)
    })
}
resolveInFourSeconds();


//3a. Use Promise.resolve(value) to create a promise that will resolve itself with a value of 3.
function resolveThree() {
    return Promise.resolve(3);
}
resolveThree();

// 3b. Use Promise.reject(error) to create a promise that will reject itself with the string “Boo!”
function rejectBoo() {
    return Promise.reject("Boo!");
}
rejectBoo();
