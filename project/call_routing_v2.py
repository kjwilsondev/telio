#python3

"""
This module produces call pricing from multiple carriers. In order provide pricing
class must be initialized with any number of route pages as parameters. Pages are
converted into a dictionary format for speed and ease of phone number checking. 

Routes can also be interated through and printed in sorted order for manual checking 
as needed.

Once routes have been added to class, one can call the `output_number_costs()` function
to write costs for a file of phone numbers to a text file and return that text file. 

**Functions:**

`print_routes`: simply prints all routes stored in CallRoutes.routes property in sorted
                order. This is useful because routes are stored in an unordered dictionary 
                object. 

`call_cost`:    Normally only called through the `output_number_costs` function, this 
                function checks the CallRoutes.routes property for the cost, outputting 
                the most inexpensive cost.
                
`output_number_costs`: This function takes in a list of phone number files and calls
                `call_cost` on them. It then packages the phone numbers and their costs
                and writes them to a text file. We also return the text file for ease of 
                use (i.e. for printing) by the user.

Improves on v1 by handling multiple pages of route costs and multiple pages of phone numbers.
Also writes output to a file as well as returning file so that user can access the information
either way. 

There is also testing for most functions and code is well documented. Memory and time complexities
for all functions are annotated and actual memory and time usage is logged and output to terminal. 

Currently adding a function to handle multiple costs for identical routes. 

Potential Improvements: 
- create a web-service API to allow clients to price a call before it is initiated
- create an efficient route cost lookup solution that can handle high spikes of traffic 
(up to 10,000 requests per minute) without overloading servers
- allow changes to a subset of the route cost data while the pricing web API remains 
operational 
"""

import os
import time
import resource
import platform
import pathlib

class CallRoutes(object):
    def __init__(self, *route_pages):
        """
        Initialize all route pages and store routes and costs in self.routes, a dictionary.

        --

        Time complexity: O(n) where n is the number of route costs because we have to copy
        each route over into a dictionary.
        Space complexity: O(n) because we create a dictionary to handle all route costs and
        store them all in memory.
        """
        self.routes = {}

        # input : route page text files
        # output: dictiorary of key: prefixes, value: costs
        for route_page in route_pages:
            route_holder = self.split_prefixes(route_page)
            # set update method
            self.routes.update(route_holder) # O(len(n))
        # print("ROUTES",self.routes)

    def __iter__(self):
        """
        Allows interation through all items in self.routes. 

        -- 

        Time complexity: O(n) where n is the number of items in the self.routes. 
        Space complexity: O(1) no new structures are created or stored in memory.
        """
        return self._generator()

    def _generator(self):
        """
        returns items in set
        -- 

        Time complexity: O(n) where n is the number of items in the self.routes. 
        Space complexity: O(1) no new structures are created or stored in memory.
        """
        for item in self.routes.items():
            yield item
    
    def print_routes(self, want=None):
        """
        Sorts all items in self.routes, and returns them as a list in sorted order. 

        --

        Time complexity: O(n log n) it takes O(n) time to add all items in self.routes to 
        list and O(n log n) time to sort the items in the list. 
        Space complexity: O(n) a new list is created with length equal to the number of 
        items in self.routes. 
        """
        # sorted by key
        if want == "key" or want == None:
            print("Routes in order of key")
            print([(key, self.routes[key]) for key in sorted(self.routes)])
        # sorted by value
        if want == "value":
            print("Routes in order of value")
            print(sorted(self.routes.items(), key = lambda kv:(kv[1], kv[0])))

    def split_prefixes(self, prefixes):
        """
        Returns dictionary of routes from text files.

        --

        Time complexity: O(n) have to iterate through all routes in self.routes
        Space complexity: O(n) creating and returning new dictionary with length equal
        to all items in prefixes files.
        """
        file = open(prefixes, 'r')
        prefixes_list = file.readlines()
        file.close()

        prefix_dict = {}
        for prefix_line in prefixes_list:
            if "," in prefix_line:
                # Splits string into prefix and cost
                prefix, cost = prefix_line.split(",")
                # puts in (key: prefix, value: cost) and takes out \n
                prefix_dict[prefix] = cost.strip('\n')

        return prefix_dict

    def call_cost(self, phone_number):
        """
        Returns cost of phone number as a string. 

        --

        Time complexity: Best case O(1) if the entire phone number exists in the routes 
        dictionary. Worst case O(p) where p is the length of the phone number if the 
        matching route is very short or if the phone number is not in the routes dictionary.
        
        Space complexity: Best case O(1) if the entire phone number exists in the routes 
        dictionary. Worst case O(p^2) where p is the length of the phone number if the 
        matching route is very short or if the phone number is not in the routes dictionary
        due to repeated slicing of the phone number. 
        """
        # holds original number
        original_number = phone_number
        while len(phone_number) > 0:
            # checks if phone number is in routes
            if phone_number in self.routes:
                cost = self.routes[phone_number]
                # print(f"{phone_number} cost found: {cost}")
                # adds phone number to dictionary for convience
                self.routes[original_number] = cost
                return cost
            # Removes last character from string
            phone_number = phone_number[:-1]
            # print("finding...")
        
        return 0
    
    def output_number_costs(self, *phone_number_lists):
        """
        input: text files of phone number lists
        output: returns new text file of all phone numbers with costs

        --
        
        """
        # deletes file - no longer neccessary
        # if os.path.exists("data/number-costs.txt"):
        #     os.remove("data/number-costs.txt")

        # initialize a txt file
        txt = open("data/number-costs.txt","w+")

        # O(n) on average, n = len(first given list)
        # This applies if only 1 list is given
        for phone_list in phone_number_lists:
            # number_holders is array of phone numbers
            pl = open(phone_list, 'r')
            # splits numbers into elements in number_list
            number_list = pl.readlines()
            pl.close()

            for number in number_list:
                number = number.strip("\n")
                # inputs number into call_cost function to find cost
                cost = self.call_cost(number)
                # writes phone number, cost onto the text file
                txt.write(f"{number},{cost}\r\n")

        txt.close()
        return txt

    # IDEA
    # save time by reading file
    # def save_time():
        # check = Path("data/numbers-costs.txt")
        # if config.is_file():
        #     # Store configuration file values
        # else:
        #     # Keep presets
        # searchfile = open("phone-numbers.txt", "r")
        # for line in searchfile:
        #     if "searchphrase" in line: print line
        # searchfile.close()

def get_mem():
    """
    Returns current memory usage in mb.

    --

    """
    usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if platform.system() == 'Linux':
        return round(usage/float(1 << 10), 2)
    return round(usage/float(1 << 20), 2)

if __name__ == "__main__":
    # keep track of time and memory
    before_time = time.time()
    before_mem = get_mem()

    # Input route-costs into CallRoutes object
    # Around 15 sec to run
    # c = CallRoutes("data/route-costs-10000000.txt", "data/route-costs-1000000.txt", "data/route-costs-106000.txt", "data/route-costs-35000.txt", "data/route-costs-600.txt", "data/route-costs-100.txt")
    # c = CallRoutes("data/route-costs-100.txt")
    c = CallRoutes("data/route-costs-600.txt", "data/route-costs-100.txt")
    c.output_number_costs("data/phone-numbers.txt")
    print(c.routes["+823320392141"])
    # print("Memory after loading call routes: {} mb ".format(get_mem()))

    # takes less than .1 second to calculate cost once constructor is built
    # before_time = time.time()
    # before_mem = get_mem()

    # outputs number-costs.txt
    # c.output_number_costs("data/phone-numbers-test.txt")
    # c.output_number_costs("data/phone-numbers.txt")

    # prints routes
    # c.print_routes()
    # c.print_routes('value')

    # print(c.call_cost("+613133255931"))
    # print(c.call_cost("+81926008441"))

    # log time and memory usage
    after_time = time.time()
    after_mem = get_mem()
    print(f"Total Processing Time: {after_time - before_time} s")
    print(f"Total Memory Usage: {after_mem - before_mem} mb")

    # displays phone numbers and costs in terminal
    # with open("number-costs.txt", 'r') as costs:
    #     print("Best call costs for the following numbers:\n{}".format(costs.read()))

    # c.print_routes()
    
