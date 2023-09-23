import unittest
import os

from dotenv import load_dotenv
from jose import JWTError, jwt

load_dotenv()

def encode_token(payload):
    return jwt.encode(
        payload=payload,
        key=os.getenv("PWD_SECRET"),  # The private key created in the previous step
        algorithm="HS256",
    )


def get_mock_user_claims(permissions):
    return {
        "sub": "123|auth0",
        "iss": "some-issuer",  # Should match the issuer your app expects
        "aud": "audience",  # Should match the audience your app expects
        "iat": 0,  # Issued a long time ago: 1/1/1970
        "exp": 9999999999,  # One long-lasting token, expiring 11/20/2286
        "permissions": permissions,
    }

class TestUserEndpoint(unittest.TestCase):

    def setUp(self):
        pass

    def test_x(self):
        # encode_token(get_mock_user_claims(permissions))
        # self.assertEqual(function(a,b), expected)
        pass

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()