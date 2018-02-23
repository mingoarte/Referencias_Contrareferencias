# -*- coding: utf-8 -*-
import unittest
from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.core.urlresolvers import reverse
from django.core.management import call_command
import unittest, time, re

# run: ./manage.py test administador
class SeleniumTests(StaticLiveServerTestCase):

    def setUp(self):
        # Usar fixture para tener datos en la db
        call_command('loaddata', 'fixtures/db.json', verbosity=0)

        self.driver = webdriver.Firefox()
        self.driver.get('%s' % (self.live_server_url))

        # Admin login
        self.login_button = self.driver.find_element_by_css_selector("input[type='submit']")
        self.username = self.driver.find_element_by_css_selector("input[name='username']")
        self.password = self.driver.find_element_by_css_selector("input[name='password']")
        self.username.send_keys("admin")
        self.password.send_keys("admin")
        self.login_button.send_keys(Keys.RETURN)

        time.sleep(1)

    def tearDown(self):
        self.driver.close()

    def open(self, url):
        self.driver.get("%s%s" % (self.live_server_url, url))

class TestBuscarInstituciones(SeleniumTests):
    def runTest(self):
        self.open(reverse('ver_instituciones'))
        self.assertTrue(u"Gestión de Instituciones" in self.driver.page_source)

@unittest.skip("Verificada")
class TestAgregarInstituciones(SeleniumTests):
    def runTest(self):
        self.open(reverse('agregar_institucion'))

@unittest.skip("Verificada")
class TestModificarInstituciones(SeleniumTests):
    def runTest(self):
        self.open(reverse('modificar_institucion'))

@unittest.skip("Verificada")
class TestEliminarInstituciones(SeleniumTests):
    def runTest(self):
        self.open(reverse('eliminar_institucion'))

if __name__ == '__main__':
    unittest.main()