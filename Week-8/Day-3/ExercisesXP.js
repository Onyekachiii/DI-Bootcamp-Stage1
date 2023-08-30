// With your knewly accumulated knowledge of the Fetch API lets write some cool code!
// You will use this Gif URL: https://api.giphy.com/v1/gifs/search?q=hilarious&rating=g&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My
// api_key Request Paramater : GIPHY API Key. Our API KEY is hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My

//1. Create a program to retrieve the data from the API URL provided above.
// Use the fetch() method to make a GET request to the Giphy API and Console.log the Javascript Object that you receive.

function getGif() {
    fetch('https://api.giphy.com/v1/gifs/search?q=hilarious&rating=g&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My')
    .then(response => response.json())
    .then(data => console.log(data))
}
getGif();

//2. Use the Fetch API to retrieve 10 gifs about the “sun”. The starting position of the results should be 2.

function getGif2() {
    fetch('https://api.giphy.com/v1/gifs/search?q=sun&rating=g&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My&limit=10&offset=2')
    .then(response => response.json())
    .then(data => console.log(data))
}
getGif2();

// Improve the program below :
fetch("https://www.swapi.tech/api/starships/9/")
    .then(response => response.json())
    .then(objectStarWars => console.log(objectStarWars.result));

// Create an async function, that will await for the above GET request.
// The program shouldn’t contain any then() method.

async function getStarWars() {
    let response = await fetch("https://www.swapi.tech/api/starships/9/");
    let objectStarWars = await response.json();
    console.log(objectStarWars.result);
}
getStarWars();


// Analyse the code provided below - what will be the outcome?
function resolveAfter2Seconds() {
    return new Promise(resolve => {
        setTimeout(() => {
            resolve('resolved');
        }, 2000);
    });
}

async function asyncCall() {
    console.log('calling');
    let result = await resolveAfter2Seconds();
    console.log(result);
}

asyncCall();  //calling, resolved