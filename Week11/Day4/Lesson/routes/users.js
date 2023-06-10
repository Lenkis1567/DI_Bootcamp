const express = require('express');
const router = express.Router();

const {_register, _login, _allUsers} = 
require('../controllers/users.js')

router.post('/register', _register);
router.post('/login', _login);
router.get('/users', _allUsers);

module.exports ={
    router
}
// "email": "john@mail.ru",
// "password": "johnsmith"