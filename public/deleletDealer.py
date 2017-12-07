# -*- coding:utf-8 -*-
import pymysql.cursors

def deleteDealer(dealerid):
    connection = pymysql.connect(
        host='106.14.243.44',
        user='qr_bh',
        password='zBO0NCEe',
        db='qr_bh',
        charset='utf8'
    )
    if dealerid == '':
        connection.close()
    else:
        try:
            with connection.cursor() as cursor:
                sql = "delete from de_dealer where id = %s"
                cursor.execute(sql,(dealerid,))
                connection.commit()
        finally:
            connection.close()


