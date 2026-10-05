import pytest
import requests
from common.read_yaml import read_yaml

# 读取环境配置yaml
env_data = read_yaml("data/env.yaml")
base_url = env_data["test_env"]["base_url"]

@pytest.fixture(scope="session")
def base_url_fixture():
    """全局fixture，提供基础url，整个测试会话只执行一次"""
    return base_url返回base_url

@pytest.fixture(scope="session")
def session_fixture():
    """全局requests会话，复用连接，所有用例共用"""
    session = requests.Session()
    yield session
    # 测试全部执行完成后关闭session
    session.close()
