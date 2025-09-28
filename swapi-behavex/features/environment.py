import os

def before_all(context):
    context.base_url = os.getenv('SWAPI_BASE_URL', 'https://swapi.dev/api')
    context.timeout = float(os.getenv('SWAPI_TIMEOUT', '3.0'))
