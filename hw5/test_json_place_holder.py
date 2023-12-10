import pytest

from json_place_holder_api import JsonPlaceHolder
from test_data.read_write_files.read_json import read_json

POST_FILE = './test_data/json_place_holder.json'
LIST_ALL_SUB_BREEDS_FILE = './test_data/dog_ceo_list_all_sub_breeds.json'


@pytest.fixture(scope='function')
def json_place_holder():
    return JsonPlaceHolder()


def test_get_posts(json_place_holder):
    response = json_place_holder.get_posts()
    assert len(response) == 100


@pytest.mark.parametrize('test_data', [read_json(POST_FILE)])
def test_get_post_id(json_place_holder, test_data):
    response = json_place_holder.get_posts_by_id(49)
    expected_body = test_data
    for key, value in expected_body.items():
        assert response[key] == value, (
            f'[{key}] Actual value: {response[key]}, expected: {value}'
        )


@pytest.mark.parametrize('id', [5, 32, 89])
def test_get_post_by_id(json_place_holder, id):
    response = json_place_holder.get_posts_by_id(id)
    assert response['id'] == id, \
        f"Actual value: {response['id']}, expected: {id}"


@pytest.mark.parametrize('id', [5, 32, 89])
def test_get_todos_by_id(json_place_holder, id):
    response = json_place_holder.get_todos_by_id(id)
    assert response['id'] == id, \
        f"Actual value: {response['id']}, expected: {id}"


@pytest.mark.parametrize('id', [5, 3, 1])
def test_get_users_by_id(json_place_holder, id):
    response = json_place_holder.get_users_by_id(id)
    assert response['id'] == id, \
        f"Actual value: {response['id']}, expected: {id}"


@pytest.mark.parametrize('id', [5, 3, 1])
def test_get_comments_by_id(json_place_holder, id):
    response = json_place_holder.get_comments_by_id(id)
    for comment in response:
        assert comment['postId'] == id, \
            f"Actual value: {comment['postId']}, expected: {id}"
