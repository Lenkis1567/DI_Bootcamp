const {db} = require('../config/dbelephant.js');

const allUsers = () =>{
    return db('users')
    .select('*')
}

const register = (email, password) => {
    return db('users')
    .insert({email, password})
    .returning('*')
}
const login = (email) => {
    return db('users')
    .select('id', 'email', 'password')
    .where({email})
}

module.exports = {
    register,
    login,
    allUsers
}
