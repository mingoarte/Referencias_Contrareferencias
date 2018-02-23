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

#@unittest.skip("Verificada")
class TestBuscarInstituciones(SeleniumTests):
    def runTest(self):
        self.open(reverse('ver_farmacias'))
        time.sleep(1)
        self.assertTrue(u"Gestión de Instituciones Farmacéuticas" in self.driver.page_source)

#@unittest.skip("Verificada")
class TestAgregarInstituciones(SeleniumTests):
    def runTest(self):
        self.open(reverse('agregar_farmacia'))
        time.sleep(1)
        self.rif = self.driver.find_element_by_css_selector("input[name='rif']")
        self.nombre = self.driver.find_element_by_css_selector("input[name='nombre']")
        self.direccion = self.driver.find_element_by_css_selector("input[name='direccion']")
        self.institucion = self.driver.find_element_by_css_selector("select[name='institucion']")
        self.farmaceuta = self.driver.find_element_by_css_selector("select[name='farmaceuta']")

        self.rif.send_keys(u"1234567")
        self.nombre.send_keys(u"Farmacia1")
        self.direccion.send_keys(u"Dirección Farmcia1")
        Select(self.institucion).select_by_visible_text(u"Hospital1")
        Select(self.farmaceuta).select_by_visible_text(u"2121244 medico medico")
        self.driver.find_element_by_css_selector("button[type='submit']").click()
        self.assertTrue(u"Farmacia1" in self.driver.page_source)

#@unittest.skip("Verificada")
class TestModificarInstituciones(SeleniumTests):
    def runTest(self):
        self.open(reverse('agregar_farmacia'))
        time.sleep(1)
        self.rif = self.driver.find_element_by_css_selector("input[name='rif']")
        self.nombre = self.driver.find_element_by_css_selector("input[name='nombre']")
        self.direccion = self.driver.find_element_by_css_selector("input[name='direccion']")
        self.institucion = self.driver.find_element_by_css_selector("select[name='institucion']")
        self.farmaceuta = self.driver.find_element_by_css_selector("select[name='farmaceuta']")

        self.rif.send_keys(u"1234567")
        self.nombre.send_keys(u"Farmacia1")
        self.direccion.send_keys(u"Dirección Farmacia1")
        Select(self.institucion).select_by_visible_text(u"Hospital1")
        Select(self.farmaceuta).select_by_visible_text(u"2121244 medico medico")
        self.driver.find_element_by_css_selector("button[type='submit']").click()

        self.driver.find_element_by_css_selector("i.fa-pencil").click()
        time.sleep(1)
        self.direccion = self.driver.find_element_by_css_selector("input[name='direccion']").clear()
        self.direccion = self.driver.find_element_by_css_selector("input[name='direccion']")
        self.direccion.send_keys(u"Farmacia1Modif")
        self.driver.find_element_by_css_selector("button[type='submit']").click()
        
        self.assertTrue(u"Farmacia1Modif" in self.driver.page_source)

#@unittest.skip("Verificada")
class TestEliminarInstituciones(SeleniumTests):
    def runTest(self):
        self.open(reverse('agregar_farmacia'))
        time.sleep(1)
        self.rif = self.driver.find_element_by_css_selector("input[name='rif']")
        self.nombre = self.driver.find_element_by_css_selector("input[name='nombre']")
        self.direccion = self.driver.find_element_by_css_selector("input[name='direccion']")
        self.institucion = self.driver.find_element_by_css_selector("select[name='institucion']")
        self.farmaceuta = self.driver.find_element_by_css_selector("select[name='farmaceuta']")

        self.rif.send_keys(u"1234567")
        self.nombre.send_keys(u"Farmacia1")
        self.direccion.send_keys(u"Dirección Farmacia1")
        Select(self.institucion).select_by_visible_text(u"Hospital1")
        Select(self.farmaceuta).select_by_visible_text(u"2121244 medico medico")
        self.driver.find_element_by_css_selector("button[type='submit']").click()
        time.sleep(1)

        self.driver.find_element_by_css_selector("i.fa-trash").click()
        self.driver.find_element_by_css_selector("a.btn-primary").click()

        self.assertTrue(u"Farmacia1" not in self.driver.page_source)

if __name__ == '__main__':
    unittest.main()