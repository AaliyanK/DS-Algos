//#1 -- For loop in Javascript.
const fish = ['dory', 'bruce', 'marlin', 'nemo']; // Elements 
const nemo = ['nemo'];
const everyone = ['dory', 'bruce', 'marlin', 'nemo', 'gill', 'bloat', 'nigel', 'squirt', 'darla', 'hank'];
const large = new Array(10).fill('nemo');

function findNemo2(array) {
  for (let i = 0; i < array.length; i++) {
    if (array[i] === 'nemo') {
      console.log('Found NEMO!');
    }
  }
}

findNemo2(large) // O(n) -> Linear time

const boxes = [0,1,2,3,4,5];
function logFirstTwo(boxes){
    console.log(boxes[0]);
    console.log(boxes[1]);
}