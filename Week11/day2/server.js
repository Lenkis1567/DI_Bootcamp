const http = require('http');
const user = {
    firstname: 'John',
    lastname: 'Doe'
}
const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader("Content-Type", "application/json");
  res.end(JSON.stringify(user));
})
  server.listen(8080);
console.log('Node.js web server at port 8080 is running..')