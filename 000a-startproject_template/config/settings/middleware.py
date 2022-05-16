
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # WhiteNoise 中间件应该直接放在 Django SecurityMiddleware之后和所有其他中间件之前
    # http://whitenoise.evans.io/en/stable/django.html#enable-whitenoise
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
