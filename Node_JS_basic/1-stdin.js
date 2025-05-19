const readline = require('readline');

const interfaz = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const a = 'Welcome to Holberton School, what is your name?\n';

interfaz.question(a, (answer) => {
  console.log(`Your name is: ${answer}`);
  interfaz.close();
});

process.on('SIGINT', () => {
  console.log('\nThis important software is now closing');
  process.exit();
});
