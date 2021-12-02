
from django.test import TestCase

from accounts.models import User
# Create your tests here.


class TestTest(TestCase):
    def setUp(self):
        self.TestUser = {
            "email": "test@test.com",
            "username": "test_user",
            "password": "www385jo",
        }

        User.objects.create_user(
            self.TestUser["email"],
            self.TestUser["username"],
            self.TestUser["password"]
        )

    def test_get_login(self):
        client = self.client

        res = client.post("/api/user/login/", {
            "email": self.TestUser["email"],
            "password": self.TestUser["password"]
        })

        import ast
        text_data = res.content.decode("utf-8")
        access_data = ast.literal_eval(text_data)["access"]
        print(access_data)
        # self.access = res.content["access"]
        self.assertEqual(res.status_code, 200)


# DBno
