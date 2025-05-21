const readDatabase = require('../utils');

class StudentsController {
  static async getAllStudents(request, response) {
    const path = process.argv[2];

    try {
      const studentsByField = await readDatabase(path);

      let output = 'This is the list of our students';

      const sortedFields = Object.keys(studentsByField).sort((a, b) =>
        a.toLowerCase().localeCompare(b.toLowerCase())
      );

      for (const field of sortedFields) {
        const names = studentsByField[field];
        output += `\nNumber of students in ${field}: ${names.length}. List: ${names.join(', ')}`;
      }

      response.status(200).send(output);
    } catch (error) {
      response.status(500).send('Cannot load the database');
    }
  }

  static async getAllStudentsByMajor(request, response) {
    const { major } = request.params;
    const path = process.argv[2];

    if (major !== 'CS' && major !== 'SWE') {
      return response.status(500).send('Major parameter must be CS or SWE');
    }

    try {
      const studentsByField = await readDatabase(path);
      const names = studentsByField[major] || [];

      return response.status(200).send(`List: ${names.join(', ')}`);
    } catch (error) {
      return response.status(500).send('Cannot load the database');
    }
  }
}

module.exports = StudentsController;
