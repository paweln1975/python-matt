#!/usr/bin/env python3

# Reference:
# https://python3.info/testing/unittest/testcase.html

#%% Unittest TestCase
# https://martinfowler.com/articles/microservice-testing/#testing-component-out-of-process-diagram
# https://docs.python.org/3/library/unittest.mock.html



#%% Glossary



#%% Running tests with your IDE
# View menu -> Run... -> Unittest in myfunction



#%% From code



#%% From command line



#%% Methods
# self.assertEqual()
# self.assertAlmostEqual(0.1+0.2, 0.3, places=16)
# self.assertTrue()
# self.assertFalse()
# self.assertDictEqual()
# self.assertIn()
# self.assertIs()
# self.assertIsInstance()
# self.assertIsNotNone()
# self.assertRaises()



#%% Mock
# Mock and MagicMock objects create all attributes and methods as you access them and store details of how they have been used.



#%% Side effect
# Raising an exception when a mock is called



#%% patch
# The object you specify will be replaced with a mock (or other object) during the test and restored when the test ends



#%% Stub
# writing classes or functions but not yet implementing them
# After you have planned a module or class, for example by drawing it's UML diagram, you begin implementing it.
# As you may have to implement a lot of methods and classes, you begin with stubs.
# This simply means that you only write the definition of a function down and leave the actual code for later.