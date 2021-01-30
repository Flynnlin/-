"""
数据库连接工具类
# """
from threading import main_thread
import pymysql
from dbutils.persistent_db import PersistentDB
def sqlcon():
    config = {
        'host': '47.96.143.225',
        'port': 3306,
        'database': 'yundonghui',
        'user': 'test',
        'password': '123456',
        'charset': 'utf8'
    }
    db_pool = PersistentDB(pymysql, **config)
    # 从数据库连接池是取出一个数据库连接
    conn = db_pool.connection()
    cursor = conn.cursor()
    # 来查下吧
    cursor.execute('select * from yundongyuan')
    
    result = cursor.fetchall()
    cursor.connection.commit()
    print(result)
    # 关闭连接,其实不是关闭,只是把该连接返还给数据库连接池
    conn.close()
if __name__ == "__main__":
    sqlcon()