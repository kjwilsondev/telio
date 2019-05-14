#python3

import itertools

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
                prefix_dict[prefix] = cost.strip('\n')
        return prefix_dict

    def match_prefix(self, phone_numbers):
        results = ''
        # grab all the phone numbers from the file
        with open(phone_numbers, 'r') as nums:
            numbers = nums.read().splitlines() # get list of phone numbers
            prefix_dict = self.split_prefixes(self.prefixes) #assign prefixes to dict
            
            for num in numbers:
                # starting at the longest possible prefix, reduce size each time
                for i in range(len(num)-1, 0, -1):
                    # slicing increases space complexity; is there a better way?
                    current_prefix = num[:i]
                    if current_prefix in prefix_dict: # found match
                        cost = prefix_dict[current_prefix]
                        new_result = num + ',' + cost + '\n' # concatenate result
                        results += new_result
                        break # evaluate next phone number
        return results
        

if __name__ == "__main__":
    c = CallRoutes("route-costs-1000000.txt", "phone-numbers-10000.txt")
    print(c.match_prefix(c.phone_numbers))


        
        

