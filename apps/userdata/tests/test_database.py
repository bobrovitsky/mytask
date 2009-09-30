''' test case for userdata database '''
from tddspry.django import DatabaseTestCase
from apps.userdata.models import Profile

FIRSTNAME = 'john'
LASTNAME = 'smith'
ADDRESS = 'test address'
DESCRIPTION = 'some description about john smith'
BIRTHDAY = '1970-01-01'


class TestProfile(DatabaseTestCase):
    ''' userdata database test '''

    def _create_record(self):
        ''' create single record '''
        return self.assert_create(Profile, first_name=FIRSTNAME,
            last_name=LASTNAME, address=ADDRESS, description=DESCRIPTION,
            birthday=BIRTHDAY)

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
        self.assert_read(Profile, first_name=FIRSTNAME,
            last_name=LASTNAME)

    def test_update(self):
        ''' update test '''
        record = self._create_record()
        self.assert_update(record, first_name='mike')
