

def call_routing(prefix_file, number):
    """
    Both params are strings. 
    """

    """Load words from dictionary"""
    file = open(prefix_file, 'r')
    prefixes = file.readlines()
    # print(prefixes)
    file.close()
    
    prefix_list = []

    for line in prefixes:
        prefix_list.append(line.split(','))
        # print(prefix_list)

    for prefix in prefix_list:
        pre_len = len(prefix[0])
        num_prefix = number[:pre_len]
        if num_prefix == prefix[0]:
            return number + "," + prefix[1]
        else: 
            print("number prefix and current", num_prefix, "and",  prefix[0])
        


prefixes = """+1512, 0.04
+1415, 0.02
"""
number = "+1667565111"

print(call_routing('route-costs-600.txt', number))
