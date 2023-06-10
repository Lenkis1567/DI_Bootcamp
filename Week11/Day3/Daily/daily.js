const express = require('express');
const app = express();

app.listen(3001, () => {
  console.log('Server is running on port 3001');
});

app.use('/', express.static(__dirname + '/public'));
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

app.get('/aboutme/:hobby', (req, res) => {
  const hobby = req.params.hobby;
  if (isNaN(hobby)) {
    res.status(200).send(`My hobby is ${hobby}`);
  } else {
    res.status(404).send('Hobby not found');
  }
});

// app.get('/', (req, res) => {
//     res.sendFile(__dirname + '/about.html');
//   });

app.get('/formData/:email', (req, res) => {
    console.log(req);
    const email = req.query.email;
    const message = req.query.message;
    const output = `${email} sent you a message: "${message}"`;
    res.send(output);
  });