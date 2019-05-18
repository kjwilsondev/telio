#python3

"""
Pseudocode:
- import call route txt files
- input phone number costs into dictionary
    - read call route lines
    - splits call routes into (key: phone number, value: costs) pairs
    - ex input: "+86153,0.84"
    - ex output: {(+86153:0.84)}
- import phone number txt files
- look up phone numbers in dictionary
- output costs
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
            self.update_routes(route_page)

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
        # sorted by key
        for key, value in sorted(self.routes.items()):
            yield (key, value)
    
    def _print_routes(self, want=None):
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
            print("Routes in order of key:")
            print([pair for pair in self])
        # sorted by value
        if want == "value":
            print("Routes in order of value:")
            print(sorted(self.routes.items(), key = lambda kv:(kv[1], kv[0])))

    def update_routes(self, prefixes):
        """
        old name: split_prefixes

        Splits route-costs txt file lines into key:prefix value:cost pair dictionary
        ex input: "+86153,0.84"
        ex output: {(+86153:0.84)}

        Updates self.routes dictionary with prefix dictionary pairs
        Returns prefix dictionary from text file input.

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

        # set update method
        # this method updates the self.routes dictionary with 
        # key:prefix, value:cost pairs in prefix_dict
        self.routes.update(prefix_dict) # O(len(n))
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
            if phone_number in self.routes: # O(1)
                cost = self.routes[phone_number]
                # adds phone number to dictionary for convenience
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
                phone numbers are added to self.routes

        --
        
        """

        # initialize a txt file
        txt = open("data/number-costs.txt","w+")

        # O(n), n = lines in lists
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

def get_mem():
    """
    Returns current memory usage in bytes.

    --
    Time complexity: O(1)
    Space complexity: O(1)
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
    c = CallRoutes("data/route-costs-100.txt")
    c.update_routes("data/route-costs-600.txt")
    c.output_number_costs("data/phone-numbers.txt")
    # print(c.routes["+823320392141"])
    # print("Memory after loading call routes: {} mb ".format(get_mem()))

    # takes less than .1 second to calculate cost once constructor is built
    before_time = time.time()
    before_mem = get_mem()

    # outputs number-costs.txt
    c.output_number_costs("data/phone-numbers-test.txt")
    # c.output_number_costs("data/phone-numbers.txt")

    # prints routes
    c._print_routes()
    c._print_routes('value')

    # print(c.call_cost("+613133255931"))
    # print(c.call_cost("+81926008441"))

    # log time and memory usage
    after_time = time.time()
    after_mem = get_mem()
    print(f"Total Processing Time: {after_time - before_time} s")
    print(f"Total Memory Usage: {after_mem - before_mem} b")

    # displays phone numbers and costs in terminal
    # with open("number-costs.txt", 'r') as costs:
    #     print("Best call costs for the following numbers:\n{}".format(costs.read()))

    # c.print_routes()
    
