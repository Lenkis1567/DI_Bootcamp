const fs = require('fs');
const express = require('express');
const path = require('path');
const app = express();
const user = { firstname: 'John', lastname: 'Doe' };

app.use(express.static(path.join(__dirname, 'public')));

app.listen(3000, () => {
    console.log('Server is running on port 3000');
  });
  
app.get('/users', (req, res) => {
    res.send(JSON.stringify(user));
});

app.get('/parameters/:id', (req, res) => {
    const id = req.params.id;
    obj={"id":id}
    console.log (id, obj)
    res.send(`Here is the result: ${JSON.stringify(obj)}`);
});
