import requests


class RequestDummyJSon:
    _BASE_URL = "https://dummyjson.com/"
    _ALL_PRODUCTS = "products"
    _ADD_UPDATE_PRODUCTS = "/add"

    @property
    def generate_token(self):
        auth_link = "https://dummyjson.com/auth/login"
        body_json = {
            "username": "kminchelle",
            "password": "0lelplR"
        }

        response = requests.post(auth_link, json=body_json)
        return f"Bearer {response.json()['token']}"

    def generate_headers_params(self):
        return {'Authorization': self.generate_token}

    def login(self):
        auth_link = "https://dummyjson.com/auth/login"
        body_json = {
            "username": "kminchelle",
            "password": "0lelplR"
        }
        response = requests.post(auth_link, json=body_json)
        return response

    def get_all_products(self, limit=0, skip=0, select=""):
        products_url = self._BASE_URL + self._ALL_PRODUCTS
        params = []
        if limit != 0:
            params.append(f'limit={limit}')
        if skip != 0:
            params.append(f'skip={skip}')
        if select:
            params.append(f'select={select}')
        if params:
            products_url += "?" + "&".join(params)

        response = requests.get(products_url)
        return response

    def get_a_single_product(self, id_prod=None, select=""):
        products_url = self._BASE_URL + self._ALL_PRODUCTS+ f"/{id_prod}" + f"?select={select}"
        reponse = requests.get(products_url)
        return reponse

    def search_products(self, search_product):
        search_url = self._BASE_URL + self._ALL_PRODUCTS + f"/search?q={search_product}"
        response = requests.get(search_url)
        return response

    def add_product(self, name=""):
        add_prod_url = self._BASE_URL + self._ALL_PRODUCTS + self._ADD_UPDATE_PRODUCTS
        body_json = {
            "title": name
        }
        response = requests.post(add_prod_url, json=body_json)
        return response

    def update_product(self, id_product, title_name):
        update_url = self._BASE_URL + self._ALL_PRODUCTS + f'/{id_product}'
        body_json = {
            "title": title_name
        }
        response = requests.put(update_url, json=body_json)
        return response

    def delete_product(self, id_product):
        delete_url = self._BASE_URL + self._ALL_PRODUCTS + f"/{id_product}"
        response = requests.delete(delete_url)
        return response
#
# authtest = RequestDummyJSon()
# print(authtest.generate_headers_params())

