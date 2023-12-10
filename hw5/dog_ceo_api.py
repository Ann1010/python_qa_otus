from api_testing.base_request import BaseRequest, BASE_URL_DOGCEO


class DogCeoApi(BaseRequest):
    def __init__(self):
        super().__init__(BASE_URL_DOGCEO)

    def get_list_all(self):
        return self.get('breeds/list/all',)

    def get_multiple_images(self, count):
        return self.get(f'breed/hound/images/random/{count}')

    def get_list_all_sub_breeds(self):
        return self.get('breed/hound/list')

    def get_single_random_images_from_sub_breed(self, sub_breed):
        return self.get(f'breed/hound/{sub_breed}/images/random')

    def get_multiple_random_images_from_sub_breed(self, sub_breed, count):
        return self.get(f'breed/hound/{sub_breed}/images/random/{count}')