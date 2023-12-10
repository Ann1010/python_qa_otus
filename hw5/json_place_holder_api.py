from api_testing.base_request import BaseRequest, BASE_URL_JSON_PLACE_HOLDER


class JsonPlaceHolder(BaseRequest):
    def __init__(self):
        super().__init__(BASE_URL_JSON_PLACE_HOLDER)

    def get_posts(self):
        return self.get('posts')

    def get_posts_by_id(self, id):
        return self.get(f'posts/{id}')

    def get_todos_by_id(self, id):
        return self.get(f'todos/{id}')

    def get_users_by_id(self, id):
        return self.get(f'users/{id}')

    def get_comments_by_id(self, id):
        return self.get_with_param('comments', f'postId={id}')

