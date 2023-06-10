const {getAllregs,
     

} = require('../modules/reg.js');

const _getAllregs = (req, res) => {
    getAllregs()
    .then(data => {
        res.json(data)
    })
    .catch(err=> {
        console.log(err);
        res.status(404).json({msg:err.message})
    })
}

const _getProduct = (req, res) => {
const id = req.params.id;
getProduct(id)
.then(data => {
    res.json(data)
})
.catch(err=> {
    console.log(err);
    res.status(404).json({msg:err.message})
})
}

const _searchProduct = (req,res) => {
    console.log(req.query)
    searchProduct(req.query.name)
    .then(data=>{
        res.json(data)
    })
    .catch(err=>{
        console.log(err);
        res.status(404).json({msg:err.message})
    })
}

const _insertProduct = (req, res) => {
    insertProduct(req.body)
    .then (data => {
        res.json(data)
    })
    .catch(err=>{
        console.log(err);
        res.status(404).json({msg:err.message})
    })
}

const _deleteProduct = (req, res) => {
    deleteProduct(req.params.id)
      .then(data => {
        res.json(data)
    })
    .catch(err=> {
        console.log(err);
        res.status(404).json({msg:err.message})
    })
}

const _updateProduct = (req, res) => {
    updateProduct(req.params.id, req.body)
    .then(data => {
        res.json(data)
    })
    .catch(err=> {
        console.log(err);
        res.status(404).json({msg:err.message})
    })
}


module.exports= {
    _getAllProducts,
    _getProduct,
    _searchProduct,
    _deleteProduct,
    _updateProduct,
    _insertProduct
}