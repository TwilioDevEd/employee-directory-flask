from .base import BaseTest


class RootTest(BaseTest):

    def test_root(self):
        response = self.client.get('/')
        self.assertEquals(200, response.status_code)
        self.assertIn('Employee Directory', response.data.decode('utf8'))

    def test_no_results(self):
        response = self.client.post('/directory/search',
                                    {'Body': 'you_will_not_find_me'})
        self.assertEquals(200, response.status_code)

        root = self.assertXmlDocument(response.data)
        content = root.xpath('./Message/Body/text()')

        self.assertEquals(1, len(content), response.data)
        self.assertEquals("We did not find the employee you're looking for", content[0])
