import React, { useState, useEffect } from 'react'
import ProductsService from './ProductsService'
import { useForm } from 'react-hook-form'
import { useParams } from 'react-router-dom'

const productsService = new ProductsService();

function ProductCreateUpdate () {
    
    const [categories, setCategories] = useState([]);
    const [brands, setBrands] = useState([]);
    const [categoryName, setCategoryName] = useState("");
    const [categoryDesc, setCategoryDesc] = useState("");
    const [brandName, setBrandName] = useState("");
    const [catVisible, setCatVisible] = useState(false);
    const [braVisible, setBraVisible] = useState(false);
    const [typeOpts] = useState(['Camisa', 'Camiseta', 'Polo', 'Calça', 'Bermuda', 'Casaco']);
    const [genderOpts] = useState(['Masculino', 'Feminino']);
    const [sizeOpts] = useState(['PP', 'P', 'M', 'G', 'GG']);

    const {handleSubmit, register, reset} = useForm();
    const { pk } = useParams();

    const handleCreate = async (product) => {
        const result = await productsService.createProduct({
            "name": product.name,
            "category": product.category,
            "product_type": product.productType,
            "gender": product.gender,
            "size": product.size,
            "brand": product.brand,
            "color": product.color,
            "price": product.price,
            "category_obj": (categoryName !== "") ? {"name": categoryName, "description": categoryDesc} : null,
            "brand_obj": (brandName !== "") ? {"name": brandName} : null
        });
        if (result.status === 201) {
            alert("Produto adicionado!");
        } else {
            alert("Erro ao adicionar produto. Verifique os campos e tente novamente.");
        }
    }

    const handleUpdate = async (pkey, product) => {
        const result = await productsService.updateProduct({
            "pk": pkey,
            "name": product.name,
            "category": product.category,
            "product_type": product.productType,
            "gender": product.gender,
            "size": product.size,
            "brand": product.brand,
            "color": product.color,
            "price": product.price,
            "category_obj": (categoryName !== "") ? {"name": categoryName, "description": categoryDesc} : null,
            "brand_obj": (brandName !== "") ? {"name": brandName} : null
        });
        if (result.status === 200) {
            alert("Informações sobre o produto alteradas!");
        }else {
            alert("Erro ao alterar dados do produto. Verifique os campos e tente novamente.");
        }
    }

    const onSubmit = data => {
        if (pk) {
            handleUpdate(pk, data);
        }
        else{
            handleCreate(data);
        }
    }

    const showCategoryDiv = () => (
        <div className="row">
            <label>Nova categoria:</label>
            <input className="form-control col-sm marginHor10 marginVert10" type="text" onChange={e => setCategoryName(e.target.value)} placeholder="Nome da categoria" />
            <input className="form-control col-sm marginHor10 marginVert10" type="text" onChange={e => setCategoryDesc(e.target.value)} placeholder="Descrição" />
            <div className="col-sm">
                <button className="btn btn-link marginVert10" onClick={(e) => {setCatVisible(false); setCategoryName("")}}>Cancelar</button>
            </div>
        </div>
    );

    const showBrandDiv = () => (
        <div className="row">
            <label>Nova marca:</label>
            <input className="form-control col-sm marginHor10 marginVert10" type="text" onChange={e => setBrandName(e.target.value)} placeholder="Nome da marca" />
            <div className="col-sm">
                <button className="btn btn-link marginVert10 marginVert10" onClick={(e) => {setBraVisible(false); setBrandName("")}}>Cancelar</button>
            </div>
        </div>
    );

    useEffect(() => {
        const fetchCategories = async () => {
            const resultCat = await productsService.getCategories();
            setCategories(resultCat)
        }

        const fetchBrands = async () => {
            const resultBran = await productsService.getBrands();
            setBrands(resultBran)
        }

        if (pk) {
            const fetchProducts = async () => {
                const prod = await productsService.getProductById(pk);
                reset({...prod, productType: prod.product_type})
            }
            fetchProducts();
        }
        fetchCategories();
        fetchBrands();
    }, [pk, reset]);

    return(
        <form onSubmit={handleSubmit(onSubmit)}>
        <div className="form-group">
            <label>Nome:</label>
            <input className="form-control" type="text" name="name" required ref={register} />
            <label>Categoria:</label>
            <select className="form-control" name="category" ref={register}>
            <option value={null}>Selecione</option>
                {categories.map( c => 
                    <option key={c.pk} value={c.pk}>{c.name}</option>
                 )}
            </select>
            <div>
                <button className="btn btn-link marginVert10" onClick={(e) => setCatVisible(true)}>Adicionar nova categoria</button>
            </div>

            {catVisible ? showCategoryDiv() : null}

            <label>Tipo:</label>
            <select className="form-control" name="productType" required ref={register}>
                {typeOpts.map( (t, index) =>
                    <option value={index+1}>{t}</option>
                 )}
            </select>
            <label>Gênero:</label>
            <select className="form-control" name="gender" required ref={register}>
                {genderOpts.map( (g, index) => 
                    <option value={index+1}>{g}</option>
                 )}
            </select>
            <label>Tamanho:</label>
            <select className="form-control" name="size" required ref={register}>
                {sizeOpts.map( (s, index) => 
                    <option value={index+1}>{s}</option>
                 )}
            </select>
            <label>Cor:</label>
            <input className="form-control" type="text" required name="color" ref={register} />
            <label>Marca:</label>
            <select className="form-control" name="brand" ref={register}>
                <option value={null}>Selecione</option>
                {brands.map( b =>
                    <option key={b.pk} value={b.pk}>{b.name}</option>
                 )}
            </select>
            <div>
                <button className="btn btn-link marginVert10" onClick={(e) => setBraVisible(true)}>Adicionar nova marca</button>
            </div>

            {braVisible ? showBrandDiv() : null}

            <label>Preço:</label>
            <input className="form-control" type="text" pattern="[+,0-9.]*" name="price" required ref={register} />

            <div className="row">
                <div className="col-sm">
                    <input className="btn btn-success position-absolute end-50 marginVert10" type="submit" value="Salvar" />
                </div>
            </div>
        </div>
        </form>
    );
}

export default ProductCreateUpdate;