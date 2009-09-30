''' http test for userdata '''
from tddspry.django import HttpTestCase, DatabaseTestCase
from tddspry.django.helpers import USERNAME, PASSWORD
from django.conf import settings
from django.core.urlresolvers import reverse
from apps.userdata.models import Profile
from apps.userdata.widgets import DatePicker
from apps.userdata.tests.test_database import \
    FIRSTNAME, LASTNAME, ADDRESS, DESCRIPTION, BIRTHDAY

NEW_FIRSTNAME = 'new_firstname'
NEW_LASTNAME = 'new_lastname'


class TestProfile(HttpTestCase, DatabaseTestCase):
    ''' run http tests '''

    def _make_login(self):
        ''' just login user '''
        self.helper('create_user')
        self.login(USERNAME, PASSWORD, url=reverse('login'))

    def _create_profile(self):
        ''' create profile '''
        return self.assert_create(Profile, first_name=FIRSTNAME,
            last_name=LASTNAME, address=ADDRESS, description=DESCRIPTION,
            birthday=BIRTHDAY)

    def test_index_page(self):
        ''' test if profile_list page available '''
        self._make_login()
        self.go200(reverse('profile_list'))
        self.url(reverse('profile_list'))
        self.find('<title>profiles</title>')

    def test_profile_edit_page(self):
        ''' test if profile_edit page available '''
        self._make_login()
        profile = self._create_profile()
        self.go200(reverse('profile_edit', kwargs={'pid': profile.pk}))
        self.url(profile.get_absolute_url())
        self.find(DESCRIPTION)

    def test_edit_profile(self):
        ''' test edit profile '''
        self._make_login()
        profile = self._create_profile()
        self.go200(reverse('profile_edit', kwargs={'pid': profile.pk}))
        self.url(profile.get_absolute_url())

        self.formvalue(1, 'id_first_name', NEW_FIRSTNAME)
        self.formvalue(1, 'id_last_name', NEW_LASTNAME)
        self.submit200()

        self.find(NEW_FIRSTNAME)
        self.find(NEW_LASTNAME)

    def test_logout(self):
        ''' test logout '''
        self._make_login()
        self.logout(url=reverse('logout'))
        self.go200(reverse('profile_list'))
        self.url(reverse('login'))
