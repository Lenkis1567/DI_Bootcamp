const http = require('http');

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/html');
res.end(`
    <h1>Hello, Daniel</h1>
    <p>It's a new crazy staff and we still didn't finish the hakaton</p>
    <p>DIsaster</p>`
  );
});
server.listen(3000, 'localhost', () => {
    console.log('Server is running at http://localhost:3000/');
  });