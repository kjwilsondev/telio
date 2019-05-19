#python3

"""
Improves on v0 by handling muliple phone numbers and using a dictionary 
to process phone numbers much faster. 

Potential Improvements: 
- Write output to file instead of handling just string
- Handle multiple files of phone numbers 
- Handle multiple files of route costs
- Handle situation where there are multiple costs for identical
routes (carriers cost different amounts)
"""

import itertools
import os
import time
import resource
import platform
import pathlib

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
        results = ''
        # grab all the phone numbers from the file
        with open(phone_numbers, 'r') as nums:
            numbers = nums.read().splitlines()  # get list of phone numbers
            prefix_dict = self.split_prefixes(
                self.prefixes)  # assign prefixes to dict

            for num in numbers:
                # starting at the longest possible prefix, reduce size each time
                for i in range(len(num)-1, 0, -1):
                    # slicing increases space complexity; is there a better way?
                    current_prefix = num[:i]
                    if current_prefix in prefix_dict:  # found match
                        cost = prefix_dict[current_prefix]
                        new_result = num + ',' + cost + '\n'  # concatenate result
                        results += new_result
                        break  # evaluate next phone number
        return results

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

    c = CallRoutes("route-costs-106000.txt", "phone-numbers-1000.txt")
    print(c.match_prefix(c.phone_numbers))

    # log time and memory usage
    after_time = time.time()
    after_mem = get_mem()
    print(f"Total Processing Time: {after_time - before_time} s")
    print(f"Total Memory Usage: {after_mem - before_mem} b")


        
        

