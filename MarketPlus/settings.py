"""
Django settings for MarketPlus project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CURRENT_PATH = os.path.abspath(os.path.dirname(__file__)).replace('\\', '/')
os.environ['PATH'] = os.path.join(BASE_DIR, r'env\Lib\site-packages\osgeo') + ';' + os.environ['PATH']

os.environ['PROJ_LIB'] = os.path.join(BASE_DIR, r'env3\Lib\site-packages\osgeo\data\proj') + ';' + os.environ['PATH']

GDAL_LIBRARY_PATH = os.path.join(BASE_DIR, r'env\Lib\site-packages\osgeo\gdal203.dll')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')2vq$^ui@dy&gclpeszp6jl*pqe0$m10#!)+__=8$9#00n0b2#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS	=	['market-plus.com', 'www.market-plus.com', 'www.market-plus.bj', 'www.market-plus.fr', 'wsl-morghoulis.market-plus.com',	'localhost', '192.168.136.1', '192.168.8.150', '127.0.0.1'] 

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    # 'debug_toolbar',
    'Accounts',
    'Blog',
    'Carts',
    'Coupons',
    'Marketing',
    'Orders',
    'Products',
    'Search',
    'Stats',
    'Utils',
    'django.contrib.sites',
    'allauth',
    'taggit',
    'social_django',
    # 'allauth.account',
    # 'allauth.socialaccount',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'debug_toolbar.middleware.DebugToolbarMiddleware'
]
# INTERNAL_IPS = ['127.0.0.1',]

ROOT_URLCONF = 'MarketPlus.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'Utils.context_processors.market_plus',
            ],
        },
    },
]

"""AUTHENTICATION_BACKENDS = (
    #django.contrib.auth.backends.ModelBackend
    #'allauth.account.auth_backends.AuthenticationBackend',
    'social_core.backends.facebook.FacebookOAuth2',
)"""
WSGI_APPLICATION = 'MarketPlus.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db',
        'USER': 'postgres',
        'PASSWORD': "J'SuisAmoureux",
        'HOST': 'localhost',
        'PORT': '5432',
    },
    'other': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/statics/'
STATIC_ROOT = os.path.join(BASE_DIR, "statics", "static_root")
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "statics", "static_files"),
)
# Medias files for the website
MEDIA_URL = '/medias/'
MEDIA_ROOT = os.path.join(BASE_DIR, "statics", "medias")

# Globals statements foe the website
PRODUCTS_PER_PAGE = 12
PRODUCTS_PER_ROW = 4

# Other statements
SITE_ID = 1

LOGIN_URL = '/accounts/login'
LOGOUT_URL = '/accounts/logout'
LOGIN_REDIRECT_URL = '/accounts/my_account/'
SITE_NAME = 'Market Plus '
META_KEYWORDS = ''
META_DESCRIPTION = ''

CANON_URL_HOST = 'www.django-ecommerce.com'
CANON_URLS_TO_REWRITE = ['django-ecommerce.com', 'modernmusician.com']

AUTHNET_POST_URL = 'test.authorize.net'
AUTHNET_POST_PATH = '/gateway/transact.dll'
AUTHNET_LOGIN = ['your login here']
AUTHNET_KEY = ['your transaction key here']


# GOOGLE configurations
GOOGLE_CHECKOUT_MERCHANT_ID = 'your id here'
GOOGLE_CHECKOUT_MERCHANT_KEY = 'your key here'
GOOGLE_CHECKOUT_URL = 'https://sandbox.google.com/checkout/api/v2/merchantCheckout/Merchant/' + \
                      GOOGLE_CHECKOUT_MERCHANT_ID

SOCIAL_AUTH_FACEBOOK_KEY	=	'XXX'	#	Facebook	App	ID
SOCIAL_AUTH_FACEBOOK_SECRET	=	'XXX'	#	Facebook	App	Secret

# EMAILS CONFIGRATIONS
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'your_account@gmail.com'
EMAIL_HOST_PASSWORD = 'your_password'
EMAIL_PORT = 587
EMAIL_USE_TLS = True


"""ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_CONFIRM_EMAIL_ON_GET = False
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = LOGIN_URL
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_URL = None

ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3
ACCOUNT_EMAIL_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = None
ACCOUNT_EMAIL_SUBJECT_PREFIX = 'My Subject'
ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'http'

ACCOUNT_LOGOUT_ON_GET = False
ACCOUNT_LOGOUT_REDIRECT_URL = '/'
ACCOUNT_SIGNUP_FORM_CLASS = None
ACCOUNT_SIGNUP_PASSWORD_VERIFICATION = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USER_MODEL_USERNAME_FIELD = 'username'
ACCOUNT_USER_MODEL_EMAIL_FIELD = "email"

ACCOUNT_USERNAME_MIN_LENGTH = 5
ACCOUNT_USERNAME_BLACKLIST = []
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_PASSWORD_INPUT_RENDER_VALUE = False
ACCOUNT_PASSWORD_MIN_LENGTH = 6
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
"""