const express = require('express');
const dotenv = require('dotenv');
const cors = require('cors');
const products_router = require('./routes/products.js')

const {db} = require('./config/dbelephant.js')
const app = express()
dotenv.config()

app.listen(process.env.PORT, ()=> {
    console.log(`run on port ${process.env.PORT}`)
}
)  //на инв файл. 

app.use(cors());
app.use (express.urlencoded({extended:true})); //body parser
app.use(express.json());
app.use ('/', products_router.router)
app.use('/', express.static(__dirname+'/public'))

// app.use ('/api', products_router.router) чтобы убрать из раутера

///api/search  get - name=ip search db by name


// db('products')
// .select('*')
// .then(data=>{
//     console.log(data)
// })
// .catch(e =>{
//     console.log(e);
// })