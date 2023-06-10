const express = require('express');
const ejs = require('ejs')

const app=express();

//set template engine
app.set('view engine', 'ejs');

app.listen(process.env.PORT||3030, ()=> {
    console.log(`run on ${process.env.PORT||3030}`);
})
// app.get('/', (req, res)=> {
//     // res.send('<h1>Hello ejs</>')
// let login=true;
// let user = {
//     'firstname':'john',
//     'lastname': 'smith'
// }
// res.render('index', {
//     login:login
// })

//     res.render('index', {
//         'firstname':'john',
// 'lastname': 'smith'
    // })
//     res.render('index', {

// })
// })
// ========

// app.get('/', (req, res)=> {
// res.render('index', {
//     login:login
// })

app.render('/shop', (req,res)=>{
    res.render
})