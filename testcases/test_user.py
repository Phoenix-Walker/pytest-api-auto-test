import allure
import pytest
from api.user_api import UserApi
from common.read_yaml import read_yaml

# 读取测试数据
test_data = read_yaml("data/test_data.yaml")
get_user_cases = test_data["get_user_data"]
create_post_cases = test_data["create_post_data"]

@allure.feature("用户模块接口")
@allure.story("获取单个用户接口")
@pytest.mark.parametrize("case", get_user_cases)
def test_get_user(session_fixture, base_url_fixture, case):
    user_api = UserApi(session_fixture, base_url_fixture)
    resp = user_api.get_user(case["user_id"])
    # 断言响应状态码
    assert resp.status_code == case["expect_status"]
    # 正向用例额外校验返回名字
    if resp.status_code == 200:
        assert resp.json()["name"] == case["expect_name"]

@allure.feature("帖子模块接口")
@allure.story("新建帖子接口")
@pytest.mark.parametrize("case", create_post_cases)
def test_create_post(session_fixture, base_url_fixture, case):
    user_api = UserApi(session_fixture, base_url_fixture)
    resp = user_api.create_post(case["payload"])
    assert resp.status_code == case["expect_status"]
