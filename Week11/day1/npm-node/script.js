const {largeNumber, getCurrentDateTime} = require('./main1.js')
const b = 5
console.log(largeNumber+b)
const result = largeNumber + b;
let http = require("http");
let time=getCurrentDateTime()
const server = http.createServer( (req,res) => {
    console.log('I am listening....');
    // res.writeHead(200);
    res.setHeader("Content-Type", "text/html")
    res.write (`The date and time are currently ${time}.`)
    res.write (`<p>My Module is ${result}</p>. <h1>Hi there at the frontend</h1>`)
    res.end();
 
 });

server.listen(8080);
