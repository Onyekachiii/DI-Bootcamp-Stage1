// const numbers = [10,11,12,15,20]

// for (number in numbers) {
//   if (number % 2 == 0) {
//     console.log(number);
//   }
// }

const words = [wow, hey, bye];

startsWithh = false;
for(let i = 0; i < words.length; i++) {
  if(words[i][0] === 'h') {
    startsWithh = true;
    break;
  }
}
console.log(startsWithh);  