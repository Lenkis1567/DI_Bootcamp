const {db} = require('../config/dbreg.js');
const getAllregs = () => {
    return db('register')
    .select('id', 'first_name', 'last_name', 'email', 'username', 'date_created', 'last_login')
    .orderBy('id')
}

