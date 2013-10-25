#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Search for (similar) web pages

#Imports
# import sqlite as sql
import sqlite3 as sql #Problem with sql.connect()
import os
import time
# from __future__ import division

__author__ = "Jorge Blanco"
__description__ = "Create, search and analyze a DB with your Apple's newsstand app information"
__email__ = "py [at] jorgeblan [dot] co"
__license__ = "GPLv2"
__maintainer__ = "Jorge Blanco"
__status__ = "Development"
__version__ = "0.1"

class newsstandDB:
    '''
    Create, search and analyze a DB with Apple's newsstand information
    **********************************
    Usage:
        createDB() #Creates the DB tables (DB file itself is created at __init__)
        removeDB() # Deletes the DB file
        importData(filename) #imports CSV file into the data table
        importOptin(filename) #imports the optin file into the optin table
        buildStats() #Analyzes the data
        writeStats() #Writes the stats into the stats table
        log(msg) #Write msg to the log
        setLog(log,logfile=None) #Set the logging on or off. (Optional) Change the logfile
        uniqueList(seq) #return a list containing only one instance of each element in seq
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
    __path = os.path.split(__file__)[0]
    __log = True
    __logfile = os.path.join(__path, 'newsstandDB.log')
    __dataStructure = (('Provider','TEXT'),('Provider Country','TEXT'),('SKU','TEXT'),
                       ('Developer','TEXT'),('Title','TEXT'),('Version','TEXT'),
                       ('Product Type Identifier','TEXT'),('Units','INTEGER'),
                       ('Developer Proceeds','REAL'),('Customer Currency','TEXT'),
                       ('Country Code','TEXT'),('Currency of Proceeds','TEXT'),
                       ('Apple Identifier','TEXT'),('Customer Price','REAL'),
                       ('Promo Code','TEXT'),('Parent Identifier','TEXT'),
                       ('Subscription','TEXT'),('Period','TEXT'),('Download Date (PST)','TEXT'),
                       (' Customer Identifier','TEXT'),('Report Date (Local)','TEXT'),
                       ('Sales/Return','TEXT'),('Category','TEXT'),('USDproceeds','REAL'))
    __fileStructure = (('filename','TEXT'),('hash','TEXT'))
    __statsStructure = (('Date','TEXT'),('UniqueUsers','INTEGER'),('PayingUsers','INTEGER'),
                        ('Conversion','REAL'),('TotalProceeds','REAL'),('ProceedsPerUser','REAL'),
                        ('CLV','REAL'),('CurrentSubscribers','INTEGER'))
    __monthProceedsStructure = (('Month','TEXT'),('Proceeds','REAL'))
    __optinStructure = (('First Name','TEXT'),('Last Name','TEXT'),('Email Address','TEXT'),
                        ('Postal Code','TEXT'),('Apple Identifier','TEXT'),
                        ('Report Start Date','TEXT'),('Report End Date','TEXT'))
    
    __dbFilename = ''
    
    __uniqueUsers = 0
    __payingUsers = 0
    __conversion = 0
    __totalProceeds = 0
    __proceedsPerUser = 0
    __clv = 0
    __currentSubscribers = 0
    
    def __init__(self, dbPath='newsstandDB.sql',absolutePath=False):
        '''init: Connect to the database and initialize variables'''
        #Connect to the database
        if not absolutePath:
            realFilename = os.path.join(self.__path, dbPath)
        else:
            realFilename = dbPath
        self.__dbFilename = realFilename
        assert self.__dbFilename
        self.conn = sql.connect(self.__dbFilename)
        self.cur = self.conn.cursor()
        print 'Connected to the database'
        
    def __del__(self):
        '''del: Try to shutdown as cleanly as possible. Close the database connection and open file handles'''
        self.conn.close()
    
    def log(self,msg):
        '''log(msg): Write msg to the log'''
        if self.__log:
            try:
                with open(self.__logfile,'a') as fp:
                    fp.write(time.asctime()+': '+msg+'\n')
            except IOError:
                print 'Unable to write to logfile %s' % self.__logfile
    
    def setLog(self,log,logfile=None):
        '''setLog(log): Set the logging on or off. (Optional) Change the logfile'''
        if log:
            self.__log = True
        else:
            self.__log = False
        if logfile:
            self.__logfile = logfile
            
    def uniqueList(self, seq):
        '''uniqueList(seq): return a list containing only one instance of each element in seq'''
        seen = set()
        return [ x for x in seq if x not in seen and not seen.add(x)]
    
    def calculateUniqueUsers(self):
        '''calculateUniqueUsers(): calculate the amount of people who downloaded the app (unique)'''
        pass
    
    def calculatePayingUsers(self):
        '''calculatePayingUsers(): calculate the amount of people who made a purchase'''
        pass
    
    def calculateConversion(self,users,payingUsers):
        '''calculateConversion(users,payingUsers): calculate the ratio between people who 
        download the app and people who make a purchase'''
        return payingUsers/float(users)
    
    def calculateTotalProceeds(self):
        '''calculateTotalProceeds(): calculate the total revenue'''
        pass
    
    def calculateProceedsPerUser(self,proceeds,users):
        '''calculateProceedsPerUser(proceeds,users): calclulate the ratio between proceeds 
        and total downloads (unique)'''
        return proceeds/float(users)
    
    def calculateCLV(self,proceeds,payingUsers):
        '''calculateCLV(proceeds,payingUsers): calculate the customer lifetime value 
        (ratio between total paying usrs and proceeds)'''
        return proceeds/float(payingUsers)
    
    def calculateCurrentSubscribers(self):
        '''calculateCurrentSubscribers(): calculate the amount of subscribers active in 
        the past 30 days'''
        pass
    
    def createDB(self): 
        '''createDB(): Creates the DB tables (DB file itself is created at __init__)'''
        pass
    
    def removeDB(self): 
        '''removeDB(): Deletes the DB file'''
        os.remove(self.__dbFilename)
        pass
    
    def importData(self,filename): 
        '''importData(filename): imports CSV file into the data table'''
        pass
    
    def importOptin(self,filename): 
        '''importOptin(filename): imports the optin file into the optin table'''
        pass
    
    def buildStats(self): #Analyzes the data and updates the stats table
        self.__uniqueUsers = self.calculateUniqueUsers()
        self.__payingUsers = self.calculatePayingUsers()
        self.__conversion = self.calculateConversion(self.__uniqueUsers,self.__payingUsers)
        self.__totalProceeds = self.calculateTotalProceeds()
        self.__proceedsPerUser = self.calculateProceedsPerUser(self.__totalProceeds,
                                                               self.__uniqueUsers)
        self.__clv = self.calculateCLV(self.__totalProceeds, self.__payingUsers)
        self.__currentSubscribers = self.calculateCurrentSubscribers()
        
    def writeStats(self): 
        '''writeStats(): Writes the stats into the stats table'''
        pass
        