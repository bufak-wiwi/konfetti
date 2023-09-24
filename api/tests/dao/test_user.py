import unittest

from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

from api.db.base import Base
from api.db.models.user import User


url = URL.create(
    drivername="mariadb",
    username="konfetti",
    host="/tmp/mariadb/socket",
    database="konfetti"
    )

engine = create_engine(url)
Session = sessionmaker(bind=engine)

class TestUserDao(unittest.TestCase):

    def setUp(self):
        Base.metadata.create_all(engine)
        session = Session()
        yield session
        session.rollback()
        session.close()
        valid_data = User(
        email="test@test.de"
    )

    def test_x(self):
        # encode_token(get_mock_user_claims(permissions))
        # self.assertEqual(function(a,b), expected)
        pass

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
