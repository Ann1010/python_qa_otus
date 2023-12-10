from api_testing.base_request import BaseRequest, BASE_URL_OPEN_BREWERY_DB


class OpenBreweryDBApi(BaseRequest):
    def __init__(self):
        super().__init__(BASE_URL_OPEN_BREWERY_DB)

    def get_list_breweries(self, per_page):
        return self.get_with_param('breweries', f'per_page={per_page}')

    def get_list_breweries_by_city(self, per_page, city):
        return self.get_with_param('breweries', f'by_city={city}&per_page={per_page}')

    def get_list_breweries_by_state(self, per_page, state):
        return self.get_with_param('breweries', f'by_state={state}&per_page={per_page}')

    def get_list_breweries_by_type(self, per_page, type):
        return self.get_with_param('breweries', f'by_type={type}&per_page={per_page}')
