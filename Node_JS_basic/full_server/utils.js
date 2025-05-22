const fs = require('fs').promises;

async function readDatabase(path) {
  const data = await fs.readFile(path, 'utf-8');
  const lineas = data.split('\n').filter((linea) => linea.trim() !== '');
  lineas.shift();

  const StudentsByField = {};
  lineas.forEach((linea) => {
    const datos = linea.split(',');
    const FirstName = datos[0].trim();
    const Field = datos[3].trim();

    if (!StudentsByField[Field]) {
      StudentsByField[Field] = [];
    }

    StudentsByField[Field].push(FirstName);
  });

  return StudentsByField;
}

module.exports = readDatabase;
