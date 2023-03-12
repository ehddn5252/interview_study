import random
from data.category import question_types
from db.db_pool import DbPool
from typing import Dict
from datetime import datetime
from pprint import pprint


def extract_question(cursor, name: str, question_number: int, content_type: str = None):
    sql = f"select id, content, isCompleted from question where name='{name}' and type='{content_type}' and isCompleted =0"
    # sql = f"select id, content, from question where name='{name}' and isCompleted =0"

    if content_type is None:
        sql = f"select id, content, isCompleted from question where name='{name}' and isCompleted =0"
    elif content_type == "tech":
        sql = f"select id, content, isCompleted from question where name='{name}' and type!='personality' and isCompleted =0"
    cursor.execute(sql)
    tmp = cursor.fetchall()
    questions = []
    for i in range(len(tmp)):
        if tmp[i][2]:
            continue
        else:
            questions.append(tmp[i][:2])
    my_question = set([])
    while len(my_question) < question_number:
        n = random.randrange(0, len(questions))
        my_question.add(questions[n])
    return my_question


if __name__ == '__main__':
    # db 에 logs라는 db 만들기
    question_num = 2
    conn = DbPool.get_instance().get_connect()
    cur = conn.cursor()
    print(question_types.keys())
    print(datetime.today().date())
    with open(f"result/{datetime.today().date()}personality.txt", 'w', encoding='utf-8') as d:
        tmp = extract_question(cur, 'sj', question_num,"personality")
        pprint(tmp)
        d.write(str(tmp))
        d.close()
    # pprint(extract_question(cur, 'dw', question_num, question_types['personality']))  # (cursor, name, question_number)
