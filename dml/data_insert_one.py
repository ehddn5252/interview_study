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
    sql = "insert into question(name,type,content) values"
    name = "dw"
    type = "java"
    for index, content in enumerate(question_data.java):
        if index == len(question_data.personality) - 1:
            sql += f'("{name}", "{type}","{content}");'
            break
        else:
            sql += f'("{name}", "{type}","{content}"),'

    print(sql)
    cursor.execute(sql)
    conn.commit()
    conn.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    conn = DbPool.get_instance().get_connect()
    insert_data(conn)
