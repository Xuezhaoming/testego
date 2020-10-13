import logging

import app
import pytest
from Api.api import ApiFactory


@pytest.mark.run(order=0)
class TestUserApi:
    def test_get_token(self):
        """获取token"""
        # 请求返回对象
        res = ApiFactory.get_user_api().get_token_api()
        logging.info("请求地址:{}".format(res.url))
        logging.info("响应数据:{}".format(res.json()))
        # 断言 -状态码
        assert res.status_code == 200
        # 断言token存在
        assert len(res.json().get("token")) > 0
        # 保存token
        app.headers["token"] = res.json().get("token")
        print("app.headers:{}".format(app.headers))

    def test_verify_token(self):
        """验证token"""
        # 请求返回对象
        res = ApiFactory.get_user_api().verify_api()
        logging.info("请求地址:{}".format(res.url))
        logging.info("响应数据:{}".format(res.json()))
        # 断言 -状态码
        assert res.status_code == 200
        # 断言有效
        assert res.json().get("isValid") is True

    def test_address_pai(self):
        """用户地址信息"""
        # 请求返回对象
        res = ApiFactory.get_user_api().address_pai()
        logging.info("请求地址:{}".format(res.url))
        logging.info("响应数据:{}".format(res.json()))
        # 断言 -状态码
        assert res.status_code == 200
        # 断言信息
        assert False not in [i in res.text for i in ["小明", "18888888888", "上海市", "浦东新区"]]
