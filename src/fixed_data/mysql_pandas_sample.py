# -*- coding:utf-8 -*-

import MySQLdb
import yaml
import pandas as pd

#main function
if __name__ == '__main__':
    f = open("connect.yml", "r+")
    conn_info = yaml.load(f)
    conn = MySQLdb.connect(
        user=conn_info['user'],
        passwd=conn_info['passwd'],
        host=conn_info['host'],
        db=conn_info['db']
    )
    #c = conn.cursor()

    # テーブル一覧の取得
    sql = """
    select * from table_name
    """

    #データの取得＆pandasの形式への変換
    result = pd.read_sql(sql,conn)
    print(result.describe())
