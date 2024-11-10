#!/usr/bin/env python3

# Reference:
# https://python3.info/django/tests/about.html

#%% Tests About
# django.test.TestCase
# All Django tests run always with DEBUG=False
# https://docs.djangoproject.com/en/stable/topics/testing/overview/



#%% Structure



#%% Types
# SimpleTestCase - no database interaction
# TestCase - database interaction
# TransactionTestCase - wraps each test in a transaction
# LiveServerTestCase - runs a live server in the background
# StaticLiveServerTestCase - runs a live server in the background with static files



#%% TestCase



#%% Python Assertions
# assertEqual(a, b) - checks that a == b
# assertNotEqual(a, b) - checks that a != b
# assertTrue(x) - checks that bool(x) is True
# assertFalse(x) - checks that bool(x) is False
# assertIs(a, b) - checks that a is b
# assertIsNot(a, b) - checks that a is not b
# assertIsNone(x) - checks that x is None
# assertIsNotNone(x) - checks that x is not None
# assertIn(a, b) - checks that a in b
# assertNotIn(a, b) - checks that a not in b
# assertIsInstance(a, b) - checks that isinstance(a, b)
# assertNotIsInstance(a, b) - checks that not isinstance(a, b)



#%% Django Assertions
# assertTemplateUsed(response, filename)