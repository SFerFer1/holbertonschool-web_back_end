import express from 'express';
import routes from './routes/index';

const app = express();
const port = 1245;

app.use('/', routes);

const server = app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});

// Export both for different use cases
export default app;
export { server };
