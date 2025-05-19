const { ALL } = require('dns');
const fs = require('fs');

function countStudents(path) {
  try{
    const data = fs.readFileSync(path, 'utf-8').trim();

    const lineas = data.split('\n').filter((lineas) => lineas.trim() != '');
    const header = lineas.shift();

    const StudentsByField = {};
    let AllStudents = 0;

    lineas.forEach((lineas) => {
    const StudentData = lineas.split(',');
    if (StudentData.length >= 4) {
        const FirstName = StudentData[0];
        const Field = StudentData[3];
        
        if (!StudentsByField[Field]) StudentsByField[Field] = [];
        StudentsByField[Field].push(FirstName);

        AllStudents++;
    }
    });
    console.log(`Number of students: ${AllStudents}`);
    for (const field in StudentsByField) {
      const list = StudentsByField[field];
      console.log(
        `Number of students in ${field}: ${list.length}. List: ${list.join(', ')}`
      );
    }
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;