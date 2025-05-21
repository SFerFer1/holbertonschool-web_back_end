const readline = require('readline');

const interfaz = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

console.log('Welcome to Holberton School, what is your name?');

interfaz.on('line', (input) => {
  process.stdout.write(`Your name is: ${input.trim()}\r`);
  setTimeout(() => {

    console.log('\nThis important software is now closing');
    interfaz.close();
  }, 0);
});
