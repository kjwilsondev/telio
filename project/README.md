# Call_Routing_V2

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

Improves on v1 by handling multiple pages of route costs and multiple pages of phone numbers.
Also writes output to a file as well as returning file so that user can access the information
either way. 

There is also testing for functions and code is well documented. Memory and time complexities
for all functions are annotated and actual memory and time usage is logged and output to terminal. 

Potential Improvements: 
- create a web-service API to allow clients to price a call before it is initiated
- create an efficient route cost lookup solution that can handle high spikes of traffic 
(up to 10,000 requests per minute) without overloading servers