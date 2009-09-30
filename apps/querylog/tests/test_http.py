''' http test for querylog '''
from tddspry.django import HttpTestCase
from tddspry.django.helpers import USERNAME, PASSWORD
from django.conf import settings
from django.core.urlresolvers import reverse


class TestQueryLog(HttpTestCase):
    ''' run http tests '''

    def test_querylog_page(self):
        ''' test if querylog page available '''
        user = self.helper('create_user')
        self.login(USERNAME, PASSWORD, url=reverse('login'))
        self.go200(reverse('querylog_list'))
        self.url(reverse('querylog_list'))
        self.find('<title>querylog</title>')
