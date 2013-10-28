from unittest import TestCase
import unittest
from newsstand_db import newsstandDB as ndb
from os import remove
from subprocess import call, check_output, CalledProcessError
from os import path

class TestCmd(TestCase):
    def setUp(self):
        self.__path = path.split(__file__)[0]
        self.__testsql = path.join(self.__path,'test.sql')
        self.__testcsv = path.join(self.__path,'test.csv')
        self.__test2csv = path.join(self.__path,'test2.csv')
        self.__testoptin = path.join(self.__path,'testOptin.csv')
        self.__faketest = path.join(self.__path,'faketest.csv')
#         self.__statsmd = path.join(self.__path,'stats.md') #Fails test
        self.__statsmd = 'stats.md'
        
        self.__db = ndb(self.__testsql)
        
    def tearDown(self):
        self.__db.removeDB()
#         self.__db.con.close() # Debug
    
#     @unittest.skip('Temp')    
    def testCreate(self):
        self.assertFalse(call(["newsstanddb-create", self.__testsql]), "newsstanddb-create failed")
    
#     @unittest.skip('Temp')    
    def testCreateFail(self):
        self.assertTrue(call(["newsstanddb-create", "/test.sql"]), ''''newsstanddb-create succeeded
        when it should have failed''')
    
#     @unittest.skip('Temp')    
    def testMultipleImport(self):
        self.__db.createDB()
        self.__db.con.close()
        self.assertFalse(call(["newsstanddb-import", self.__testcsv, self.__test2csv, self.__testoptin]), 
                         "newsstanddb-import failed")
        
#     @unittest.skip('Temp')    
    def testMultipleImportFail(self):
        self.__db.createDB()
        self.__db.con.close()
        self.assertFalse(call(["newsstanddb-import", self.__testcsv, self.__faketest]), 
                         "newsstanddb-import failed to handle the exception properly")
    
#     @unittest.skip('Temp')      
    def testAutoUpdate(self):
        self.__db.createDB()
        #Product setup
        self.__db.addProduct('02/01/2013','IA1',3.5)
        self.__db.addProduct('02/01/2013','IAY',1.4)
        self.__db.addProduct('10/01/2013','IAY',2.1)
        #Test
        self.assertFalse(call(["newsstanddb-update", "-d", ".", "-p", "*.csv", "-o", self.__statsmd]), 
                         "newsstanddb-update failed")
        remove(self.__statsmd)
        
#     @unittest.skip('Temp')      
    def testAutoUpdateVerbose(self):
        self.__db.createDB()
        #Product setup
        self.__db.addProduct('02/01/2013','IA1',3.5)
        self.__db.addProduct('02/01/2013','IAY',1.4)
        self.__db.addProduct('10/01/2013','IAY',2.1)
        #Test
        self.assertFalse(call(["newsstanddb-update", "-d", ".", "-p", "*.csv", "-o", self.__statsmd, 
                               "-vvv"]),"newsstanddb-update failed")
        remove(self.__statsmd)

#     @unittest.skip('Temp')          
    def testGetStats(self):
        self.__db.createDB()
        #Product setup
        self.__db.addProduct('02/01/2013','IA1',3.5)
        self.__db.addProduct('02/01/2013','IAY',1.4)
        self.__db.addProduct('10/01/2013','IAY',2.1)
        #Test
        call(["newsstanddb-import", self.__testcsv, self.__test2csv, self.__testoptin])
        self.assertFalse(call(["newsstanddb-stats",]),"newsstanddb-stats failed")

#     @unittest.skip('Temp')          
    def testGetDBFile(self):
        self.assertTrue(call(["newsstanddb-getdbfile",]),"newsstanddb-getdbfile failed")
        
#     @unittest.skip('Temp')          
    def testSetDBFile(self):
        self.assertFalse(call(["newsstanddb-setdbfile",self.__testsql]),"newsstanddb-setdbfile failed")
        
#     @unittest.skip('Temp')
    def testAddProduct(self):
        self.__db.createDB()
        #Test
        self.assertFalse(call(["newsstanddb-addproduct","02/01/2013","IA1","3.5"]),
                         "newsstanddb-addproduct failed")
        self.assertFalse(call(["newsstanddb-addproduct","02/01/2013","IAY","1.4"]),
                         "newsstanddb-addproduct failed")
        self.assertFalse(call(["newsstanddb-addproduct","10/01/2013","IAY","2.1"]),
                         "newsstanddb-addproduct failed")

    @unittest.skip('Fails in shell')      
    def testAutoUpdateFail(self):
        self.__db.createDB()
        #Test
#         self.assertEqual(call(["newsstanddb-update", "-d", ".", "-p", "*.csv", "-o", self.__statsmd],shell=True), 
#                          1)
        with self.assertRaises(CalledProcessError) as cm:
            check_output(["newsstanddb-update", "-d", ".", "-p", "*.csv", "-o", self.__statsmd],shell=False)
            
        self.assertEqual(cm.exception.returncode, 1)
            