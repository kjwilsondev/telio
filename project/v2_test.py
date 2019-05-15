#!python3

from call_routing_v2 import CallRoutes
import unittest

# Python 2 and 3 compatibility: unittest module renamed this assertion method
# if not hasattr(unittest.TestCase, 'assertCountEqual'):
#     unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual

class RoutingTest(unittest.TestCase):
    def test_init(self):
        c = CallRoutes()
        assert c.routes == {} # make sure its an empty dict

    def test_split_prefixes(self):
        c = CallRoutes("data/route-costs-600.txt")
        assert c.routes["+82338123"] == "0.79"
        assert c.routes["+861694484"] == "0.94"
        assert c.routes["+1329888"] == "0.06"
        assert c.routes["+861533676"] == "0.69"
        assert c.routes["+82333797"] == "0.79"
        assert c.routes["+34714334"] == "0.42"
        assert c.routes["+1713334"] == "0.06"
        assert c.routes["+492059"] == "0.37"
        assert c.routes["+8241"] == "0.62"
        assert c.routes["+1656665"] == "0.10"
        assert c.routes["+449326404"] == "0.37"

    def test_call_cost(self):
        c = CallRoutes("data/route-costs-600.txt")
        assert c.call_cost("+8233812322") == "0.79"
        assert c.call_cost("+8616944844") == "0.94"
        assert c.call_cost("+1329888783") == "0.06"
        assert c.call_cost("+8615336766") == "0.69"
        assert c.call_cost("+8233379775") == "0.79"
        assert c.call_cost("+3471433443") == "0.42"
        assert c.call_cost("+1713334753") == "0.06"
        assert c.call_cost("+8233812322") == "0.79"

    def test_output_number_costs(self):
        """
        checks if new routes were added
        """
        c = CallRoutes("data/route-costs-600.txt", "data/route-costs-100.txt")
        c.output_number_costs("data/phone-numbers-test.txt")
        assert c.routes["+14326228140"] == "0.03"
        assert c.routes["+14326228158"] == "0.03"
        assert c.routes["+14324751325"] == "0.03"
        assert c.routes["+14328611917"] == "0.03"
        assert c.routes["+14322617591"] == "0.03"
        assert c.routes["+14322611331"] == "0.03"
        assert c.routes["+14327289105"] == "0.03"
        assert c.routes["+14326809107"] == "0.03"
        assert c.routes["+14324133948"] == "0.03"
        assert c.routes["+14323815283"] == "0.03"
