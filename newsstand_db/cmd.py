from newsstand_db import newsstandDB as ndb
from glob import glob


def newsstanddb_create(filename):
    try:
        db = ndb(filename)
        db.createDB()
    except IOError:
        print 'Unable to createDB'
        
def newsstanddb_import(*args):
    try:
        db = ndb(newsstanddb_getdbfile())
    except IOError:
        print 'Couldn\'nt connect to DB'
        
    for arg in args:
#         print arg #Debug
        try:
            db.importData(arg)
        except IOError:
            print 'File %s does not exist' % arg
        except:
            try:
                db.importOptin(arg)
            except:
                print 'Unknown error in import'
                raise

def newsstanddb_autoupdate(basedir='.',pattern=('N_D_W*','O_S_W*'),outputFile='stats.md'):
    for pat in pattern:
        files = glob('/'.join([basedir,pat]))
#         print files #Debug
        newsstanddb_import(*files)
        
    try:
        db = ndb(newsstanddb_getdbfile())
    except IOError:
        print 'Couldn\'nt connect to DB'
    
    db.buildStats()
    db.writeStats()
    db.outputStats('/'.join([basedir,outputFile]))

def newsstanddb_getdbfile():
    return 'test.sql'