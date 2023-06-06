const knex = require('knex')

const db = knex ({
    client: 'pg',
    connection: {
        host: 'localhost',
        port: '5432', //можно 5433
        user: 'postgres',
        password: '220879',
        database:'dvdrental',
    }
});
// db.select('city', 'city_id')
// .from ('city')
// .then(rows=> {
//     console.log(rows);
// })
// .catch(err=>{
//     console.log(err)
// })

//possible to take table:
db('city')
.select('city', 'city_id')
.update({city: 'Tel Aviv'})
.where({city_id:99})
.then(rows=> {
    console.log(rows);
})
.catch(err=>{
    console.log(err)
})

