from envparse import env

MONGO_HOST = 'db'
MONGO_PORT = 27017

MONGO_USERNAME = env('MONGO_INITDB_ROOT_USERNAME')
MONGO_PASSWORD = env('MONGO_INITDB_ROOT_PASSWORD')

HOST = "127.0.0.1"

DEBUG = env('DEBUG', default=False, cast=bool)


# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

# Dangerous !!!!
ALLOW_UNKNOWN = True


if DEBUG:
    HOST = "0.0.0.0"

DOMAIN = {
    'users': {},
    'courses': {},
    'enrollments': {},
}
