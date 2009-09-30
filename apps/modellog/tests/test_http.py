''' http test for modellog '''
from tddspry.django import HttpTestCase
from tddspry.django.helpers import USERNAME, PASSWORD
from django.conf import settings
from django.core.urlresolvers import reverse


class TestModelLog(HttpTestCase):
    ''' run http tests '''

    def test_modellog_page(self):
        ''' test if modellog page available '''
        user = self.helper('create_user')
        self.login(USERNAME, PASSWORD, url=reverse('login'))
        self.go200(reverse('modellog_list'))
        self.url(reverse('modellog_list'))
        self.find('<title>modellog</title>')
