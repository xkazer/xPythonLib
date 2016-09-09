# -*- coding: UTF-8 -*-

import os
import sys
import sqlite3


class osql:
	def __init__(self, path):
		'''获取数据库连接对象，若不存在，则在创建'''
		self.conn = sqlite3.connect(path)
		self.cur = self.conn.cursor()

	def readTables(self):
		self.cur.execute('SELECT name FROM sqlite_master WHERE type=\'table\' ORDER BY name;')
		return self.cur.fetchall()

	def readData(self, table):
		self.cur.execute('SELECT * FROM '+table)
		#print 'select * from '+table
		return self.cur.fetchall()
        
	def execute(self, sql):
		self.cur.execute(sql)
		return self.cur.fetchall()

	def commit(self):
		self.conn.commit()

	def createFromFile(self, file):
		if os.path.exists(file) and os.path.isfile(file):
			_fp = open(file, "r")
			_data = _fp.read().split(';')
			for _sql in _data:
				self.execute(_sql)

