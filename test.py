from django.test import TestCase # Import the view you want to test
from opai.views import testGPTView

class YourTestCase(TestCase):
    def test_post_request(self):        
        # Simulate a POST request
        response = self.client.post('/opai/testgpt/')
        
        print (response.content)
