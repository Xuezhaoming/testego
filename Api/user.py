"""用户"""
import logging

import requests
import app


class UserApi:
    """用户api接口"""
    def __init__(self):
        # 获取token
        self.token_url = app.base_url + "/token/user"
        # token验证
        self.verify_url = app.base_url + "/token/verify"
        # 获取地址信息
        self.address_url = app.base_url + "/address"

    def get_token_api(self):
        """获取token"""
        # 请求体
        logging.info("用户-获取token")
        data = {"code": app.code}
        logging.info("参数:{}".format(data))
        return requests.post(self.token_url, json=data, headers=app.headers)

    def verify_api(self):
        """token验证"""
        # 请求参数
        logging.info("用户-token验证")
        data = {"token": app.headers.get("token")}
        logging.info("参数:{}".format(data))
        return requests.post(self.verify_url, json=data, headers=app.headers)

    def address_pai(self):
        """获取地址信息"""
        logging.info("用户-获取地址信息")
        return requests.get(self.address_url, headers=app.headers)