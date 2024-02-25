import pytest

from open_brewery_db_api import OpenBreweryDBApi
from test_data.read_write_files.read_json import read_json

LIST_ALL_FILE = './test_data/open_brewery_db_list_breweries.json'


@pytest.fixture(scope='function')
def open_brewery_api():
    return OpenBreweryDBApi()


@pytest.mark.parametrize('test_data', [read_json(LIST_ALL_FILE)])
def test_get_list_breweries(open_brewery_api, test_data):
    response = open_brewery_api.get_list_breweries(3)
    expected_body = test_data
    for i in range(len(expected_body)):
        for key, value in expected_body[i].items():
            assert response[i][key] == value, (
                f'[{key}] Actual value: {response[i][key]}, expected: {value}'
            )


@pytest.mark.parametrize('city', ['san_diego', 'oklahoma', 'texas'])
def test_get_list_breweries_by_city(open_brewery_api, city):
    response = open_brewery_api.get_list_breweries_by_city(city=city, per_page=3)
    for brew in response:
        assert city.replace("_", " ") in brew['city'].lower(), \
            f"Actual value: {brew['city'].lower()}, expected: {city.replace('_', ' ')}"


@pytest.mark.parametrize('state', ['new_york', 'california', 'wisconsin'])
def test_get_list_breweries_by_state(open_brewery_api, state):
    response = open_brewery_api.get_list_breweries_by_state(state=state, per_page=3)
    for brew in response:
        assert state.replace("_", " ") in brew['state'].lower(), \
            f"Actual value: {brew['state'].lower()}, expected: {state.replace('_', ' ')}"


@pytest.mark.parametrize('type', ['micro', 'nano', 'regional', 'brewpub', 'planning',
                                  'bar', 'contract', 'proprietor', 'closed'])
def test_get_list_breweries_by_type(open_brewery_api, type):
    response = open_brewery_api.get_list_breweries_by_type(type=type, per_page=3)
    for brew in response:
        assert type.replace("_", " ") in brew['brewery_type'].lower(), \
            f"Actual value: {brew['brewery_type'].lower()}, expected: {type.replace('_', ' ')}"


@pytest.mark.parametrize('per_page', [0, 1, 79, 200, 201])
def test_get_list_breweries_per_page(open_brewery_api, per_page):
    response = open_brewery_api.get_list_breweries(per_page=per_page)
    if per_page < 0:
        assert len(response) == 50, \
            f"Actual value: {len(response)}, expected: 50"
    elif per_page > 200:
        assert len(response) == 200, \
            f"Actual value: {len(response)}, expected: 200"
    else:
        assert len(response) == per_page, \
            f"Actual value: {len(response)}, expected: {per_page}"
