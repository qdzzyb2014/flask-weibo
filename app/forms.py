from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, TextAreaField, PasswordField
from wtforms.validators import Required, Length, Email

class LoginForm(Form):
    user_name = TextField('user_name', validators = [Required()])
    password = PasswordField('password', validators = [Required()]) 
    remember_me = BooleanField('remember_me', default = False)

class SignUpForm(Form):
    user_name = TextField('user_name', validators = [Required()])
    password = PasswordField('password', validators = [Required()])
    user_email = TextField('user_email', validators = [Email(), Required()])

class EditForm(Form):
    nickname = TextField('nickname', validators = [Required()])
    about_me = TextAreaField('about_me', validators = [Length(min = 0, max = 140)])
    
    def __init__(self, original_nickname, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.original_nickname = original_nickname
        
    def validate(self):
        if not Form.validate(self):
            return False
        if self.nickname.data == self.original_nickname:
            return True
        user = User.query.filter_by(nickname = self.nickname.data).first()
        if user != None:
            self.nickname.errors.append('This nickname is already in use. Please choose another one.')
            return False
        return True
        
class PostForm(Form):
    post = TextField('post', validators = [Required()])
    
class SearchForm(Form):
    search = TextField('search', validators = [Required()])

