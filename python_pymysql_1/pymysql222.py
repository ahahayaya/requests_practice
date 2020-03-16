import pymysql

def update_mysql(product,nprice):
    conn =pymysql.connect(host='127.0.0.1',port=3306,user='root',password='root',database='User',charset='utf8')
    cur = conn.cursor()
    update_price= 'update User_like_book set book_price="{}" where book_product="{}"'.format(nprice,product)
    cur.execute(update_price)
    conn.commit()
    cur.close()
    conn.close()
update_mysql('aaa',12)