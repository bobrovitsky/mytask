''' test case for modellog database '''
from tddspry.django import DatabaseTestCase
from apps.modellog.models import ModelLog

MODEL = 'ModelLog'
OBJECT = 'object'
ACTION = 1


class TestModelLog(DatabaseTestCase):
    ''' modellog database test '''

    def _create_record(self):
        ''' create single record '''
        return self.assert_create(ModelLog, model_name=MODEL,
            object=OBJECT, action=ACTION)

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
        self.assert_read(ModelLog, model_name=MODEL)

    def test_update(self):
        ''' update test '''
        record = self._create_record()
        self.assert_update(record, object='new_test_object')
