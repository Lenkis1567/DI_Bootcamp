const express = require('express');
const router = express.Router();

const {_getAllProducts,
    _getProduct,
    _searchProduct,
    _insertProduct,
    _deleteProduct,
    _updateProduct,
    _getAllProductsEjs 

} = require('../controllers/products.js')

// router.get('/api/products', (req,res)=> {
//     _getAllProducts(req,res)
// })

router.get('/api/products', _getAllProducts)
router.get('/api/search', _searchProduct)
router.get('/api/products/:id', _getProduct)
router.post('/api/products', _insertProduct)
router.delete('/api/products/:id', _deleteProduct)
router.put('/api/products/:id', _updateProduct)

router.get('/ejs/products', _getAllProductsEjs)


// router.get('/products', _getAllProducts)
// router.get('/search', _searchProduct)
// router.get('/products/:id', _getProduct)
// router.post('/products', _insertProduct)
// router.delete('/products/:id', _deleteProduct)
// router.put('/products/:id', _updateProduct)


module.exports = {
router
} 