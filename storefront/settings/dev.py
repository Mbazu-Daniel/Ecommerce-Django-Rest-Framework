from .common import * 

SECRET_KEY = "django-insecure-q+0m)p+s-na6j8dgd8k&wwimerg(#5jgnwk+!^-8qxbkz!=#v9"


DEBUG = True


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'storefront',
#         'HOST': 'localhost',
#         'USER': 'sieg',
#         'PASSWORD': 'S13gd0ma1n#'
#     }
# }

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "storefront3",
        "USER": "postgres",
        "PASSWORD": "qwertyuiop",
        "HOST": "localhost",
        "PORT": 5432,
    }
}
