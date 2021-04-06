import React,  {useState, useEffect} from 'react';
import ProductsService from './ProductsService';

const productService = new ProductsService();

function ProductsList() {

    const [products, setProducts] = useState([]);
    const [nextPageURL, setNextPageURL] = useState('');
    const [numPages, setNumPages] = useState(0);
    const [countProds, setCountProds] = useState(0);

    useEffect(() => {
        const fetchData = async () => {
            const result = await productService.getProducts();
            setProducts(result.data);
            setNextPageURL(result.nextlink);
            setCountProds(result.count);
            setNumPages(result.numpages);
        }
        fetchData();
    }, []);

    const handleDelete = async (e, pk) => {
        await productService.deleteProduct({pk: pk});
        var newArrProd = products.filter(function(obj) {
            return obj.pk !== pk;
        })
        setProducts(newArrProd);
    }

    const nextPage = async e => {
        const result = await productService.getProductsByURL(nextPageURL);
            setProducts(result.data);
            setNextPageURL(result.nextlink);
    }

    return(
        <div className="products--list">
            <table className="table">
                <thead key="thead">
                    <tr>
                        <th>Código</th>
                        <th>Nome</th>
                        <th>Categoria</th>
                        <th>Tipo</th>
                        <th>Gênero</th>
                        <th>Tamanho</th>
                        <th>Cor</th>
                        <th>Marca</th>
                        <th>Preço</th>
                    </tr>
                </thead>
                <tbody>
                {products.map( prod => 
                    <tr key={prod.pk}>
                        <td>{prod.pk}</td>
                        <td>{prod.name}</td>
                        <td>{prod.category_name}</td>
                        <td>{prod.product_type_name}</td>
                        <td>{prod.gender_name}</td>
                        <td>{prod.size_name}</td>
                        <td>{prod.color}</td>
                        <td>{prod.brand_name}</td>
                        <td>{prod.price}</td>
                        <td>
                            <a className="marginHor10" href={"/product/" + prod.pk}>Editar</a>
                            <button className="btn btn-link marginHor10" onClick={(e) => handleDelete(e, prod.pk)}>Excluir</button>
                        </td>
                    </tr>
                )}
                </tbody>
            </table>
            <div className="row marginHor10">
                <div className="col-sm">
                    <p className="" >{countProds} produto(s) encontrado(s). {numPages} página(s).</p> 
                </div>
                <div className="col-sm">
                    <button className="btn btn-primary marginHor10 position-absolute end-0" onClick={(e) => nextPage(e)}>Próximo</button>
                </div>                           
            </div>
        </div>
    );
}

export default ProductsList