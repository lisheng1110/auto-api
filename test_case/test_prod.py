from tools.api import request_tool
from tools.security.md5_tool import md5_passwd

'''
自动生成 数字 20,80   #生成20到80之间的数字 例：56
自动生成 字符串 5 中文数字字母特殊字符 xuepl        #生成以xuepl开头加上长度2到5位包含中文数字字母特殊字符的字符串，例子：xuepl我1
自动生成 地址
自动生成 姓名
自动生成 手机号
自动生成 邮箱
自动生成 身份证号
'''

def test_post_add_prod(pub_data):  # 新增产品

    method = "POST"  # 请求方法，全部大写
    feature = "商品模块"  # allure报告中一级分类
    story = '商品信息'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/addProd"  # 接口地址
    headers = {"token": pub_data["token"]}
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''{
  "brand": "荣耀",
  "colors": [
    "金桔黄","中国红","炫蓝","酷黑"
  ],
  "price": 10000,
  "productCode": "自动生成 字符串 5 数字字母",
  "productName": "huawei",
  "sizes": [
    "6寸"
  ],
  "type": "手机"
}'''
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    json_path = [{"skuCode": '$.data[0].skuCode'}]  # 等效于pub_data["skuCode"]=r.json()["data"][0]["skuCode"]
    r = request_tool.request(json_path=json_path, headers=headers, method=method, url=uri, pub_data=pub_data,
                             json_data=json_data, status_code=status_code, expect=expect, feature=feature, story=story,
                             title=title)
    # pub_data["skuCode"]=r.json()["data"][0]["skuCode"]#r是返回的字符串数据，通过json（）把r转成字典格式，先通过字典关键字取“data”数据内容，然后通过下标取data（这里是个列表）中下标为0的字典，再通过字典中的key取值


def test_post_change_price(pub_data):  # 修改产品价格
    method = "POST"  # 请求方法，全部大写
    feature = "产品模块"  # allure报告中一级分类
    story = '修改价格'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/changePrice"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    data = {"SKU": pub_data["skuCode"], "price": 10000}
    headers = {"token": pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method, url=uri, pub_data=pub_data, data=data, status_code=status_code, expect=expect,
                         feature=feature, story=story, title=title, headers=headers)


def test_post_sold_out(pub_data):  # 产品下架
    method = "POST"  # 请求方法，全部大写
    feature = "产品模块"  # allure报告中一级分类
    story = '商品下架'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/soldOut"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    data = {"productCode": "lss210089"}  # 输入精确下架的产品名
    headers = {"token": pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method, url=uri, pub_data=pub_data, data=data, status_code=status_code, expect=expect,
                         feature=feature, story=story, title=title, headers=headers)


def test_post_pi_liang(pub_data):  # 根据产品编码批量修改商品价格
    method = "POST"  # 请求方法，全部大写
    feature = "产品模块"  # allure报告中一级分类
    story = '批量修改商品价格'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/changePriceByProdCode"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    data = {"prodCode": 'mate30', "price": 9999}
    headers = {"token": pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method, url=uri, pub_data=pub_data, data=data, status_code=status_code, expect=expect,
                         feature=feature, story=story, title=title, headers=headers)


def test_post_add_kucun(pub_data):  # 增加商品库存
    method = "POST"  # 请求方法，全部大写
    feature = "商品模块"  # allure报告中一级分类
    story = '增加商品库存'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/incrementSku"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    data = {"skuCode": "mate30_金桔黄_6寸", "qty": 99}  # 增加99个库存
    headers = {"token": pub_data['token']}
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method, url=uri, pub_data=pub_data, data=data, status_code=status_code, expect=expect,
                         feature=feature, story=story, title=title, headers=headers)


def test_get_ku_cun(pub_data):  # 查询单个商品库存
    method = "GET"  # 请求方法，全部大写
    feature = "产品模块"  # allure报告中一级分类
    story = '查询单个库存'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/getSkuRepertory"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    params = {"skuCode": 'mate30_金桔黄_6寸'}  # 输入精确的商品名
    headers = {"token": pub_data['token']}
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method, url=uri, pub_data=pub_data, params=params, status_code=status_code,
                         expect=expect, feature=feature, story=story, title=title, headers=headers)


def test_add_Order(pub_data):  # 无签名无加密下单
    method = "POST"  # 请求方法，全部大写
    feature = "订单模块"  # allure报告中一级分类
    story = '无加密下单'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/order/addOrder"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
  {
  "ordeerPrice": 20000,
  "orderLineList": [
    {
      "qty": 2,
      "skuCode": "mate30_金桔黄_6寸"
    }
  ],
  "receiver": "15221818789",
  "receiverPhone": "15221818789",
  "receivingAddress": "地球村1号",
  "sign": "李月生",
  "userName": "ls2000"
}
    '''
    headers = {"token": pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(headers=headers, method=method, url=uri, pub_data=pub_data, json_data=json_data,
                         status_code=status_code, expect=expect, feature=feature, story=story, title=title)

def test_add_Order_sign(pub_data):  # 签名下单
    method = "POST"  # 请求方法，全部大写
    feature = "订单模块"  # allure报告中一级分类
    story = '签名下单'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/order/addOrderSignBody"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    s="receiver=15221818789&ordeerPrice=20000&receiverPhone=15221818789&key=guoya"
    sign=md5_passwd(s,"")
    pub_data["sign"]=sign
    json_data = '''
  {
  "ordeerPrice": 2000
  "orderLineList": [
    {
      "qty": 2,
      "skuCode": "mate30_金桔黄_6寸"
    }
  ],
  "receiver": "15221818789",
  "receiverPhone": "15221818789",
  "receivingAddress": "地球村1号",
  "sign": "${sign}",
  "userName": "ls2000"
}
    '''
    headers = {"token": pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(headers=headers, method=method, url=uri, pub_data=pub_data, json_data=json_data,
                         status_code=status_code, expect=expect, feature=feature, story=story, title=title)


