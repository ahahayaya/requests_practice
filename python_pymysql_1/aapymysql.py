import pymysql
#对数据库做了写操作，需要提交操作conn.commit()





#创建数据库连接
conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',password='root',database='User',charset='utf8')
# 创建游标
cur = conn.cursor()
query_select = "select * from User_like_book "
# 执行查询操作
cur.execute(query_select)

# insert_sql ="insert into User_like_book(book_product,book_name,user_name,book_price)values('qqq','www','eee',1)"
# cur.execute(insert_sql)
# conn.commit()






# # 查询sql查询的所有数据   用游标查询数据只能用一次就被释放掉了，不能重复使用
print(cur.fetchall())
#
# print(cur.fetchone())

cur.close()
conn.close()
