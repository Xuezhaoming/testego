from Api.api import ApiFactory

# 调用轮播图api
# print("轮播图：{}".format(ApiFactory.get_home_api().banner_api().json()))

# 调用主题
# print("主题：{}".format(ApiFactory.get_home_api().theme_api().json()))
# 调用最新商品
# print("调用最新商品:{}".format(ApiFactory.get_home_api().recent_api().json()))

# 调用商品分类
# print("分类:{}".format(ApiFactory.get_product_api().product_classify_api().json()))
# 调用分类下的商品
# print("分类下商品:{}".format(ApiFactory.get_product_api().classify_product_api().json()))
# 调用商品信息
# print("商品信息:{}".format(ApiFactory.get_product_api().product_detail_api().json()))

# 调用获取token方法
# print("返回值：{}".format(ApiFactory.get_user_api().get_token_api().json()))

print("订单列表:{}".format(ApiFactory.get_order_api().order_list_api().json()))
# print("创建订单:{}".format(ApiFactory.get_order_api().create_order_api(12, 7).json()))
# print("查看订单：{}".format(ApiFactory.get_order_api().query_order_api(114).json()))
