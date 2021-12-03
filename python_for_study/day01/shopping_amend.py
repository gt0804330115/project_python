"""

"""
commodity_info = {
    101: {"name": "屠龙刀", "price": 10000},
    102: {"name": "倚天剑", "price": 10000},
    103: {"name": "九阴白骨爪", "price": 8000},
    104: {"name": "九阳神功", "price": 9000},
    105: {"name": "降龙十八掌", "price": 8000},
    106: {"name": "乾坤大挪移", "price": 10000}
}

order = []


def shopping():
    """
        购物
    :return:
    """
    while True:
        item = input("1键购买，2键结算。")
        if item == "1":
            add_shopping_cart()
        elif item == "2":
            settlement()


def settlement():
    """
    商品结算
    :return:
    """
    total_prices = 0
    for item in order:
        commodity = commodity_info[item["goods_number"]]
        print("商品：%s，单价：%d,数量:%d." % (commodity["name"], commodity["price"], item["count"]))
        total_prices += commodity["price"] * item["count"]
    whether_buy_succeed(total_prices)


def whether_buy_succeed(total_prices):
    """
    判断是否购买成功
    :param total_prices:商品总价
    :return:
    """
    while True:
        money = float(input("总价%d元，请输入金额：" % total_prices))
        if money >= total_prices:
            print("购买成功，找回：%d元。" % (money - total_prices))
            order.clear()
            break
        else:
            print("金额不足.")


def add_shopping_cart():
    """
    添加购物车
    :return:
    """
    for key, value in commodity_info.items():
        print("编号：%d，名称：%s，单价：%d。" % (key, value["name"], value["price"]))
    goods_number = is_number_for_commodity_info()
    count = int(input("请输入购买数量："))
    order.append({"goods_number": goods_number, "count": count})
    print("添加到购物车。")


def is_number_for_commodity_info():
    """
    查询商品编号
    :return:
    """
    while True:
        goods_number = int(input("请输入商品编号："))
        if goods_number in commodity_info:
            break
        else:
            print("该商品不存在")
    return goods_number



