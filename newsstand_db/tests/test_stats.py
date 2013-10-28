from unittest import TestCase
from newsstand_db import newsstandDB as ndb
from os.path import isfile
from os import remove
from os import path

'''
Functions to test:
    calculateUniqueUsers() #calculate the amount of people who downloaded the app (unique)
    calculatePayingUsers() #calculate the amount of people who made a purchase
    calculateConversion(users,payingUsers) #calculate the ratio between people who 
        download the app and people who make a purchase
    calculateTotalProceeds() #calculate the total revenue
    calculateProceedsPerUser(proceeds,users) #calclulate the ratio between proceeds 
        and total downloads (unique)
    calculateCLV(proceeds,payingUsers) #calculate the customer lifetime value 
        (ratio between total paying usrs and proceeds)
    calculateCurrentSubscribers(): calculate the amount of subscribers active in 
        the past 30 days
'''

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
#         self.__db.con.close() #Debug
        
    def testUniqueUsers(self):
        s = self.__db.calculateUniqueUsers()        
#         print s #Debug
        self.assertTrue(isinstance(s, int),'Unique users is not an integer')
        self.assertEqual(s, 346, 'Unique users doesn\'t return the expected value')
        
    def testPayingUsers(self):
        s = self.__db.calculatePayingUsers()   
#         print s #Debug     
        self.assertTrue(isinstance(s, int),'Paying users is not an integer')
        self.assertEqual(s, 19, 'Paying users doesn\'t return the expected value')
        
    def testConversion(self):
        s = self.__db.calculateConversion(30,3)        
        self.assertTrue(isinstance(s, float),'Conversion is not a float')
        self.assertEqual(s, 0.1, 'Conversion doesn\'t return the expected value')
        
    def testProceeds(self):
        s = self.__db.calculateTotalProceeds()        
        self.assertTrue(isinstance(s, float),'Total proceeds is not a float')
        self.assertAlmostEqual(s, 70.7, msg='Total proceeds doesn\'t return the expected value',
                               delta=0.1)
        
    def testProceedsPerUser(self):
        s = self.__db.calculateProceedsPerUser(10.0,30)        
        self.assertTrue(isinstance(s, float),'Proceeds per user is not a float')
        self.assertAlmostEqual(s, 0.33, msg='Proceeds per user doesn\'t return the expected value',
                               delta=0.01)
    
    def testCLV(self):
        s = self.__db.calculateCLV(10.0,3)        
        self.assertTrue(isinstance(s, float),'CLV is not a float')
        self.assertAlmostEqual(s, 3.3, msg='CLV doesn\'t return the expected value',delta=0.1)
        
    def testSubscribers(self):
        s = self.__db.calculateCurrentSubscribers()        
        self.assertTrue(isinstance(s, int),'Current subscribers is not an integer')
        self.assertEqual(s, 14, 'Current subscribers doesn\'t return the expected value')
        
    def testBuildStats(self):
        self.assertFalse(self.__db.buildStats(), 'Build stats failed')        
        
    def testWriteStats(self):
        self.__db.buildStats()
        self.__db.writeStats()
        self.__db.cur.execute('SELECT * FROM stats')
        s = self.__db.cur.fetchall()
#         print s #Debug
        self.assertEqual(len(s), 1, 'The length of the stats table is not as expected')
        
class TestStatsFail(TestCase):
    def setUp(self):
        self.__path = path.split(__file__)[0]
        self.__db = ndb(path.join(self.__path,'test.sql'))
        self.__db.createDB()
        self.__db.importData(path.join(self.__path,'test2.csv'))
        
    def tearDown(self):
        self.__db.removeDB()
#         self.__db.con.close() # Debug

    def testBuildStatsFail(self):
        with self.assertRaises(SystemExit) as cm:
            self.__db.buildStats()
            
        self.assertEqual(cm.exception.code, 1)
        