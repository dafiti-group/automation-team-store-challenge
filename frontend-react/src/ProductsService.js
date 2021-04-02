import axios from 'axios'

const API_URL = 'http://localhost:8000';

export default class ProductsService {

    getProducts(){
        const url = `${API_URL}/api/products/`;
        return axios.get(url).then(response => response.data);
    }
    getProductsByURL(link){
        const url = `${API_URL}${link}`;
        return axios.get(url).then(response => response.data);
    }
    getProductById(pk){
        const url = `${API_URL}/api/products/${pk}`;
        return axios.get(url).then(response => response.data);
    }
    deleteProduct(product){
        const url = `${API_URL}/api/products/${product.pk}`;
        return axios.delete(url);
    }
    createProduct(product){
        const url = `${API_URL}/api/products/`;
        return axios.post(url, product);
    }
    updateProduct(product){
        const url = `${API_URL}/api/products/${product.pk}`;
        return axios.put(url, product)
    }
    getCategories(){
        const url = `${API_URL}/api/categories/`;
        return axios.get(url).then(response => response.data);
    }
    createCategory(category){
        const url = `${API_URL}/api/categories/`;
        return axios.post(url, category)
    }
    getBrands(){
        const url = `${API_URL}/api/brands/`;
        return axios.get(url).then(response => response.data)
    }
    createBrand(brand){
        const url = `${API_URL}/api/brands/`;
        return axios.post(url, brand)
    }
}