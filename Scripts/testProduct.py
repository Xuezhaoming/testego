import logging

from Api.api import ApiFactory


class TestProductApi:

    def test_product_classify_api(self):
        """商品分类"""
        # 请求返回参数
        res = ApiFactory.get_product_api().product_classify_api()
        logging.info("请求地址:{}".format(res.url))
        logging.info("响应数据:{}".format(res.json()))
        # 断言状态码
        assert res.status_code == 200
        # 断言关键字
        assert "id" in res.text and "name" in res.text and "topic_img_id" in res.text
        # 断言列表长度大于0
        assert len(res.json()) > 0

    def test_classify_product_api(self):
        """分类下商品"""
        # 请求返回参数
        res = ApiFactory.get_product_api().classify_product_api()
        logging.info("请求地址:{}".format(res.url))
        logging.info("响应数据:{}".format(res.json()))
        # 断言状态码
        assert res.status_code == 200
        # 断言列表长度大于0
        assert len(res.json()) > 0
        # 断言关键字段
        assert False not in [i in res.text for i in ["id", "name", "price", "stock"]]

    def test_product_detail_api(self):
        """商品信息"""
        # 请求返回参数
        res = ApiFactory.get_product_api().product_detail_api()
        logging.info("请求地址:{}".format(res.url))
        logging.info("响应数据:{}".format(res.json()))
        # 断言状态码
        assert res.status_code == 200
        # 断言id
        assert res.json().get("id") == 2
        # 断言name
        assert res.json().get("name") == "梨花带雨 3个"
        # 断言price
        assert res.json().get("price") == "0.01"
