const http = require('http');
const user = {
    firstname: 'John',
    lastname: 'Doe'
}
const readline = require('readline');

const {timeUntilJan1, timelived} = require('./date.js')
const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader("Content-Type", "application/json");
  res.end(JSON.stringify(user));
})
  server.listen(8080);
console.log('Node.js web server at port 8080 is running..')
const timeLeft = timeUntilJan1();

// const timeLived=timelived(2000, 1, 1)
console.log('The first january is in', timeLeft)
// console.log("the personlived", timeLived, " minutes")


const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.question('Enter your birthdate (YYYY-MM-DD): ', (birthdateString) => {
  rl.close();

  const [year, month, day] = birthdateString.split('-');
  const minutesLived = timelived(year, month, day);

  console.log(`You have lived approximately ${minutesLived.minutes} minutes.`);
});