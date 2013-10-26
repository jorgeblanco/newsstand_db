from unittest import TestCase
from newsstand_db import newsstandDB as ndb
from sqlite3 import IntegrityError

class TestImport(TestCase):
    
    def setUp(self):
        self.db = ndb('test.sql')
        self.db.createDB()
        
    def tearDown(self):
        self.db.removeDB()
    
    def testImportCSV(self):
        d = self.db.importCSV('test.csv')
#         print d
        self.assertIsInstance(d, list, 'importCSV doesn\'t return a list')
#         print len(d)
        self.assertEqual(len(d), 10, 'The result of importCSV is not of the expected length')
        
    def testImportData(self):
        self.db.importData('test.csv')
        self.db.cur.execute('SELECT * FROM data')
        s = self.db.cur.fetchall()
#         print len(s)
        self.assertEqual(len(s), 10, 'The length of the importData table is not as expected')
        
    def testImportDataTwice(self):
        self.db.importData('test.csv')
#         self.db.importData('test.csv')
        self.assertRaises(IntegrityError, self.db.importData,'test.csv')
        
    def testImportOptin(self):
        self.db.importOptin('testOptin.csv')
        self.db.cur.execute('SELECT * FROM optin')
        s = self.db.cur.fetchall()
#         print len(s)
        self.assertEqual(len(s), 10, 'The length of the importOptin table is not as expected')
        
    def testImportOptinTwice(self):
        self.db.importOptin('testOptin.csv')
#         self.db.importOptin'testOptin.csv')
        self.assertRaises(IntegrityError, self.db.importOptin,'testOptin.csv')
        