
import os
os.environ["PYTEST_UTF8_IDS"] = "1"
from common.assert_util import AssertUtil
import pytest
from common.allure_util import set_allure_info
from common.yaml_util import read_yaml
from common.yaml_util import get_test_cases

yaml_path=os.path.join(os.path.dirname(os.path.dirname(__file__)), "data","get_data.yaml")
yaml_data=read_yaml(yaml_path)

get_list_data, get_list_ids = get_test_cases(yaml_data, "get_list_data")
get_users_data, get_users_ids = get_test_cases(yaml_data, "get_users_data")
post_users_data, post_users_ids = get_test_cases(yaml_data, "post_users_data")
put_users_data, put_users_ids = get_test_cases(yaml_data, "put_users_data")
delete_users_data, delete_users_ids = get_test_cases(yaml_data, "delete_users_data")

@pytest.mark.regression
@pytest.mark.smoke
@pytest.mark.parametrize("case", get_list_data,ids=get_list_ids)
def test_get_list(api_client,case):
    set_allure_info(case)
    resp=api_client.api_get(case.get("path"),params=case.get("params"))
    AssertUtil.assert_status_code(resp, case.get("expect_code"))
    AssertUtil.assert_json_value(resp,"total", case.get("expect_total"))

@pytest.mark.regression
@pytest.mark.smoke
@pytest.mark.parametrize("case",get_users_data,ids=get_users_ids)
def test_get_users(api_client,case):
    set_allure_info(case)
    path=case.get("path").format(id=case.get("id"))
    resp=api_client.api_get(path)
    AssertUtil.assert_status_code(resp, case.get("expect_code"))

@pytest.mark.regression
@pytest.mark.smoke
@pytest.mark.parametrize("case",post_users_data,ids=post_users_ids)
def test_post_users(api_client,case):
    set_allure_info(case)
    resp=api_client.api_post(case.get("path"),json=case.get("data"))
    AssertUtil.assert_status_code(resp, case.get("expect_code"))
    AssertUtil.assert_json_value(resp,"data.name", case.get("expect_name"))
    AssertUtil.assert_json_value(resp, "job", case.get("expect_job"))

@pytest.mark.regression
@pytest.mark.parametrize("case",put_users_data,ids=put_users_ids)
def test_put_users(api_client,case):
    set_allure_info(case)
    path=case.get("path").format(id=case.get("id"))
    resp=api_client.api_put(path,json=case.get("data"))
    AssertUtil.assert_status_code(resp, case.get("expect_code"))
    AssertUtil.assert_json_value(resp, "name", case.get("expect_name"))
    AssertUtil.assert_json_value(resp, "job", case.get("expect_job"))

@pytest.mark.regression
@pytest.mark.smoke
@pytest.mark.parametrize("case",delete_users_data,ids=delete_users_ids)
def test_delete_users(api_client,case):
    set_allure_info(case)
    path = case.get("path").format(id=case.get("id"))
    resp = api_client.api_delete(path)
    AssertUtil.assert_status_code(resp, case.get("expect_code"))


