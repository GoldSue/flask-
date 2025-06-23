from flask import Blueprint,session, render_template, request, redirect, url_for
from Day21.utils.db import fetch_all,fetch_one

od = Blueprint('order', __name__)


@od.route('/order/list')
def order_list():
    user_info = session.get("user_info")
    role = user_info['role']
    if role == 2:
        data_list = fetch_all("select * from `order`")
    else:
        data_list = fetch_all("select * from `order` where user_id = %s",(user_info["id"],))
    print(data_list)
    return render_template('order_list.html', data_list=data_list)


@od.route('/order/create')
def create_list():
    return "创建订单"


@od.route('/order/delete')
def delete_list():
    return "删除订单"
