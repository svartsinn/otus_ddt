import requests
import pytest

base_url = "https://jsonplaceholder.typicode.com"


@pytest.mark.parametrize(['controller', 'count'], [('/posts', 100), ('/comments', 500),
                                                   ('/albums', 100), ('/photos', 5000),
                                                   ('/todos', 200), ('/users', 10)])
def test_items_count_in_controllers(controller, count):
    response = requests.get(base_url + controller)
    assert len(response.json()) == count


@pytest.mark.parametrize('route', ['/posts/1', '/posts/1/comments', '/comments?postId=1'])
def test_200_status_code_for_routes(route):
    response = requests.get(base_url + route)
    assert response.status_code == 200


def test_id_for_post():
    response = requests.get(base_url + '/posts/1')
    assert response.json()['id'] == 1


def test_201_status_code_for_create_post():
    payload = {'title': 'foo', 'body': 'bar', 'userId': 1000}
    response = requests.post(base_url + '/posts', data=payload)
    assert response.status_code == 201


def test_200_status_code_for_update_post():
    payload = {'title': 'update_foo', 'body': 'update_bar', 'userId': 1000}
    response = requests.put(base_url + '/posts/1', data=payload)
    assert response.status_code == 200


def test_200_status_code_for_delete_post():
    response = requests.put(base_url + '/posts/1')
    assert response.status_code == 200
