from utils import tools
import requests


class ViaCep:
    def __init__(self):
        self.base_url = 'https://viacep.com.br/ws/'

        self.zipcode = None
        self.street = None
        self.district = None
        self.city = None
        self.uf = None
        self.complement = None

        self.erro = False

    def consult(self, zipcode: str):
        """
        Método para consultar o CEP
        :param zipcode: CEP
        :return: object
        """
        zipcode = tools.only_numbers(zipcode)
        url = self.base_url + zipcode + '/json/'

        try:
            result = requests.get(url).json()
        except Exception as error:
            self.erro = True
            return self

        if result.get('erro'):
            self.erro = True
            return self

        self.zipcode = tools.only_numbers(result.get('cep'))
        self.street = result.get('logradouro')
        self.district = result.get('bairro')
        self.city = result.get('localidade')
        self.uf = result.get('uf')
        self.complement = result.get('complemento')
        return self

    def __str__(self):
        return "{'zipcode': %s, 'street': %s}" % (self.zipcode, self.street)
