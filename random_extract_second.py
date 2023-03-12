import random
from data.category import question_types
from db.db_pool import DbPool
from typing import Dict
from datetime import datetime
from pprint import pprint


def extract_question(cursor, name: str, question_number: int, content_type: Dict = None):
    sql = f"select id, content, isCompleted from question where name='{name}' and type='{content_type}' and isCompleted =0"
    # sql = f"select id, content, from question where name='{name}' and isCompleted =0"

    if content_type is None:
        sql = f"select id, content, isCompleted from question where name='{name}' and isCompleted =0"
    cursor.execute(sql)
    tmp = cursor.fetchall()
    questions = []
    for i in range(len(tmp)):
        if tmp[i][2]:
            continue
        else:
            questions.append(tmp[i][:2])


if __name__ == '__main__':
    # db 에 logs라는 db 만들기
    question_num = 10
    my_question = set([])
    questions = list({(392, '트리거(Trigger)에 대해 설명해주세요'),
                 (393, 'Index에 대해 설명해주시고, 장/단점에 대해 아는 대로 말해주세요'),
                 (397, '데이터베이스 이상 현상의 종류에 대해 설명해주세요'),
                 (399, 'SQL Injection을 방어 및 방지하기 위한 방법에 대해 설명해주세요'),
                 (401, '트랜잭션이란 무엇인지 설명해주세요'),
                 (402, '트랜잭션의 특성(ACID)에 대해 설명해주세요'),
                 (404, 'Elastic Search의 키워드 검색과 RDBMS의 LIKE 검색의 차이에 대해 설명해주세요'),
                 (405, '옵티마이저(Optimizer)에 대해 아는 대로 말해주세요'),
                 (411, 'HAVING과 WHERE의 차이를 설명해주세요'),
                 (412, 'JOIN에서 ON과 WHERE의 차이를 설명해주세요')})
    while len(my_question) < question_num:
        my_question.add(questions[n])
    print(my_question)