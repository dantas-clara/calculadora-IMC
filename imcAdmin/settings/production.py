from .settings import *


DEBUG = False
# Crie a secret key para seu ambiente de produção


SECRET_KEY = 'ixb6fha#ts=&b4t2u%p1_62-!8dw2245ljyg%$#hgy&^3-j$!z(@*m+-h'

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