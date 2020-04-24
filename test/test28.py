import requests
from lxml import etree
import pymysql
from DBUtils.PooledDB import PooledDB
import time
import random
import sys

pool = PooledDB(pymysql, 10,
                host='localhost',
                port=3306,
                user='root',
                passwd='123456',
                db='ip_proxy_pool',
                charset='utf8'
                )
