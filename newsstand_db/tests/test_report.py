from unittest import TestCase
from newsstand_db import newsstandDB as ndb
from os.path import isfile
from os import remove
from os import path

class TestStats(TestCase):
    def setUp(self):
        self.__path = path.split(__file__)[0]
        self.__db = ndb(path.join(self.__path,'test.sql'))
        self.__db.createDB()
        self.__db.importData(path.join(self.__path,'test2.csv'))
        #Product setup
        self.__db.addProduct('02/01/2013','IA1',3.5)
        self.__db.addProduct('02/01/2013','IAY',1.4)
        self.__db.addProduct('10/01/2013','IAY',2.1)
        
    def tearDown(self):
        self.__db.removeDB()
        
    def testOutputStats(self):
        self.__db.buildStats()
        self.__db.outputStats(path.join(self.__path,'stats.md'))
        self.assertTrue(isfile(path.join(self.__path,'stats.md')), 'The stats file is not being created')
        remove(path.join(self.__path,'stats.md'))
    
    def testPrintStats(self):
        self.__db.buildStats()
        self.__db.printStats()
        
    def testOptinExport(self):
        pass #TODO: Add test & function
    
    def testOutputStatsHistorical(self):
        pass #TODO: Add test & function
    
    def testOutputStatsChart(self):
        pass #TODO: Add test & function