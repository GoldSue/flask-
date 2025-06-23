from flask import Blueprint,session, render_template, request, redirect, url_for
from Day21.utils.db import fetch_all,fetch_one

od = Blueprint('order', __name__)


@od.route('/order/list')
def order_list():
    user_info = session.get("user_info")
    real_name = user_info['real_name']
    print("user_info:", user_info)
    role = int(user_info.get("role", 1))
    if role == 2:
        sql = "select * from orders LEFT JOIN userinfo on orders.user_id = userinfo.id"
        data_list = fetch_all(sql)
    else:
        sql = "select * from orders LEFT JOIN userinfo on orders.user_id = userinfo.id where orders.user_id = %s"
        data_list = fetch_all(sql, (user_info["id"],))
    status_dict = {
        1: "待执行",
        2: "正在执行",
        3: "完成",
        4: "失败",
    }
    print("执行SQL:", sql)
    print("返回条数:", len(data_list))
    for row in data_list:
        print(row)
    return render_template('order_list.html', data_list=data_list, status_dict=status_dict,real_name=real_name)


@od.route('/order/create')
def create_list():
    return "创建订单"


@od.route('/order/delete')
def delete_list():
    return "删除订单"
