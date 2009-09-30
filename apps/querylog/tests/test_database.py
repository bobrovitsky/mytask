''' test case for querylog database '''
from tddspry.django import DatabaseTestCase
from apps.modellog.models import QueryLog
from django.conf import settings

SQL = 'select count(*) from querylog_querylog'
TIME = 0.0


class TestQueryLog(DatabaseTestCase):
    ''' querylog database test '''

    def _create_record(self):
        return self.assert_create(QueryLog, sql=SQL, time=TIME)

    def test_debug_mode(self):
        ''' test if debug=True otherwise connection.queries will be empty '''
        self.assert_equals(settings.DEBUG, True)

    def test_create(self):
        ''' create record test '''
        self._create_record()

    def test_delete(self):
        ''' delete record test '''
        record = self._create_record()
        self.assert_delete(record)

    def test_read(self):
        ''' test if record exists '''
        self._create_record()
        self.assert_read(QueryLog, sql=SQL)

    def test_update(self):
        ''' update test '''
        record = self._create_record()
        self.assert_update(record, sql='select NOW')
