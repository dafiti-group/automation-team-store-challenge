import React, { Component } from 'react';
import { BrowserRouter, Route } from 'react-router-dom'
import './App.css'

import ProductsList from './ProductsList'
import ProductCreateUpdate from './ProductCreateUpdate'


const BaseLayout = () => (
  <div className="container-fluid">
    <nav className="navbar navbar-expand-lg navbar-light bg-light">
      <a className="navbar-brand"  href="/">Gerenciador de Produtos - Dafiti CHLLNG</a>
      <button  className="navbar-toggler"  type="button"  data-toggle="collapse"  data-target="#navbarNavAltMarkup"  aria-controls="navbarNavAltMarkup"  aria-expanded="false"  aria-label="Toggle navigation">
        <span  className="navbar-toggler-icon"></span>
      </button>
      <div  className="collapse navbar-collapse"  id="navbarNavAltMarkup">
        <div  className="navbar-nav">
            <a  className="nav-item nav-link"  href="/">Produtos</a>
            <a  className="nav-item nav-link"  href="/product">Adicionar Produto</a>
        </div>
      </div>
    </nav>
    <div className="content">
      <Route path="/" exact component={ ProductsList } />
      <Route path="/product/" exact component={ ProductCreateUpdate } />
      <Route path="/product/:pk" component={ ProductCreateUpdate } />
    </div>
  </div>
);

class App extends Component {
  render() {
    return (
      <BrowserRouter>
        <BaseLayout />
      </BrowserRouter>
    );
  }
}

export default App