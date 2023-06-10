const express = require('express');
const dotenv = require('dotenv');
const cors = require('cors');
const reg_router = require('./routes/register.js')

const {db} = require('./config/_______________')
const app = express()
dotenv.config()

app.listen(process.env.PORT, ()=> {
    console.log(`run on port ${process.env.PORT}`)
})

app.use(cors());
app.use (express.urlencoded({extended:true})); //body parser
app.use(express.json());
app.use ('/', reg_router.router)
app.use('/', express.static(__dirname+'/public'))
