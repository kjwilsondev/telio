#python3

import itertools

# V3: Binary Search

class CallRoutes():
    def __init__(self, prefixes, phone_numbers):
        self.prefixes = prefixes
        self.phone_numbers = phone_numbers

    
    # Takes phone numbers 
    def split_prefixes(self, prefixes):
        """Initialize dictionary"""
        prefix_dict = {}

        """Load words from dictionary"""
        file  = open(prefixes, 'r')
        prefixes_list = file.readlines()
        file.close()

        for prefix_line in prefixes_list:
            if "," in prefix_line:
                prefix, cost = prefix_line.split(",")
                prefix_dict[prefix] = cost

        return prefix_dict
        # test

if __name__ == "__main__":
    c = CallRoutes("data/route-costs.txt", "data/phone-numbers.txt")
    print(c.split_prefixes(c.prefixes))


        
        

