DEBUG = False
ALLOWED_HOSTS = ['dohaich.ru','www.dohaich.ru']

#settings for db on server
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'likwid_db1',
#         'USER': 'django_likwid',
#         'PASSWORD': 'vftv6iI&',
#         'HOST': 'localhost',
#         'PORT': '',                      # Set to empty string for default.
#     }
# }
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'localhost'
# EMAIL_PORT = '1025'
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = "info@doxaih.ru"
EMAIL_HOST_PASSWORD = "In123456"
EMAIL_USE_SSL = True
# SERVER_EMAIL = EMAIL_HOST_USER
# DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
