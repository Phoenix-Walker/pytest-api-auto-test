# pytest-api-auto-test
基于Python + pytest + requests 实现接口自动化测试项目，YAML管理测试数据，Allure生成可视化测试报告。
> 被测接口：公开免费API jsonplaceholder.typicode.com，无需部署后端服务。

## 技术栈
- Python3
- pytest：测试框架
- requests：HTTP接口请求
- PyYAML：读取yaml测试数据、环境配置
- Allure-Pytest：生成可视化测试报告

## 项目目录结构
pytest-api-auto-test/
├── api/                 # 接口封装层，封装请求方法与业务接口
│   └── user_api.py
├── common/              # 公共工具模块
│   ├── read_yaml.py     # yaml文件读取工具
│   └── log_util.py      # 日志工具
├── data/                # 测试数据与环境配置（数据代码分离）
│   ├── env.yaml         # 环境基础地址配置
│   └── test_data.yaml   # 用例测试数据
├── testcases/           # pytest测试用例
│   └── test_user.py
├── reports/             # allure测试报告输出目录
│   └── .gitkeep
├── conftest.py          # pytest全局fixture，全局会话配置
├── requirements.txt     # 项目依赖包清单
└── README.md

## 测试覆盖场景
1. 获取用户接口
    - 正向场景：查询存在用户，校验状态码+返回内容
    - 异常场景：查询不存在ID，校验404返回码
2. 创建帖子接口
    - 正向场景：传入完整参数新建帖子
    - 异常场景：缺失部分请求参数，验证接口容错

## 运行步骤
1. 克隆仓库
```bash
git clone https://github.com/phoenix-walker/pytest-api-auto-test.git
cd pytest-api-auto-test

pip install -r requirements.txt

pytest testcases/ --alluredir=reports/allure-results
allure generate reports/allure-results -o reports/allure-report --clean
allure open reports/allure-report

## 项目亮点
1. 数据与代码分离：测试参数、环境地址统一存放在YAML文件，修改用例无需改动业务代码
2. 使用pytest fixture全局复用requests session，减少连接开销
3. 用 @pytest.mark.parametrize 实现用例参数化，一套代码执行多组测试场景
4. Allure可视化报告，清晰展示用例执行结果，方便回归测试
5. 分层架构：公共工具层 → 接口封装层 → 测试用例层，符合自动化项目工程化规范
