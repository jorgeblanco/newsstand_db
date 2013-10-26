from unittest import TestCase
import unittest
from newsstand_db import newsstandDB as ndb
from os import remove

from newsstand_db.cmd import newsstanddb_create
from newsstand_db.cmd import newsstanddb_import
from newsstand_db.cmd import newsstanddb_autoupdate


class TestCmd(TestCase):
    def setUp(self):
        self.__db = ndb('test.sql')
        
    def tearDown(self):
        self.__db.removeDB()
#         self.__db.con.close()
    
#     @unittest.skip('Temp')    
    def testCreate(self):
        newsstanddb_create('test.sql')
    
#     @unittest.skip('Temp')    
    def testMultipleImport(self):
        self.__db.createDB()
        self.__db.con.close()
        newsstanddb_import('test.csv','test2.csv','testOptin.csv')
        self.__db = ndb('test.sql')
        self.__db.buildStats()
        self.__db.writeStats()
        self.__db.outputStats('statsImport.md')
        remove('statsImport.md')
    
#     @unittest.skip('Temp')      
    def testAutoUpdate(self):
        self.__db.createDB()
        newsstanddb_autoupdate('.',('*.csv',),'stats.md')
        remove('stats.md')