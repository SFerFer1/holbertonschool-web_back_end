const readline = require('readline');

const interfaz = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

console.log('Welcome to Holberton School, what is your name?\n');

interfaz.on('line', (input) => {
  process.stdout.write(`Your name is: ${input.trim()}`);
  setTimeout(() => {

    console.log('\nThis important software is now closing\n');
    interfaz.close();
  }, 0);
});
