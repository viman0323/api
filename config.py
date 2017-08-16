#!flask/bin/python
# -*- coding: utf-8 -*-


class DbConf(object):
    ## Mysql Db
    MYSQL_USER = 'api'
    MYSQL_PASS = 'EXhW5FU8zhoM'
    MYSQL_HOST = '192.168.0.166'
    MYSQL_PORT = '3306'
    MYSQL_DB = 'api'

    MYSQL_INFO = "mysql://api:EXhW5FU8zhoM@192.168.0.166:3306/api?charset=utf8"

    ## Redis Db
    REDIS_HOST = '192.168.0.166'
    REDIS_PORT = '6379'
    REDIS_DB = '1'


Conf = DbConf
