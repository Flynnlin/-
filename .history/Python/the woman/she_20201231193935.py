def sql_write(code1,code2):
    config = {
        
    }
    db_pool = PersistentDB(pymysql, **config)
    # 从数据库连接池是取出一个数据库连接
    conn = db_pool.connection()
    cursor = conn.cursor()
    # 来查下吧
    cursor.execute(str(code1))
    cursor.execute(str(code2))
    # result = cursor.fetchone()
    cursor.connection.commit()
    # print(result)
    # 关闭连接,其实不是关闭,只是把该连接返还给数据库连接池
    conn.close()