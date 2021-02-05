from django.db.models import Max
from django.test import Client, TestCase


# Create your tests here.
class ModelsTestCase(TestCase):

    def test_index(self):
        c = Client()
        response = c.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["flights"].count(), 3)
