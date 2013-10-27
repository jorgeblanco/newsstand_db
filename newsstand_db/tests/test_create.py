from unittest import TestCase
from newsstand_db import newsstandDB as ndb

class TestCreate(TestCase):
    __dataSQL = '''CREATE TABLE data (Provider TEXT, ProviderCountry TEXT, SKU TEXT, Developer TEXT, Title TEXT, Version TEXT, ProductTypeIdentifier TEXT, Units INTEGER, DeveloperProceeds REAL, CustomerCurrency TEXT, CountryCode TEXT, CurrencyOfProceeds TEXT, AppleIdentifier TEXT, CustomerPrice REAL, PromoCode TEXT, ParentIdentifier TEXT, Subscription TEXT, Period TEXT, DownloadDatePST TEXT, CustomerIdentifier TEXT, ReportDate_Local TEXT, SalesReturn TEXT, Category TEXT DEFAULT \'\')'''
    __fileSQL = '''CREATE TABLE file (filename TEXT UNIQUE, hash TEXT UNIQUE)'''
    __statsSQL = '''CREATE TABLE stats (Date TEXT, UniqueUsers INTEGER, PayingUsers INTEGER, Conversion REAL, TotalProceeds REAL, ProceedsPerUser REAL, CLV REAL, CurrentSubscribers INTEGER)'''
    __monthProceedsSQL = '''CREATE TABLE monthProceeds (Month TEXT, Proceeds REAL)'''
    __optinSQL = '''CREATE TABLE optin (FirstName TEXT, LastName TEXT, EmailAddress TEXT, PostalCode TEXT, AppleIdentifier TEXT, ReportStartDate TEXT, ReportEndDate TEXT)'''
    
    def tearDown(self):
        s = ndb('test.sql')
        s.removeDB()
        
    def test_is_ndb(self):
        s = ndb('test.sql')
        self.assertTrue(isinstance(s, ndb))
    
    def testCreate(self):
        # Create database
        s = ndb('test.sql')
        
        # Create tables
        s.createDB()
        
        # Fetch all tables from DB
        s.cur.execute("SELECT name FROM sqlite_master WHERE type = 'table';")
        t = s.cur.fetchall()
#         print t
        #     @unittest.skip('Temp')          
        # Verify that the tables we = ndb('test.sql')re created
        self.assertIn((u'data',), t, '\'data\' table not in database')
        self.assertIn((u'file',), t, '\'file\' table not in database')
        self.assertIn((u'stats',), t, '\'stats\' table not in database')
        self.assertIn((u'monthProceeds',), t, '\'monthProceeds\' table not in database')
        self.assertIn((u'optin',), t, '\'optin\' table not in database')
        
        for name,structure in [('data',self.__dataSQL),('file',self.__fileSQL),
                               ('stats',self.__statsSQL),
                               ('monthProceeds',self.__monthProceedsSQL),
                               ('optin',self.__optinSQL)]:
            # Fetch each table's sql
            code = ''.join(["SELECT sql FROM sqlite_master WHERE type = 'table' AND name = '",name,"';",])
            s.cur.execute(code)
            t = s.cur.fetchone()[0] # No exception handling here, assuming that table still exists
#             print t
        
            # And verify SQL schema is correct
            self.assertEqual(t, structure, ''.join(['\'',name,
                                                    '\' table schema is not as expected',]))