from flask import Blueprint,session, render_template, request, redirect, url_for

from Day21 import create_app
from Day21.utils import db
from Day21.utils.db import fetch_all,fetch_one
from Day21.utils import cache



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
    status_dict = {1: {"text":"待执行", "color":"primary"},
                   2: {"text":"正在执行", "color":"warning"},
                   3: {"text":"完成", "color":"success"},
                   4: {"text":"失败", "color":"danger"},

    }
    print("执行SQL:", sql)
    print("返回条数:", len(data_list))
    for row in data_list:
        print(row)
    return render_template('order_list.html', data_list=data_list, status_dict=status_dict,real_name=real_name)


@od.route('/order/create', methods=["GET", "POST"])
def order_create():
    if request.method == "GET":
        return render_template("order_create.html")
    url = request.form.get("url")
    count = request.form.get("count")
    params = [url, count, session.get("user_info").get("id")]
    order_id = db.create("insert into orders(url,count,user_id,status)values (%s,%s,%s,1)",params)
    print(order_id)
    cache.push_queue(order_id)
    return redirect('/order/list')


@od.route('/order/delete')
def delete_list():
    return "删除订单"





