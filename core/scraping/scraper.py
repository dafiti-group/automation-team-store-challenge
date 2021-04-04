#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 08:32:48 2021

@author: nayannanara
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import re
from decouple import config


class Scraping():

    def __init__(self):
        self.url_dafiti = [
            'https://www.dafiti.com.br/calcados-masculinos/tenis-para-corrida/adidas--adidas-originals--adidas-performance/?cat-pwa=0&campwa=0',
            'https://www.dafiti.com.br/calcados-masculinos/nike--nike-sb--nike-sportswear/?cat-pwa=0&campwa=0'
            ]
        self.url_zattini = [
            'https://www.zattini.com.br/adidas?mi=ztt_mntop_ESP-MC-adidas&psn=Menu_Top&genero=masculino&tipo-de-produto=tenis&tipo-de-produto=tenis-performance',
            'https://www.zattini.com.br/nike?nsCat=Natural&q=nike&genero=masculino&tipo-de-produto=tenis&tipo-de-produto=tenis-performance'
        ]
        
        self.all_products = []

    def scraping_dafiti(self):
        chrome_options = Options()
        # chrome_options.binary_location = config('GOOGLE_CHROME_BIN')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--headless')
        
        # driver = webdriver.Chrome(executable_path=config('CHROMEDRIVER_PATH'), options=chrome_options)
        driver = webdriver.Remote(
            command_executor="http://selenium:4444/wd/hub",
            desired_capabilities=DesiredCapabilities.FIREFOX
        )
        # driver = webdriver.Chrome(executable_path='./core/scraping/chromedriver', options=chrome_options)
        urls_dafiti = []  
        for url in self.url_dafiti:

            driver.get(url)
            sleep(3)
            
            ul_pag = driver.find_element_by_class_name('pagination-list').find_elements_by_tag_name('li')[-2].text
            num_page = []
            
            for pag in range(1,(int(ul_pag)+1)):
                num_page.append(pag)
            
             
            for x in num_page:
                url_page = f"{url}&page={x}"
                urls_dafiti.append(url_page)
            
        for url in urls_dafiti:
            driver.get(url)
            driver.execute_script('window.scrollBy(0, 300)')
            sleep(2)
            driver.execute_script('window.scrollBy(0, 600)')
            driver.execute_script('window.scrollBy(0, 900)')
            sleep(2)
            driver.execute_script('window.scrollBy(0, 1200)')
            driver.execute_script('window.scrollBy(0, 1500)')
            sleep(2)
            driver.execute_script('window.scrollBy(0, 1800)')
            driver.execute_script('window.scrollBy(0, 2100)')
            
            try:
                button = driver.find_element_by_xpath('//*[@id="dy_newsletter_submit"]/div[3]/button[2]').click()
            except:
                pass
            
            products = driver.find_elements_by_class_name('product-box')
            
            for product in products:
                div_detail = product.find_element_by_class_name('product-box-detail')
                marca = div_detail.find_element_by_class_name('product-box-brand').text
                descricao = div_detail.find_element_by_class_name('product-box-title').text
                div_precos = product.find_element_by_class_name('product-box-price')
                link_produto = product.find_element_by_class_name('product-box-link').get_attribute('href')
                link_img_produto = product.find_element_by_class_name('product-image').get_attribute('src')
                loja = 'Dafiti'
                
                try:
                    preco_original = div_precos.find_element_by_class_name('product-box-price-from').text
                except:
                    preco_original = 0.00

                try:
                    preco_promocional = div_precos.find_element_by_class_name('product-box-price-to').text     
                except:
                    preco_promocional = 0.00
                
                if preco_promocional != 0:    
                    promocao = True
                else:
                    promocao = False
                
                if type(preco_original) == str:
                    if preco_original:
                        preco_original = re.sub('[^0-9]', '', preco_original)
                        preco_original = float(int(preco_original)/100)
                    else:
                        preco_original = 0
                else:
                    preco_original = float(preco_original)

                if type(preco_promocional) == str:
                    if preco_promocional:
                        preco_promocional = re.sub('[^0-9]', '', preco_promocional)
                        preco_promocional = float(int(preco_promocional)/100)
                    else:
                        preco_promocional = 0
                else:
                    preco_promocional = preco_promocional
                
                product = {
                    'descricao': descricao,
                    'preco_original': preco_original,
                    'preco_promocional': preco_promocional,
                    'link_produto': link_produto,
                    'promocao': promocao,
                    'link_img_produto': link_img_produto,
                    'marca': marca,
                    'status': True,
                    'loja': loja
                }
                if preco_original != 0:
                    self.all_products.append(product)
        return self.all_products

    def scraping_zattini(self):
        chrome_options = Options()
        # chrome_options.binary_location = config('GOOGLE_CHROME_BIN')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--headless')
        
        # driver = webdriver.Chrome(executable_path=config('CHROMEDRIVER_PATH'), options=chrome_options)
        driver = webdriver.Remote(
            command_executor="http://selenium:4444/wd/hub",
            desired_capabilities=DesiredCapabilities.FIREFOX
        )
        # driver = webdriver.Chrome(executable_path='./core/scraping/chromedriver', options=chrome_options)
        urls_zattini = []   

        for url in self.url_zattini:
            driver.get(url)
            ul_pag = driver.find_element_by_class_name('pagination').find_elements_by_tag_name('a')[-2].text
            num_page = []
            
            for pag in range(1,(int(ul_pag)+1)):
                num_page.append(pag)
            
            for x in num_page:
                url_page = f"{url}&page={x}"
                urls_zattini.append(url_page)
            
        for url in urls_zattini:
            driver.get(url)
            driver.execute_script('window.scrollBy(0, 300)')
            sleep(2)
            driver.execute_script('window.scrollBy(0, 600)')
            driver.execute_script('window.scrollBy(0, 900)')
            sleep(2)
            driver.execute_script('window.scrollBy(0, 1200)')
            driver.execute_script('window.scrollBy(0, 1500)')
            sleep(2)
            driver.execute_script('window.scrollBy(0, 1800)')
            driver.execute_script('window.scrollBy(0, 2100)')
    
        
            products = driver.find_elements_by_class_name('item-card')
        
            for product in products:
                descricao = product.find_element_by_class_name('item-card__description__product-name').text
                marca = product.find_element_by_xpath('//*[@id="content"]/section/section[2]/h1').text
                link_produto = product.find_element_by_class_name('item-card__images__image-link').get_attribute('href')
                link_img_produto = product.find_element_by_class_name('item-card__images__image-link').find_element_by_tag_name('img').get_attribute('src')
                loja = 'Zattini'

                try:
                    preco_original = product.find_element_by_tag_name('del').text
                    preco_promocional = product.find_element_by_class_name('haveInstallments').get_attribute('content')
                except:
                    try:
                        preco_original = product.find_element_by_class_name('haveInstallments').get_attribute('content')
                        preco_promocional = 0.00 
                    except:
                        preco_original = 0.00
                        preco_promocional = 0.00
                
                if preco_promocional == 0:
                    promocao = False
                else:
                    promocao = True

                if type(preco_promocional) == str:
                    preco_promocional = re.sub('[^0-9]', '', preco_promocional)
                    preco_promocional = float(int(preco_promocional)/100)
                else:
                    preco_promocional = preco_promocional
                
                if type(preco_original) == str:
                    preco_original = re.sub('[^0-9]', '', preco_original)
                    preco_original = float(int(preco_original)/100)
                else:
                    preco_original = preco_original

                product = {
                    'descricao': descricao,
                    'preco_original': preco_original,
                    'preco_promocional': preco_promocional,
                    'link_produto': link_produto,
                    'promocao': promocao,
                    'link_img_produto': link_img_produto,
                    'marca': marca,
                    'status': True,
                    'loja': loja
                }
                if preco_original != 0:   
                    self.all_products.append(product)
        return self.all_products


    def get_all_products():
        scraper = Scraping()
        all_products = scraper.scraping_dafiti() + scraper.scraping_zattini()
        # all_products = scraper.scraping_zattini()
        return all_products
# Scraping.get_all_products()

    