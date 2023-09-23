import pytest

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

@pytest.fixture(scope="module")
def db_session():
    Base.metadata.create_all(engine)
    session = Session()
    yield session
    session.rollback()
    session.close()

@pytest.fixture(scope="module")
def valid_data():
    valid_data = User(
        email="test@test.de"
    )
    return valid_data

class TestUserDao:

    def test_x(self):
        # self.session.add(self.valid_data)
        # self.session.commit()
        # returnvalue = function(db=db_session)
        # assert returnvalue.id == expected.id
        pass

    # @pytest.mark.xfail(raises=IntegrityError)
    def test_y(self, db_session):
        # invalid_data = User(
        #     email=1
        # )
        # db_session.add(invalid_data)
        # try:
        #     db_session.commit()
        # except IntegrityError:
        #     db_session.rollback()
        pass
