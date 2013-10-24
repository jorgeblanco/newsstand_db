from unittest import TestCase

import newsstand_db as ndb

class TestCreate(TestCase):
    def test_is_string(self):
        s = ndb.create()
        self.assertTrue(isinstance(s, newsstand_db))