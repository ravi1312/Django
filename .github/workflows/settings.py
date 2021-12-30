import os

ALLOWED_HOSTS = ['http://django-env-1.eba-qxakrfjp.us-east-1.elasticbeanstalk.com/']

DATABASES = {
'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': os.environ['RDS_DB_NAME'],
    'USER': os.environ['ravi'],
    'PASSWORD': os.environ['ravi1312'],
    'HOST': os.environ['RDS_HOSTNAME'],
    'PORT': os.environ['RDS_PORT'],
    }
}
