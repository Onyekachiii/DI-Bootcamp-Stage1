// Exercise 1

function displayNumbersDivisible() {
    let sum = 0;
  
    for (let i = 0; i <= 500; i++) {
      if (i % 23 === 0) {
        console.log(i);
        sum += i;
      }
    }
  
    console.log("Sum of all numbers divisible by 23:", sum);
  }
  
  displayNumbersDivisible();