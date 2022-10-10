from flask_wtf import Form
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import InputRequired,Length,Email
#登录的验证表单
class LoginForm(Form):
    email = StringField("Email",validators=[InputRequired(),Length(1,64),Email()])
    password = PasswordField("Password",validators=[InputRequired()])
    remember_me = BooleanField("keep me logged in")
    submit = SubmitField("Log In")