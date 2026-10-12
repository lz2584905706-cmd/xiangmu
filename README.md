```
# 接口自动化测试项目(Pytest+Allure+YAML)
## 项目简介
基于Python+pytest实现的接口自动化测试框架，用于完成HTTP接口的自动化回归测试。
- 使用YAML管理测试用例，用例与代码分离，方便维护用例
- 封装通用HTTP请求客户端，自动携带token鉴权
- 使用pytest‑fixture实现跨用例数据共享，支持新增‑查询‑修改‑删除完整业务流程串联
- Allure生成可视化测试报告
- git版本管理，忽略日志、报告、虚拟环境等无关文件

### 技术栈
Python3、Pytest、Allure‑pytest、PyYAML、requests

## 项目目录说明
```

├── common              # 公共工具模块
│   ├── api_client.py   # http 请求封装，自动处理 token
│   ├── logger.py       # 日志封装
│   ├── assert_util.py  # 通用断言工具
│   └── allure_util.py  # allure 报告工具
├── config              # 配置文件
├── data                # yaml 测试用例数据
├── test_cases         # pytest 测试用例
├── logs               # 运行日志（git 忽略不上传）
├── reports            # allure 报告（git 忽略不上传）
├── conftest.py        # pytest 全局钩子、fixture
├── pytest.ini         # pytest 配置
└── .gitignore         # git 忽略配置

```

## 运行方式
1. 安装依赖
```bash
pip install -r requirements.txt
```

2. 执行用例

```
pytest
```

3. 生成 allure 报告

```
pytest --allure‑report=reports/allure‑results
allure generate reports/allure‑results -o reports/html‑report --clean
allure open reports/html‑report
```