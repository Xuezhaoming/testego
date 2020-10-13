from Api.api import ApiFactory
import logging


class TestHomeApi:

    def test_home_api(self):
        """轮播图"""
        # 请求返回参数
        res = ApiFactory.get_home_api().banner_api()
        # 打印请求地址，请求参数响应数据
        logging.info("请求地址:{}".format(res.url))
        logging.info("响应数据:{}".format(res.json()))
        # 断言状态码
        assert res.status_code == 200
        # 断言id 和 name
        assert res.json().get("id") == 1 and res.json().get("name") == "首页置顶"
        # 断言items列表长度大于0
        assert len(res.json().get("items")) > 0

    def test_theme_api(self):
        """专题栏"""
        # 请求返回对象
        res = ApiFactory.get_home_api().theme_api()
        # 打印请求地址，请求参数响应数据
        logging.info("请求地址:{}".format(res.url))
        logging.info("响应数据:{}".format(res.json()))
        # 断言 -状态码
        assert res.status_code == 200
        # 断言三个id= 1 2 3
        assert 'id":1' in res.text and 'id":2' in res.text and 'id":3' in res.text
        # 断言关键字段 name description topic_img head_img
        assert False not in [i in res.text for i in ["name", "description", "topic_img", "head_img"]]

    def test_recent_api(self):
        # 请求返回对象
        res = ApiFactory.get_home_api().recent_api()
        # 打印请求地址，请求参数响应数据
        logging.info("请求地址:{}".format(res.url))
        logging.info("响应数据:{}".format(res.json()))
        # 断言 -状态码
        assert res.status_code == 200
        # 断言新品数量大于0
        assert len(res.json()) > 0
        # 断言关键字
        assert "id" in res.text and "name" in res.text and "price" in res.text