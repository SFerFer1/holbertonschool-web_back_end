const countStudents = require('./3-read_file_async');

countStudents('database.csv')
  .then(() => console.log('Done'))
  .catch((err) => console.error(err.message));
