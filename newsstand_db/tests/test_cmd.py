from unittest import TestCase
import unittest
from newsstand_db import newsstandDB as ndb
from os import remove
from subprocess import call

from newsstand_db.cmd import newsstanddb_create
from newsstand_db.cmd import newsstanddb_import
from newsstand_db.cmd import newsstanddb_autoupdate


class TestCmd(TestCase):
    def setUp(self):
        self.__db = ndb('test.sql')
        
    def tearDown(self):
        self.__db.removeDB()
#         self.__db.con.close() # Debug
    
#     @unittest.skip('Temp')    
    def testCreate(self):
        self.assertFalse(call(["newsstanddb-create", "test.sql"]), "newsstanddb-create failed")
    
#     @unittest.skip('Temp')    
    def testCreateFail(self):
        self.assertTrue(call(["newsstanddb-create", "/test.sql"]), ''''newsstanddb-create succeeded
        when it should have failed''')
    
#     @unittest.skip('Temp')    
    def testMultipleImport(self):
        self.__db.createDB()
        self.__db.con.close()
        self.assertFalse(call(["newsstanddb-import", "test.csv", "test2.csv", "testOptin.csv"]), 
                         "newsstanddb-import failed")
        
#     @unittest.skip('Temp')    
    def testMultipleImportFail(self):
        self.__db.createDB()
        self.__db.con.close()
        self.assertFalse(call(["newsstanddb-import", "test.csv", "faketest.csv"]), 
                         "newsstanddb-import failed to handle the exception properly")
    
#     @unittest.skip('Temp')      
    def testAutoUpdate(self):
        self.__db.createDB()
        #Product setup
        self.__db.addProduct('02/01/2013','IA1',3.5)
        self.__db.addProduct('02/01/2013','IAY',1.4)
        self.__db.addProduct('10/01/2013','IAY',2.1)
        #Test
        self.assertFalse(call(["newsstanddb-update", "-d", ".", "-p", "*.csv", "-o", "stats.md"]), 
                         "newsstanddb-update failed")
        remove('stats.md')
        
#     @unittest.skip('Temp')      
    def testAutoUpdateVerbose(self):
        self.__db.createDB()
        #Product setup
        self.__db.addProduct('02/01/2013','IA1',3.5)
        self.__db.addProduct('02/01/2013','IAY',1.4)
        self.__db.addProduct('10/01/2013','IAY',2.1)
        #Test
        self.assertFalse(call(["newsstanddb-update", "-d", ".", "-p", "*.csv", "-o", "stats.md", 
                               "-vvv"]),"newsstanddb-update failed")
        remove('stats.md')

#     @unittest.skip('Temp')          
    def testGetStats(self):
        self.__db.createDB()
        #Product setup
        self.__db.addProduct('02/01/2013','IA1',3.5)
        self.__db.addProduct('02/01/2013','IAY',1.4)
        self.__db.addProduct('10/01/2013','IAY',2.1)
        #Test
        call(["newsstanddb-import", "test.csv", "test2.csv", "testOptin.csv"])
        self.assertFalse(call(["newsstanddb-stats",]),"newsstanddb-stats failed")

#     @unittest.skip('Temp')          
    def testGetDBFile(self):
        self.assertTrue(call(["newsstanddb-getdbfile",]),"newsstanddb-getdbfile failed")
        
#     @unittest.skip('Temp')          
    def testSetDBFile(self):
        self.assertFalse(call(["newsstanddb-setdbfile","test.sql"]),"newsstanddb-setdbfile failed")