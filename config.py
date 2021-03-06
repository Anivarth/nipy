SERVER_NAME = '127.0.0.1:5000'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://test:123456@localhost/test'
SQLALCHEMY_POOL_RECYCLE = 499
SQLALCHEMY_POOL_TIMEOUT = 20
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
BABEL_DEFAULT_LOCALE = 'en'
BABEL_DEFAULT_TIMEZONE = 'Asia/Dhaka'
SECRET_KEY = "Set a long string that can't be guessed easily"
WTF_CSRF_ENABLED = False
DEBUG = True

# Flask-Mail Configs
MAIL_SERVER = 'Your mail server address'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USERNAME = 'Your Email Username'
MAIL_PASSWORD = 'A Strong Password'
MAIL_DEFAULT_SENDER = 'The Email Address from where you like to send mail by default'

# Security Core Configuration
SECURITY_URL_PREFIX = '/account'
SECURITY_PASSWORD_HASH = 'bcrypt'
SECURITY_PASSWORD_SALT = '$2a$16$PnnIgfMwkOjGX4SkHqSOPO'
SECURITY_EMAIL_SENDER = 'The Email Address from where you like to send security mail by default'

# Security URLs and Views
SECURITY_POST_LOGIN_VIEW = '/admin'
SECURITY_POST_LOGOUT_VIEW = '/'
SECURITY_POST_REGISTER_VIEW = '/confirm'

# Secuirty Feature Flags
SECURITY_CONFIRMABLE = True
SECURITY_REGISTERABLE = True
SECURITY_RECOVERABLE = True
SECURITY_TRACKABLE = True
