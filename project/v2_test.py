#!python3

from call_routing_v2 import CallRoutes
import unittest
import os, pathlib

# Python 2 and 3 compatibility: unittest module renamed this assertion method
# if not hasattr(unittest.TestCase, 'assertCountEqual'):
#     unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual

class RoutingTest(unittest.TestCase):
    def test_init(self):
        c = CallRoutes()
        assert c.routes == {} # make sure its an empty dict

    def test_update_routes(self):
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

        c.update_routes("data/route-costs-100.txt")
        assert c.routes["+449275049"] == "0.49" # line 2
        assert c.routes["+4982121410"] == "0.46" # line 20
        assert c.routes["+1941672"] == "0.04" # line 30
        assert c.routes["+1888"] == "0.05"# line 40
        assert c.routes["+1432323"] == "0.03" # line 50
        assert c.routes["+82417093"] == "0.55" # line 60

        c.output_number_costs("data/phone-numbers-test.txt")
        """
        input: txt file with phone numbers without cost
        output: new txt file with phone numbers with cost
        
        tests that the phone nubmers from phone-numbers-test
        updated to prefix dictionary
        """
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
        c = CallRoutes("data/route-costs-600.txt", "data/route-costs-100.txt")
        c.output_number_costs("data/phone-numbers-test.txt")
        # tests file exists
        assert os.path.exists("data/number-costs.txt") is True
        # tests how long file is
        route_line_count = sum(1 for line in open("data/phone-numbers-test.txt"))
        number_line_count = sum(1 for line in open("data/number-costs.txt"))
        assert route_line_count == number_line_count


