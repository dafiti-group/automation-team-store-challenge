from core.scraping.scraper import Scraping as scraper
from core.models import Produto

import re

def scraping():
    all_results = scraper.get_all_products()
    Produto.objects.all().update(status=False)

    for result in all_results:
        produto = Produto.objects.filter(descricao=result["descricao"], loja=result["loja"]).exists()
        if not produto:
            Produto.objects.update_or_create(
                descricao=result["descricao"],
                preco_original=result["preco_original"],
                preco_promocional=result["preco_promocional"],
                promocao=result["promocao"],
                link_produto=result["link_produto"],
                link_img_produto=result["link_img_produto"],
                status=result["status"],
                loja=result["loja"],
                marca=result["marca"]
            )
            # print('Produto registrado')
        else:
            produto = Produto.objects.get(descricao=result["descricao"], loja=result["loja"])
            preco = produto.preco_original
            preco_promo = produto.preco_promocional
            link_img_produto = produto.link_img_produto
                
            if preco_promo != result["preco_promocional"] and result['promocao'] == True and result['status']:
                Produto.objects.filter(descricao=result["descricao"],loja=result["loja"]).update(
                    preco_original=result["preco_original"],
                    preco_promocional=result["preco_promocional"], 
                    promocao=result['promocao'], 
                    link_img_produto=result['link_img_produto'],
                    status=result['status']
                )
                # print ('Produto está em promoção')
            
            if preco_promo != result["preco_promocional"] and result['promocao'] == False and result['status']:
                Produto.objects.filter(descricao=result["descricao"],loja=result["loja"]).update(
                    preco_original=result["preco_original"],
                    preco_promocional=result["preco_promocional"], 
                    promocao=result['promocao'], 
                    link_img_produto=result['link_img_produto'],
                    status=result['status']
                )
                # print ('Produto não está em promoção')
            
            if link_img_produto != result['link_img_produto'] and result['status']==True:
                Produto.objects.filter(descricao=result["descricao"],loja=result["loja"]).update(
                    link_img_produto=result['link_img_produto'],
                    status=result['status'])

    #             print('Link da imagem do produto mudou')
            if result['status']==True:
                Produto.objects.filter(descricao=result["descricao"],loja=result["loja"]).update(status=True)
    print('Todos os produtos foram adicionados')