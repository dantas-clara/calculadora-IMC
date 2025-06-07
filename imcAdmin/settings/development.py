from .settings import *



DEBUG = True
# Crie a secret key para seu ambiente de desenvolvimento


SECRET_KEY = 'i154kjmedhuyerb745t2u%p1_62-!5w2j==j6d^3-j$!z(@*m+-h'

ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'imcdb',
        'USER': 'user',
        'PASSWORD': 'nova_senha',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}