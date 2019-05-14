#!python

from call_routing_v2 import CallRoutes
import unittest

# Python 2 and 3 compatibility: unittest module renamed this assertion method
if not hasattr(unittest.TestCase, 'assertCountEqual'):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual

class RoutingTest(unittest.TestCase):
    def test_init(self):
        pass

    def test_iter_and_generator(self):
        pass
    
    def test_print_routes(self):
        pass

    def test_split_prefixes(self):
        pass

    def test_call_cost(self):
        pass
    
    def output_number_costs(self):
        pass
