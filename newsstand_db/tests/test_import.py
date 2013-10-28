from unittest import TestCase
from newsstand_db import newsstandDB as ndb
from sqlite3 import IntegrityError
from os import path

class TestImport(TestCase):
    
    def setUp(self):
        self.__path = path.split(__file__)[0]
        self.db = ndb(path.join(self.__path,'test.sql'))
        self.db.createDB()
        
    def tearDown(self):
        self.db.removeDB()
    
    def testImportCSV(self):
        d = self.db.importCSV(path.join(self.__path,'test.csv'))
#         print d #Debug
        self.assertIsInstance(d, list, 'importCSV doesn\'t return a list')
#         print len(d) #Debug
        self.assertEqual(len(d), 10, 'The result of importCSV is not of the expected length')
        
    def testImportData(self):
        self.db.importData(path.join(self.__path,'test.csv'))
        self.db.cur.execute('SELECT * FROM data')
        s = self.db.cur.fetchall()
#         print len(s) #Debug
        self.assertEqual(len(s), 10, 'The length of the importData table is not as expected')
        
    def testImportDataTwice(self):
        self.db.importData(path.join(self.__path,'test.csv'))
        self.db.importData(path.join(self.__path,'test.csv'))
#         should not happen if exception is handled correctly
#         self.assertRaises(IntegrityError, self.db.importData,'test.csv')
        self.db.cur.execute('SELECT * FROM data')
        s = self.db.cur.fetchall()
#         print len(s) #Debug
        self.assertEqual(len(s), 10, 'The length of the importData table is not as expected')
        
    def testImportOptin(self):
        self.db.importOptin(path.join(self.__path,'testOptin.csv'))
        self.db.cur.execute('SELECT * FROM optin')
        s = self.db.cur.fetchall()
#         print len(s) #Debug
        self.assertEqual(len(s), 10, 'The length of the importOptin table is not as expected')
        
    def testImportOptinTwice(self):
        self.db.importOptin(path.join(self.__path,'testOptin.csv'))
        self.db.importOptin(path.join(self.__path,'testOptin.csv'))
#         should not happen if exception is handled correctly     
        self.db.cur.execute('SELECT * FROM optin')
        s = self.db.cur.fetchall()
#         print len(s) #Debug
        self.assertEqual(len(s), 10, 'The length of the importOptin table is not as expected')   
#         self.assertRaises(IntegrityError, self.db.importOptin,'testOptin.csv')
        