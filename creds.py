import os

CREDENTIALS = {
    'email': os.environ.get('EMAIL'),
    'password': os.environ.get('PASSWORD'),
    'subdomain': os.environ.get('SUBDOMAIN')
}