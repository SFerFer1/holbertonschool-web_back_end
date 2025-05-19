const readline = require('readline');

const interfaz = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

process.on('SIGINT', () => {
  console.log('\nThis important software is now closing');
  process.exit();
});

console.log('Welcome to Holberton School, what is your name?');

interfaz.on('line', (input) => {
  console.log(`Your name is: ${input}`);
  console.log('This important software is now closing');
  
});
