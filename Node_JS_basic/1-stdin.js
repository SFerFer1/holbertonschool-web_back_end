const readline = require('readline');

const interfaz = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

console.log('Welcome to Holberton School, what is your name?');

interfaz.on('line', (input) => {
  console.log(`Your name is: ${input.trim()}\r`);
  interfaz.close();
});

interfaz.on('close', () => {
  console.log('This important software is now closing');
});
