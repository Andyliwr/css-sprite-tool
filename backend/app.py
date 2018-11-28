#!/usr/bin/python
# -*- coding: UTF-8 -*-
from flask import Flask, url_for, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/user/<username>')
def show_user_profile(username):
    # 展示用户信息
    return 'User %s' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # 展示文章详情，文章id是整数
    return 'Post %d' % post_id


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        pass
    else:
        pass

# with app.test_request_context():
#     print url_for('show_user_profile', username='andyliwr')
#     print url_for('static', 'style.css')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
