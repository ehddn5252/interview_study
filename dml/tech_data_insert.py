from data import question_data
from db.db_pool import DbPool


def insert_data(conn):
    """
        id int auto_increment primary key,
        name varchar(255),
        type  varchar(255),
        content varchar(1000),
        isCompleted tinyint(4)
        """
    cursor = conn.cursor()
    name = "sj"
    question_types = ["java", "os", "data_structure", "network", "algorithm", "backend", 'db', 'common']
    datas = [question_data.java, question_data.os, question_data.data_structure, question_data.network,
             question_data.algorithm, question_data.backend, question_data.db, question_data.common]
    print(len(question_types))
    print(len(datas))
    for question_type, data in zip(question_types, datas):
        sql = "insert into question(name,type,content,isCompleted) values"
        for index, content in enumerate(data):
            if index == len(data) - 1:
                sql += f'("{name}", "{question_type}","{content}",0);'
                break
            else:
                sql += f'("{name}", "{question_type}","{content}",0),'
        cursor.execute(sql)
        conn.commit()
        print(sql)

    conn.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    conn = DbPool.get_instance().get_connect()
    insert_data(conn)
