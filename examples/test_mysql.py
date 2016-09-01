# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
import pymysql
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='xitao',
db='mysql')
cur = conn.cursor()
cur.execute("SELECT * FROM user")
for r in cur.fetchall():
           print(r)
           #cur.close()
conn.close()

