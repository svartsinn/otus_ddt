import requests
import pytest

base_url = "https://api.openbrewerydb.org/breweries"


@pytest.mark.parametrize('city', ['jackson', 'chamblee', 'philadelphia'])
def test_records_exist_in_breweries_by_city(city):
    response = requests.get(base_url + f"?by_city={city}")
    assert len(response.json()) > 1


@pytest.mark.parametrize('page', [10, 25, 50])
def test_records_in_breweries_per_page(page):
    response = requests.get(base_url + f"?per_page={page}")
    assert len(response.json()) == page


def test_200_status_code_breweries():
    response = requests.get(base_url)
    assert response.status_code == 200


def test_200_status_code_search_breweries():
    query = 'dog'
    response = requests.get(base_url + f"/search?query={query}")
    assert len(response.json()) > 1


def test_compare_name_with_id_in_get_brewery():
    brewery_id = 14347
    response = requests.get(base_url + f"/{brewery_id}")
    assert response.json()['name'] == 'SKA Brewing'


def test_error_non_existed_id_in_get_brewery():
    brewery_id = 111
    response = requests.get(base_url + f"/{brewery_id}")
    assert response.json()['message'] == f"Couldn\'t find Brewery with \'id\'={brewery_id}"




