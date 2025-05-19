const readline = require('readline');

const interfaz = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

console.log('Welcome to Holberton School, what is your name?');

interfaz.on('line', (input) => {
  console.log(`Your name is: ${input.trim()}`);
  interfaz.close();
});

interfaz.on('close', () => {

  if (!process.stdin.isTTY) {
    console.log('This important software is now closing');
  }
});
