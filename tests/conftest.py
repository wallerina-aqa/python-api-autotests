from pathlib import Path

import pytest
from dotenv import load_dotenv
from faker import Faker

from services.characters.get_character_by_id_api import GetCharacterByIdAPI
from services.characters.get_characters_api import GetCharactersAPI
from services.random.get_random_character import GetRandomCharacterAPI
from services.tokens.get_user_auth_token_api import GetUserAuthTokenAPI
from services.users.create_user_api import CreateUserAPI
from services.users.get_me_api import GetMeAPI
from services.users.get_users_api import GetUsersAPI
from services.users.update_user_api import UpdateUserAPI

load_dotenv()

faker = Faker()

PROJECT_ROOT = Path(__file__).resolve().parents[1]


def pytest_configure(config):
    allure_dir = PROJECT_ROOT / "allure-results"
    allure_dir.mkdir(exist_ok=True)
    config.option.allure_report_dir = str(allure_dir)


@pytest.fixture()
def get_character_by_id_api():
    return GetCharacterByIdAPI()

@pytest.fixture()
def get_random_character_api():
    return GetRandomCharacterAPI()

@pytest.fixture()
def get_characters_api():
    return GetCharactersAPI()

@pytest.fixture
def new_user_data():
    return {
        "name": faker.first_name(),
        "surname": faker.last_name(),
        "middleName": faker.first_name(),
        "email": faker.email(),
        "username": faker.user_name(),
        "password": faker.password(),
        "isSubscribed": faker.boolean(),
    }

@pytest.fixture()
def create_user_api():
    return CreateUserAPI()

@pytest.fixture()
def created_user_username_password(create_user_api, new_user_data):
    create_user_api.send_request(new_user_data)
    username = new_user_data.get("username")
    password = new_user_data.get("password")
    return username, password

@pytest.fixture()
def unexisting_user_username_password():
    username = faker.user_name()
    password = faker.password()
    return username, password

@pytest.fixture()
def get_users_api():
    return GetUsersAPI()

@pytest.fixture()
def get_user_auth_token_api():
    return GetUserAuthTokenAPI()

@pytest.fixture()
def access_token(created_user_username_password, get_user_auth_token_api):
    username, password = created_user_username_password
    get_user_auth_token_api.send_request(username, password)
    access_token = get_user_auth_token_api.ACCESS_TOKEN
    return access_token

@pytest.fixture
def user_data_to_update():
    return {
        "name": faker.first_name(),
        "surname": faker.last_name(),
        "middleName": faker.first_name()
    }


@pytest.fixture()
def update_user_api():
    return UpdateUserAPI()

@pytest.fixture()
def get_me_api():
    return GetMeAPI()
