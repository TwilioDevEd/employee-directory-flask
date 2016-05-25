from .base import BaseTest
from flask import session


class RootTest(BaseTest):

    def test_no_results(self):
        response = self.client.post('/directory/search',
                                    data={'Body': 'you_will_not_find_me'})
        self.assertEquals(200, response.status_code)

        root = self.assertXmlDocument(response.data)
        body = root.xpath('./Message/Body/text()')

        self.assertEquals(1, len(body), response.data)
        self.assertEquals("We did not find the employee you're looking for", body[0])

    def test_single_result(self):
        response = self.client.post('/directory/search',
                                    data={'Body': 'Wolverine'})
        self.assertEquals(200, response.status_code)

        root = self.assertXmlDocument(response.data)
        body = root.xpath('./Message/Body/text()')
        media = root.xpath('./Message/Media/text()')

        self.assertEquals(1, len(body), response.data)
        self.assertEquals(1, len(media), response.data)

        expected_body = "Wolverine\n+14155559718\nWolverine@heroes.example.com"
        self.assertEquals(expected_body, body[0])
        expected_media = "http://i.annihil.us/u/prod/marvel/i/mg/2/60/537bcaef0f6cf.jpg"
        self.assertEquals(expected_media, media[0])

    def test_multiple_results_will_list_on_message_body(self):
        response = self.client.post('/directory/search',
                                    data={'Body': 'Thor'})
        self.assertEquals(200, response.status_code)

        root = self.assertXmlDocument(response.data)
        body = root.xpath('./Message/Body/text()')

        self.assertEquals(1, len(body), response.data)

        expected_body = '\n'.join(["We found multiple people, reply with:",
                                   "1 for Thor Girl",
                                   "2 for Frog Thor",
                                   "3 for Thor",
                                   "Or start over"])
        self.assertEquals(expected_body, body[0])

    def test_multiple_results_will_store_names_on_session(self):
        with self.app.test_client() as client:
            client.post('/directory/search',
                        data={'Body': 'Thor'})
            choices = session.get('choices', [])
            self.assertEquals(['Thor Girl', 'Frog Thor', 'Thor'], choices)

    def test_user_can_choose_an_option(self):
        with self.app.test_client() as client:
            with client.session_transaction() as session:
                session['choices'] = ['Thor Girl', 'Frog Thor', 'Thor']
            response = client.post('/directory/search',
                                   data={'Body': '1'})
        self.assertEquals(200, response.status_code)

        root = self.assertXmlDocument(response.data)
        body = root.xpath('./Message/Body/text()')
        media = root.xpath('./Message/Media/text()')

        self.assertEquals(1, len(body), response.data)
        self.assertEquals(1, len(media), response.data)

        expected_body = "Thor Girl\n+14155550820\nThorGirl@heroes.example.com"
        self.assertEquals(expected_body, body[0])
        expected_media = "http://i.annihil.us/u/prod/marvel/i/mg/9/e0/526957cdcf6d1.jpg"
        self.assertEquals(expected_media, media[0])

    def test_invalid_option_will_trigger_a_search(self):
        with self.app.test_client() as client:
            with client.session_transaction() as session:
                session['choices'] = ['Thor Girl', 'Frog Thor', 'Thor']
            response = client.post('/directory/search',
                                   data={'Body': '51'})
        self.assertEquals(200, response.status_code)

        root = self.assertXmlDocument(response.data)
        body = root.xpath('./Message/Body/text()')
        media = root.xpath('./Message/Media/text()')

        self.assertEquals(1, len(body), response.data)
        self.assertEquals(1, len(media), response.data)

        expected_body = "X-51\n+14155550804\nX-51@heroes.example.com"
        self.assertEquals(expected_body, body[0])
        expected_media = "http://i.annihil.us/u/prod/marvel/i/mg/f/d0/4c003727804b4.jpg"
        self.assertEquals(expected_media, media[0])
