from .base import *

DEBUG=True 

# Inital Setting for sqlite3
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

#connection with mysql using mysqlclient that has been installed in site-packages in virtualenv
# DATABASES = {
#     'default': {
#         'ENGINE':'django.db.backends.mysql',
#         'NAME':'xe',
#         'USER':'yourID',
#         'PASSWORD':'yourPASSWORD',
#         'HOST':'localhost',
#         'PORT':'3306',
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE':'django.db.backends.postgresql',
#         'NAME':'test5',
#         'USER':'userid',
#         'PASSWORD':'userpassword',
#         'HOST':'localhost',
#         'PORT':'5432',
#     }
# }