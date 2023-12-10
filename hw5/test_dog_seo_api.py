import pytest

from dog_ceo_api import DogCeoApi
from test_data.read_write_files.read_json import read_json

LIST_ALL_FILE = './test_data/dog_ceo_list_all.json'
LIST_ALL_SUB_BREEDS_FILE = './test_data/dog_ceo_list_all_sub_breeds.json'


@pytest.fixture(scope='function')
def dog_ceo_api():
    return DogCeoApi()


@pytest.mark.parametrize('test_data', [read_json(LIST_ALL_FILE)])
def test_get_list_all(dog_ceo_api, test_data):
    response = dog_ceo_api.get_list_all()
    expected_body = test_data
    for key, value in expected_body.items():
        assert response[key] == value, (
            f'[{key}] Actual value: {response[key]}, expected: {value}'
        )


@pytest.mark.parametrize('count', [5, 1, 10])
def test_get_multiple_images(dog_ceo_api, count):
    response = dog_ceo_api.get_multiple_images(count)
    images_list = response["message"]
    assert count == len(images_list)


@pytest.mark.parametrize('test_data', [read_json(LIST_ALL_SUB_BREEDS_FILE)])
def test_get_list_all_sub_breeds(dog_ceo_api, test_data):
    response = dog_ceo_api.get_list_all_sub_breeds()
    expected_body = test_data
    for key, value in expected_body.items():
        assert response[key] == value, (
            f'[{key}] Actual value: {response[key]}, expected: {value}'
        )


@pytest.mark.parametrize(('sub_breed'), ['afghan', 'basset', 'ibizan'])
def test_get_single_random_images_from_sub_breed(dog_ceo_api, sub_breed):
    response = dog_ceo_api.get_single_random_images_from_sub_breed(sub_breed)
    images = response["message"]
    assert sub_breed in images


@pytest.mark.parametrize(('sub_breed', 'count'), [('afghan', 5), ('basset', 4), ('ibizan', 8)])
def test_get_multiple_random_images_from_sub_breed(dog_ceo_api, sub_breed, count):
    response = dog_ceo_api.get_multiple_random_images_from_sub_breed(sub_breed, count)
    images = response["message"]
    for image in images:
        assert sub_breed in image
    assert count == len(images)
