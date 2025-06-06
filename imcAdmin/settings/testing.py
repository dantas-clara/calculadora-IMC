from .settings import *


DEBUG = True
# Crie a secret key para seu ambiente de teste


SECRET_KEY = 'ixb6fh&#ts=&bt$5457kjh-==0%%mdbduf144254dw2j==j)d^3-j$!z(@*m+-h'

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