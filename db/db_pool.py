from info.infos import Info
import pymysql
from typing import Dict


class DbPool(object):
    _conn = None
    _instance = None

    def __init__(self):
        raise RuntimeError('Call get_instance() instead')

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls._instance = super(DbPool, cls).__new__(cls)
        return cls._instance

    @classmethod
    def get_instance(cls, db_instance_info: Dict = None):
        if cls._instance is None:
            print("create new instance")
            cls._instance = cls.__new__(cls)
            db = Info.DB.LOCAL_CONNECT_INFO
            if db_instance_info is not None:
                db.update(db_instance_info)
            cls._conn = pymysql.connect(host=db['HOST'], port=db['PORT'], user=db['USER'], password=db['PASSWORD'],
                                        database=db['DATABASE'],
                                        charset='utf8')
        return cls._instance

    @classmethod
    def get_local_instance(cls):
        if cls._instance is None:
            print("create new instance")
            cls._instance = cls.__new__(cls)
            local = Info.DB.LOCAL_CONNECT_INFO
            cls._conn = pymysql.connect(host=local['HOST'],
                                        port=local['PORT'],
                                        user=local['USER'],
                                        password=local['PASSWORD'],
                                        database=local['DATABASE'],
                                        charset='utf8')
        return cls._instance

    def get_connect(self):
        return self._conn

    def close(self):
        self._conn.close()
