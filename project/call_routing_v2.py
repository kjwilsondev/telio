#python3

import os
import time
import resource
import platform
import pathlib

class CallRoutes(object):
    def __init__(self, *route_pages):
        """
        initialize routes
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
        iterates through items in self.routes 
        """
        return self._generator()

    def _generator(self):
        """
        returns items in set
        """
        for item in self.routes.items():
            yield item
    
    def print_routes(self, want=None):
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
        returns dictionary of routes from text file
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
        returns string of cost of phone number
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
        
        return None
    
    def output_number_costs(self, *phone_number_lists):
        """
        input: text files of phone number lists
        output: returns new text file of all phone numbers with costs
        """
        # deletes file - no longer neccessary
        # if os.path.exists("data/number-costs.txt"):
        #     os.remove("data/number-costs.txt")

        # initialize a txt file
        txt = open("data/number-costs.txt","w+")

        # O(N) on average, N = len(first given list)
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
    returns current memory usage in mb.
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
    
