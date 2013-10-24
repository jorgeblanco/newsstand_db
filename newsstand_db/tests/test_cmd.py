from unittest import TestCase

from newsstand_db.cmd import newsstanddb_create


class TestCmd(TestCase):
    def test_basic(self):
        newsstanddb_create()