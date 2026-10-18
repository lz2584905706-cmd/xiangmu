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
    # 容错：只有登录成功(200)且返回里真的有token才保存；
    # 失败/限流时跳过，store["token"]保持None，不让整个会话崩溃
    if resp.status_code == 200:
        json_data = resp.json()
        token = json_data.get("token")
        if token:
            store["token"] = token
            print(f"\n=====登录成功，获取token=====\n{store['token']}")
        else:
            print("登录返回中没有token字段，跳过保存")
    else:
        print(f"登录未成功，状态码{resp.status_code}，跳过token保存（不影响无需鉴权的用例）")