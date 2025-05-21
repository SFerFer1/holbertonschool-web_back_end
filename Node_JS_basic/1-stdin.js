const readline = require('readline');

const interfaz = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

console.log('Welcome to Holberton School, what is your name?');

interfaz.on('line', (input) => {
  process.stdout.write(`Your name is: ${input.trim()}\n`);
  interfaz.close();
});

interfaz.on('close', () => {
  console.log('\nThis important software is now closing');
});
