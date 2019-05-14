#python3

# Helpful:
# https://stackoverflow.com/questions/4989763/when-is-it-better-to-use-zip-instead-of-izip
# In Python 3 the built-in zip does the same job as itertools.izip
# 2.X returns an iterator instead of a list.
# https://github.com/nschloe/matplotlib2tikz/issues/20
# try:
#     # Python 2
#     from itertools import izip
# except ImportError:
#     # Python 3
#     izip = zip

import time
import resource
import platform

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
    
    def print_routes(self):
        # print(self.routes)
        print([(key, self.routes[key]) for key in sorted(self.routes)])

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
        # initialize a txt file
        txt = open("number-costs.txt","w+")

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
        return

def get_mem():
    """
    returns current memory usage in mb.
    """
    usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if platform.system() == 'Linux':
        return round(usage/float(1 << 10), 2)
    return round(usage/float(1 << 20), 2)

if __name__ == "__main__":
    before = time.time()
    print(get_mem())
    c = CallRoutes("route-costs-1.txt", "route-costs-2.txt", "route-costs-3.txt", "route-costs-4.txt")
    print(get_mem())
    c.output_number_costs("phone-numbers.txt")
    after = time.time()
    print(f"Time: {after - before} s")
    print(f"Memory: {get_mem()} mb")
    # print(c.call_cost("+86153892109"))
    # c.print_routes()
    
