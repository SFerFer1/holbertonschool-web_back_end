const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf-8').trim();

    const lineas = data.split('\n').filter((lineas) => lineas.trim() !== '');
    lineas.shift();

    const StudentsByField = {};
    let AllStudents = 0;

    lineas.forEach((lineas) => {
      const StudentData = lineas.split(',');
      if (StudentData.length >= 4) {
        const FirstName = StudentData[0];
        const Field = StudentData[3];

        if (!StudentsByField[Field]) StudentsByField[Field] = [];
        StudentsByField[Field].push(FirstName);

        AllStudents += 1;
      }
    });
    console.log(`Number of students: ${AllStudents}`);
    Object.entries(StudentsByField).forEach(([field, list]) => {
      console.log(
        `Number of students in ${field}: ${list.length}. List: ${list.join(', ')}`,
      );
    });
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
