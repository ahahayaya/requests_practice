import pymysql
def sql(condition):
    conn = pymysql.connect(host='localhost',database='homework',user='root',passwd='ab123456')
    cur = conn.cursor()
    cur.execute(condition)
    print(cur.fetchone())
sql('select * from config_total')