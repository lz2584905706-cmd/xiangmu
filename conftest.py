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
    login_url = "/api/login"
    login_payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    resp = temp_client.api_post(login_url, json=login_payload)
    print("登录状态码", resp.status_code)
    print("登录返回文本", repr(resp.text))  # repr可以看清是不是空字符串
    json_data = resp.json()
    store["token"] = json_data["token"]
    print(f"\n=====登录成功，获取token=====\n{store['token']}")