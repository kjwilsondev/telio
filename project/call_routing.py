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
                prefix_dict[prefix] = cost.strip('\n')
        return prefix_dict

    def match_prefix(self, phone_numbers):
        results = ''
        # grab all the phone numbers from the file
        with open(phone_numbers, 'r') as numbers:
            print(numbers.read())
            prefix_dict = self.split_prefixes(self.prefixes)

            for num in numbers:
                # it seems that 8 is the length of the longest prefix
                for i in range(8, 0, -1):
                    # starting at the longest possible prefix, reduce size each time
                    current_prefix = num[:i]
                    if current_prefix in prefix_dict: # found match
                        # print(current_prefix)
                        cost = prefix_dict[current_prefix]
                        new_result = num + ',' + cost + '\n' # concatenate result
                        # print(new_result)
                        results += new_result
                    break # evaluate next phone number
        return results
        

if __name__ == "__main__":
    c = CallRoutes("route-costs.txt", "phone-numbers.txt")
    print(c.match_prefix(c.phone_numbers))


        
        

