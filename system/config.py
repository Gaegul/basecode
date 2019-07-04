import os

mysql_config = {
    'host': os.environ.get('MYSQL_HOST', 'localhost'),
    'user': os.environ.get('MYSQL_USER', 'root'),
    'pass': os.environ.get('MYSQL_PASS', ''),
    'db': os.environ.get('MYSQL_DB', 'basecode'),
}


def sqlalchemy_url():
    return 'mysql://%s:%s@%s/%s?charset=utf8' % (
        mysql_config['user'], mysql_config['pass'], mysql_config['host'], mysql_config['db']
    )


class Config:
    HOST = ''
    PORT = 8080
    DEBUG = True
