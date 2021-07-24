import requests
import pytest

base_url = 'https://dog.ceo/api'


@pytest.mark.parametrize('breed', ['newfoundland', 'pyrenees', 'papillon'])
def test_breed_exist_in_breed_list(breed):
    response = requests.get(base_url + '/breeds/list/all')
    assert breed in response.json()['message']


@pytest.mark.parametrize('breed', ['komondor', 'cairn', 'ridgeback'])
def test_200_status_code_browse_breed_list(breed):
    response = requests.get(base_url + f'/breed/{breed}/images/random')
    assert response.status_code == 200


@pytest.mark.parametrize('breed',
                         ['afghan', 'basset', 'blood', 'english', 'ibizan', 'plott', 'walker'])
def test_200_status_code_sub_breed_list(breed):
    response = requests.get(base_url + '/breed/hound/list')
    assert breed in response.json()['message']


def test_200_status_code_breeds_list():
    response = requests.get(base_url + '/breeds/list/all')
    assert response.status_code == 200


def test_200_status_code_random_image():
    response = requests.get(base_url + '/breeds/image/random')
    assert response.status_code == 200


def test_image_file_in_random_image():
    response = requests.get(base_url + '/breeds/image/random')
    assert ('jpg' or 'png' or 'jpeg') in response.json()['message']


def test_200_status_code_by_breed():
    response = requests.get(base_url + '/breed/hound/images')
    assert response.status_code == 200


def test_list_of_message_not_empty_by_breed():
    response = requests.get(base_url + '/breed/hound/images')
    assert len(response.json()['message']) > 1
