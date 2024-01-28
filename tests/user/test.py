import unittest

from src.domain.errors.auth import WrongEmailFormat, WrongPasswordFormat
from src.schemas.auth import SignIn, SignUp


class TestUser(unittest.IsolatedAsyncioTestCase):
    async def test_signIn_schema_email_format(self):
        with self.assertRaises(
            WrongEmailFormat, msg="Should raise EMAIL validation error"
        ):
            SignIn(email="faker-domain.com", password="12345ABCdef!")

    async def test_signIn_schema_password_format(self):
        with self.assertRaises(
            WrongPasswordFormat, msg="Should raise PASSWORD validation error"
        ):
            SignIn(email="faker@gmail.com.br", password="fakepassword")

    async def test_signIn_schema_ok(self):
        body = SignIn(email="faker@gmail.com.br", password="123AbcD!")
        self.assertIsInstance(body, SignIn, "Should be OK creating SignIn model")


class TestSignUp(unittest.IsolatedAsyncioTestCase):
    async def test_signIn_schema_email_format(self):
        with self.assertRaises(
            WrongEmailFormat, msg="Should raise EMAIL validation error"
        ):
            SignUp(
                email="faker-domain.com",
                password="12345ABCdef!",
                name="unit",
                lastname="test",
            )

    async def test_signIn_schema_password_format(self):
        with self.assertRaises(
            WrongPasswordFormat, msg="Should raise PASSWORD validation error"
        ):
            SignUp(
                email="faker@gmail.com",
                password="fakepassword",
                name="unit",
                lastname="test",
            )

    async def test_signIn_schema_ok(self):
        body = SignUp(
            email="faker@gmail.com",
            password="12345ABCdef!",
            name="unit",
            lastname="test",
        )
        self.assertIsInstance(body, SignUp, "Should be OK creating SignUp model")
