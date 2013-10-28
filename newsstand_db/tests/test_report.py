from unittest import TestCase
from newsstand_db import newsstandDB as ndb
from os.path import isfile
from os import remove

class TestStats(TestCase):
    def setUp(self):
        self.__db = ndb('test.sql')
        self.__db.createDB()
        self.__db.importData('test2.csv')
        #Product setup
        self.__db.addProduct('02/01/2013','IA1',3.5)
        self.__db.addProduct('02/01/2013','IAY',1.4)
        self.__db.addProduct('10/01/2013','IAY',2.1)
        
    def tearDown(self):
        self.__db.removeDB()
        
    def testOutputStats(self):
        self.__db.buildStats()
        self.__db.outputStats('stats.md')
        self.assertTrue(isfile('stats.md'), 'The stats file is not being created')
        remove('stats.md')
    
    def testPrintStats(self):
        self.__db.buildStats()
        self.__db.printStats()
        
    def testOptinExport(self):
        pass
    
    def testOutputStatsHistorical(self):
        pass
    
    def testOutputStatsChart(self):
        pass