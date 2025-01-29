// - example of an asyncronous call

// console.log('start');

// setTimeout(() => {
//     console.log("this runs after 2 seconds");}, 2000
// );

// console.log('end');


// - before async, callbacks and promises were used

// console.log('start');

function fetchData() {
    return new Promise((resolve) => {
        setTimeout(()=> {
            resolve("data received!");
        }, 2000);
    });
}


// fetchData()
//     .then(data => console.log(data))
//     .catch(error => console.log(error));

// console.log('end');


// - calling a function async means it will handle promises

// console.log('start');

async function getData() {
    try {
        const data = await fetchData();
        console.log(data);
    } catch (error) {
        console.error("error: ", error);
    }
} 

// getData();
// console.log('end');


// - example: reading a file

const fs = require('fs').promises; 

async function readFile() {
    try {
        const content = await fs.readFile('./example.txt', 'utf-8');
        console.log("File content: ", content);
    } catch (error) {
        console.error("Error reading file: ", error);
    }
}

readFile();
console.log("reading file...")