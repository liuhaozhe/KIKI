import pymysql
from db_cn import UseDatebase

dbconfig = {'host':'127.0.0.1',
                'user':'root',
                'passwd':'liuhaozhe0253',
                'db':'KIKI', }

data = [
    ('liuhaozhe','aeiou','127.0.0.1','Firefox',"{'e','i'}"),
]

sql_search_code="""
                    select * from user_info
                """

def indb(data):
    with UseDatebase(dbconfig) as cur:
        sql = 'insert into user_info(user, email) values(%s,%s);'
        # 拼接并执行sql语句
        cur.executemany(sql, data)

#indb(data)

def outdb(sqlcode):
    with UseDatebase(dbconfig) as cur:
        _SQL = sqlcode
        cur.execute(_SQL)
        res = cur.fetchall()
        return res

result = outdb(sql_search_code)

for d in result:
    print(d)


