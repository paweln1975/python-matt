from datetime import date
from unittest.mock import patch
from django.test import TestCase
from shop.models import Customer, Email, EmailType


class CustomerCreateTest(TestCase):
    def test_customer_with_firstname_and_lastname(self):
        customer = Customer.objects.create(firstname='Mark', lastname='Watney')
        self.assertEqual(customer.firstname, 'Mark')
        self.assertEqual(customer.lastname, 'Watney')

    def test_customer_with_birthdate(self):
        customer = Customer.objects.create(firstname='Mark', lastname='Watney', birthdate=date(2000, 1, 2))
        self.assertEqual(customer.birthdate, date(2000, 1, 2))


class CustomerFunctionalityTest(TestCase):
    # fixtures = ['customer.json']

    def setUp(self):
        self.customer = Customer.objects.create(firstname='Mark', lastname='Watney')
        self.email1 = Email.objects.create(customer=self.customer, type=EmailType.WORK, address='mwatney@nasa.gov')
        self.email2 = Email.objects.create(customer=self.customer, type=EmailType.HOME, address='mwatney@gmail.com')

    def test_customer_emails(self):
        self.assertEqual(self.customer.emails.count(), 2)
        self.assertListEqual(list(self.customer.emails), [self.email1, self.email2])

    def test_customer_name(self):
        self.assertEqual(self.customer.name, 'Mark Watney')

    def test_customer_str(self):
        self.assertEqual(str(self.customer), 'Mark Watney')

    def test_customer_age_hardcoded(self):
        self.customer.birthdate = date(2000, 1, 2)
        self.assertEqual(self.customer.age, 24)

    def test_customer_age_patch(self):
        self.customer.birthdate = date(2000, 1, 2)
        with patch('shop.models.customer.date') as d:
            d.today.return_value = date(2024, 1, 2)
            age = self.customer.age
        self.assertEqual(age, 24)