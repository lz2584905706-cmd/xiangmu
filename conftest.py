import os
os.environ["PYTEST_UTF8_IDS"] = "1"
import pytest
from common.api_client import ApiClient

@pytest.fixture(scope='session')
def store():
    return {
        "token": None,
        "user_id": None
    }

@pytest.fixture(scope='session')
def api_client(store):
    yield ApiClient(store)


@pytest.fixture(scope='session', autouse=True)
def login_once(store):
    temp_client = ApiClient(store)
    login_url = "/login"
    login_payload = {
        "username": "admin",
        "password": "123456"
    }
    resp = temp_client.api_post(login_url, json=login_payload)
    json_data = resp.json()
    store["token"] = json_data["data"]["token"]
    print(f"\n=====登录成功，获取token=====\n{store['token']}")