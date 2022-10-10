import unittest
from app.models import User

'''
from flask import Flask
from exts import db
app = Flask(__name__)
db.init_app(app)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()



'''
class UserModelTestCase(unittest.TestCase):
    #测试hash值是否设置成功
    def test_password_setter(self):
        u = User(password = "cat")
        self.assertTrue(u.password_hash is not None)
    #测试实例是否不能访问password属性
    def test_no_password_getter(self):
        u = User(password = "cat")
        with self.assertRaises(AttributeError):
            u.password
    #验证转换回来的密码等于原密码
    def test_password_verification(self):
        u = User(password = "cat")
        self.assertTrue(u.verify_password("cat"))
        self.assertFalse(u.verify_password("dog"))
    #验证每次hash转换的密码编码都是随机的
    def test_password_salts_are_random(self):
        u = User(password = "cat")
        u2 = User(password = "cat")
        self.assertTrue(u.password_hash != u2.password_hash)