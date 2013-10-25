from unittest import TestCase

from newsstand_db import newsstandDB as ndb

class TestCreate(TestCase):
    def test_is_ndb(self):
        s = ndb()
        self.assertTrue(isinstance(s, ndb))