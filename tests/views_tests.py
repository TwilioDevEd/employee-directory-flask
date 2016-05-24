from .base import BaseTest


class RootTest(BaseTest):

    def test_root(self):
        response = self.client.get('/')
        self.assertEquals(200, response.status_code)
        self.assertIn('Employee Directory', response.data.decode('utf8'))
