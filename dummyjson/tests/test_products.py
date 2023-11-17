from itertools import count

from dummyjson.pages.requets_dummy_json import RequestDummyJSon


def test_get_all_products():
    dummy = RequestDummyJSon()
    response = dummy.get_all_products()
    assert 200 == response.status_code, " Unexpected status code"
    # checking if we getting 30 products bydefault
    assert 30 == len(response.json()['products']), "Unexpected response size"


def test_get_products_using_limit_10():
    dummy = RequestDummyJSon()
    reponse = dummy.get_all_products(limit=10)
    assert 200 == reponse.status_code, " Unexpected status code"
    # checking if limit working if returns 10 products
    assert 10 == len(reponse.json()['products']), "Unexpected response size"
    # wanted to check titles for each product
    # items = reponse.json()['products']
    # for i in range(len(items)):
    #     current =  items[i]
    #     actual = current['title'], current['price']
    #     print(actual)


def test_test_products_skip10_limit10_selecting_title_and_price():
    dummy = RequestDummyJSon()
    response = dummy.get_all_products(limit=10, skip=10, select="title,price")
    assert 200 == response.status_code, "Unexpected status code"
    assert 10 == len(response.json()['products'])


def test_single_product():
    dummyjson = RequestDummyJSon()
    reponse = dummyjson.get_a_single_product(id_prod=3, select="title")
    assert 200 == reponse.status_code, "Unexpected status code"
    print(reponse.json())


def test_search_product():
    dummy = RequestDummyJSon()
    response = dummy.search_products('phone')
    assert 200 == response.status_code, "Unexpected status code"
    assert 4 == len(response.json()['products'])
    assert 'phone' in response.text, "Error, not found"


def test_add_product():
    dummy = RequestDummyJSon()
    response = dummy.add_product("Test")
    assert 200 == response.status_code, "Unexpected status code"
    assert "Test" in response.json()['title'], "Error, not same title"
    print(response.text)


def test_update_product():
    dummy = RequestDummyJSon()
    response_add = dummy.add_product("Test")
    assert 200 == response_add.status_code, "Unexpected status code"
    print(response_add.text)
    print(response_add.json()['id'])

    response_update = dummy.update_product(1, 'Ducks')
    assert 200 == response_update.status_code, "Unexpected status code!"
    assert "Ducks" in response_update.json()["title"], "Error, not same title"
    print(response_update.text)


def test_delete_products():
    dummy = RequestDummyJSon()
    reponse = dummy.delete_product(3)
    assert 200 == reponse.status_code, "unexpected status code"
    print(reponse.json())
