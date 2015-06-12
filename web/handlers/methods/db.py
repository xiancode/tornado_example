#!/usr/bin/env python
# coding=utf-8

import MySQLdb

conn = MySQLdb.connect(host="localhost", user="root", passwd="125896", db="qiwsirtest", port=3306, charset="utf8")    #连接对象

cur = conn.cursor()    #游标对象


def select_table(table, column, condition, value ):
    sql = "select " + column + " from " + table + " where " + condition + "='" + value + "'"
    cur.execute(sql)
    lines = cur.fetchall()
    return lines