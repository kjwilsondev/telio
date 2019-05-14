#python3

import itertools

# V3: Binary Search

class CallRoutes():
    def __init__(self, prefixes, phone_numbers):
        self.prefixes = prefixes
        self.phone_numbers = phone_numbers
        """Initialize dictionary"""
        self.prefix_dict = {}

    # Takes phone numbers 
    def split_prefixes(self, prefixes):

        """Load words from dictionary"""
        file  = open(prefixes, 'r')
        prefixes_list = file.readlines()
        file.close()

        for prefix_line in prefixes_list:
            if "," in prefix_line:
                prefix, cost = prefix_line.split(",")
                self.prefix_dict[prefix] = cost.strip('\n')

        return self.prefix_dict

    def match_prefix(self, phone_numbers):

        with open(phone_numbers, 'r') as numbers:
            self.prefix_dict = self.split_prefixes(self.prefixes)

            for num in numbers:
                longest_prefix = num[:8]
                print(longest_prefix)
                if num in self.prefix_dict:
                    pass
        

if __name__ == "__main__":
    c = CallRoutes("route-costs.txt", "phone-numbers.txt")
    # print(c.match_prefix(c.phone_numbers))


        
        

