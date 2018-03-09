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
class SeleniumTestsSprint2(StaticLiveServerTestCase):

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

class SeleniumTestsSprint3(StaticLiveServerTestCase):

    def setUp(self):
        # Usar fixture para tener datos en la db
        call_command('loaddata', 'fixtures/db.json', verbosity=0)

        self.driver = webdriver.Firefox()
        self.driver.get('%s' % (self.live_server_url))

        # Admin login
        self.login_button = self.driver.find_element_by_css_selector("input[type='submit']")
        self.username = self.driver.find_element_by_css_selector("input[name='username']")
        self.password = self.driver.find_element_by_css_selector("input[name='password']")
        self.username.send_keys("Farmaceuta1")
        self.password.send_keys("1234")
        self.login_button.click()

        time.sleep(1)

    def tearDown(self):
        self.driver.close()

    def open(self, url):
        self.driver.get("%s%s" % (self.live_server_url, url))

######################### SPRINT 3 ##############################
#@unittest.skip("Verificada Sprint 3")
class TestAgregarMedicamento(SeleniumTestsSprint3):
    def runTest(self):

        self.driver.find_element_by_css_selector("i.fa-stethoscope").click()
        time.sleep(1)
        self.driver.find_element_by_css_selector("i.fa-search").click()
        time.sleep(1)
        self.driver.find_element_by_css_selector("i.fa-plus-circle").click()

        self.driver.find_element_by_css_selector("input[name='nombre']").send_keys(u"Medicamento 1")
        self.driver.find_element_by_css_selector("textarea[name='indicacion']").send_keys(u"Indicacion Medicamento 1")
        self.driver.find_element_by_css_selector("textarea[name='posologia']").send_keys(u"Posologia Medicamento 1")
        Select(self.driver.find_element_by_css_selector("select[name='tipo']")).select_by_visible_text(u"Jarabe")
        Select(self.driver.find_element_by_css_selector("select[name='marca']")).select_by_visible_text(u"Lab1")

        time.sleep(1)
        self.driver.find_element_by_css_selector("button[type='submit']").click()

        self.assertTrue(u"Medicamento 1" in self.driver.page_source)

@unittest.skip("Verificada Sprint 3")
class TestBuscarMedicamento(SeleniumTestsSprint3):
    def runTest(self):
        # Agregar el medicamento a buscar
        self.driver.find_element_by_css_selector("i.fa-stethoscope").click()
        self.driver.find_element_by_css_selector("i.fa-search").click()
        self.driver.find_element_by_css_selector("i.fa-plus-circle").click()
        self.driver.find_element_by_css_selector("input[name='nombre']").send_keys(u"Medicamento 1")
        self.driver.find_element_by_css_selector("textarea[name='indicacion']").send_keys(u"Indicacion Medicamento 1")
        self.driver.find_element_by_css_selector("textarea[name='posologia']").send_keys(u"Posologia Medicamento 1")
        Select(self.driver.find_element_by_css_selector("select[name='tipo']")).select_by_visible_text(u"Jarabe")
        Select(self.driver.find_element_by_css_selector("select[name='marca']")).select_by_visible_text(u"Lab1")
        self.driver.find_element_by_css_selector("button[type='submit']").click()

        # Buscar el medicamento
        self.driver.find_element_by_css_selector("input[type='search'").send_keys(u"Medicamento 1")
        time.sleep(1)
        self.assertTrue(u"Medicamento 1" in self.driver.page_source)

#@unittest.skip("Verificada Sprint 3")
class TestModificarMedicamento(SeleniumTestsSprint3):
    def runTest(self):

        # Agregar el medicamento a eliminar
        self.driver.find_element_by_css_selector("i.fa-stethoscope").click()
        self.driver.find_element_by_css_selector("i.fa-search").click()
        self.driver.find_element_by_css_selector("i.fa-plus-circle").click()
        self.driver.find_element_by_css_selector("input[name='nombre']").send_keys(u"Medicamento 1")
        self.driver.find_element_by_css_selector("textarea[name='indicacion']").send_keys(u"Indicacion Medicamento 1")
        self.driver.find_element_by_css_selector("textarea[name='posologia']").send_keys(u"Posologia Medicamento 1")
        Select(self.driver.find_element_by_css_selector("select[name='tipo']")).select_by_visible_text(u"Jarabe")
        Select(self.driver.find_element_by_css_selector("select[name='marca']")).select_by_visible_text(u"Lab1")
        self.driver.find_element_by_css_selector("button[type='submit']").click()

        # Modificar el medicamento
        self.driver.find_element_by_css_selector("i.fa-stethoscope").click()
        self.driver.find_element_by_css_selector("i.fa-search").click()
        time.sleep(1)
        self.driver.find_element_by_css_selector("i.fa-pencil").click()
        self.driver.find_element_by_css_selector("input[name='nombre']").clear()
        self.driver.find_element_by_css_selector("input[name='nombre']").send_keys(u"Editado Medicamento 1")
        time.sleep(1)
        self.driver.find_element_by_css_selector("button[type='submit']").click()
        
        self.assertTrue(u"Editado Medicamento 1" in self.driver.page_source)

@unittest.skip("Verificada Sprint 3")
class TestEliminarMedicamento(SeleniumTestsSprint3):
    def runTest(self):

        # Agregar el medicamento a eliminar
        self.driver.find_element_by_css_selector("i.fa-stethoscope").click()
        self.driver.find_element_by_css_selector("i.fa-search").click()
        self.driver.find_element_by_css_selector("i.fa-plus-circle").click()
        self.driver.find_element_by_css_selector("input[name='nombre']").send_keys(u"Medicamento 1")
        self.driver.find_element_by_css_selector("textarea[name='indicacion']").send_keys(u"Indicacion Medicamento 1")
        self.driver.find_element_by_css_selector("textarea[name='posologia']").send_keys(u"Posologia Medicamento 1")
        Select(self.driver.find_element_by_css_selector("select[name='tipo']")).select_by_visible_text(u"Jarabe")
        self.driver.find_element_by_css_selector("input[name='marca']").send_keys(u"Marca Medicamento 1")
        self.driver.find_element_by_css_selector("button[type='submit']").click()

        # Eliminar el medicamento
        self.driver.find_element_by_css_selector("i.fa-stethoscope").click()
        time.sleep(1)
        self.driver.find_element_by_css_selector("i.fa-search").click()
        time.sleep(1)
        self.driver.find_element_by_css_selector("i.fa-trash").click()
        self.driver.find_element_by_css_selector("a.btn-primary").click()

        self.assertTrue(u"Medicamento 1" not in self.driver.page_source)

#################################################################

######################### SPRINT 2 ##############################
@unittest.skip("Verificada Sprint 2")
class TestBuscarInstituciones(SeleniumTestsSprint2):
    def runTest(self):
        self.open(reverse('ver_farmacias'))
        time.sleep(1)
        self.assertTrue(u"Gestión de Instituciones Farmacéuticas" in self.driver.page_source)

@unittest.skip("Verificada Sprint 2")
class TestAgregarInstituciones(SeleniumTestsSprint2):
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

@unittest.skip("Verificada Sprint 2")
class TestModificarInstituciones(SeleniumTestsSprint2):
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

@unittest.skip("Verificada Sprint 2")
class TestEliminarInstituciones(SeleniumTestsSprint2):
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

################################################################
if __name__ == '__main__':
    unittest.main()
