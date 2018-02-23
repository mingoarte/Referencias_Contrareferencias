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
from django.contrib.contenttypes.models import ContentType

# run: ./manage.py test farmaceuta
class SeleniumTests(StaticLiveServerTestCase):

    def setUp(self):
        # Usar fixture para tener datos en la db
        #call_command("flush", verbosity=0, interactive=False)
        call_command('loaddata', 'fixtures/db.json', verbosity=0)

        self.driver = webdriver.Firefox()
        self.driver.get('%s' % (self.live_server_url))

        # Admin login
        self.login_button = self.driver.find_element_by_css_selector("input[type='submit']")
        self.username = self.driver.find_element_by_css_selector("input[name='username']")
        self.password = self.driver.find_element_by_css_selector("input[name='password']")
        self.username.send_keys("admin")
        self.password.send_keys("admin")
        self.login_button.click()

        time.sleep(1)

    def tearDown(self):
        self.driver.close()

    def open(self, url):
        self.driver.get("%s%s" % (self.live_server_url, url))

class TestBuscarInstituciones(SeleniumTests):
    def runTest(self):
        self.open(reverse('ver_farmacias'))
        self.assertTrue(u"Gestión de Farmacias" in self.driver.page_source)

class TestAgregarInstituciones(SeleniumTests):
    def runTest(self):
        self.open(reverse('agregar_farmacia'))
        time.sleep(1)
        self.rif = self.driver.find_element_by_css_selector("input[name='rif']")
        self.nombre = self.driver.find_element_by_css_selector("input[name='nombre']")
        self.direccion = self.driver.find_element_by_css_selector("input[name='direccion']")
        self.institucion = self.driver.find_element_by_css_selector("select[name='institucion']")

        self.rif.send_keys(u"1234567")
        self.nombre.send_keys(u"Farmacia 1")
        self.direccion.send_keys(u"Dirección Farmcia 1")
        Select(self.institucion).select_by_visible_text(u"Hospital1")
        self.driver.find_element_by_css_selector("button[type='submit']").click()
        self.assertTrue(u"Farmacia 1" in self.driver.page_source)

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