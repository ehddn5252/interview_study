from db.db_pool import DbPool

def update_isCompleted(conn, numbers,to_change):
    cursor = conn.cursor()
    sql = f"UPDATE question SET isCompleted = {to_change} where id=%s;"
    print(sql)
    cursor.executemany(sql, numbers)
    conn.commit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # complted 한 것의
    completed_number = [1, 2, 3]
    conn = DbPool.get_instance().get_connect()
    update_isCompleted(conn, completed_number,0)
