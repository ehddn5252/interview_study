from db.db_pool import DbPool
from typing import Dict


class DML(object):
    _conn = DbPool.get_instance().get_connect()

    # not tested
    def insert_one(self, table_name: str = "question", data: Dict = {}):
        cursor = self._conn.cursor()
        sql = f"insert into {table_name}(name,type,content) values("
        vars = []
        for i, (k, v) in enumerate(data.items()):
            if i == len(data) - 1:
                sql += f"{k})"
            else:
                sql += f"{k}, "
            vars.append(v)

        for i in range(len(vars)):
            if i == 0:
                sql += f'('
            if i == len(vars) - 1:
                sql += '%s)'
            else:
                sql += '%s,'
        print(sql)
        cursor.execute(sql)
        self._conn.commit()
        self._conn.close()

    def close(self):
        self._conn.close()
