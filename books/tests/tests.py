from django.test import TestCase


# Create your tests here.

class DemoTest(TestCase):
    def test_equl(self):
        return self.assertEqual(1 + 1, 2)
