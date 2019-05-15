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
"""
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
        print("ROUTES",self.routes)

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
        print("ALL ROUTES IN SORTED ORDER\n{}".format([(key, self.routes[key]) for key in sorted(self.routes)]))

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
        return txt

def get_mem():
    """
    returns current memory usage in mb.
    """
    usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if platform.system() == 'Linux':
        return round(usage/float(1 << 10), 2)
    return round(usage/float(1 << 20), 2)

if __name__ == "__main__":
    before = time.time() # keep track of time

    print("Memory before: {} mb ".format(get_mem()))

    # Testing on 10,000,000, 1,000,000 106,000 and 35,000 route files
    c = CallRoutes("route-costs-10000000.txt", "route-costs-1000000.txt", "route-costs-106000.txt", "route-costs-35000.txt")
    print("Memory after loading call routes: {} mb ".format(get_mem()))

    # Testing on 10,000 phone number file
    c.output_number_costs("phone-numbers-10000.txt")
    after = time.time() # log total time

    print(f"Total Processing Time: {after - before} s")
    print(f"Total Memory Usage: {get_mem()} mb")

    # Uncomment lines 140 and 141 to display phone numbers and costs in terminal
    # with open("number-costs.txt", 'r') as costs:
    #     print("Best call costs for the following numbers:\n{}".format(costs.read()))
    
    # c.print_routes()
    
