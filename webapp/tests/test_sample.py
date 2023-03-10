from django.test import SimpleTestCase


class UserHoldingTestCase(SimpleTestCase):
    databases = {'default'}

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()

    def test_addition(self):
        x = 5
        y = 7
        result = x + y
        self.assertEqual(result, 12)
        print('Test successful')
