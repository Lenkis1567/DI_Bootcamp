const express = require('express');
const app = express();

app.get('/', (req, res) => {
    res.send('<h1>Hello again, I understand nothing</h1>');
  });
app.listen(3001, () => {
    console.log('Server is running on http://localhost:3001/');
  });