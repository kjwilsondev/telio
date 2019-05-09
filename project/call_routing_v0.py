

def call_routing(prefix_file, number):
    """
    Both params are strings. 
    """
    prefix_list = []
    prefix_split = prefix_file.split('\n')
    print("INITIAL SPLIT", prefix_split)

    for line in prefix_split:
        prefix_list.append(line.split(','))
    print(prefix_list)

    for prefix in prefix_list:
        pre_len = len(prefix[0]) - 1
        num_prefix = "+" + number[:pre_len]
        print("number prefix and current", num_prefix, "and",  prefix[0])
        if num_prefix == prefix[0]:
            return number + "," + prefix[1]
        else: 
            print


prefixes = """+1512, 0.04
+1415, 0.02
"""
number = "15124156620"

print(call_routing(prefixes, number))