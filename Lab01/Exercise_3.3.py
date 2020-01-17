# =============================================================================
# # ABE 651 
# # 1/17/2020
# # Logan Heusinger
# # EX 3.3 (3.5 from PDF book)
# # Parts 1

# create the follwing figure
# + - - - + - - - +
# |       |       |
# |       |       |
# |       |       |
# |       |       |
# + - - - + - - - +
# |       |       |
# |       |       |
# |       |       |
# |       |       |
# + - - - + - - - +
# 
# =============================================================================

#performes a function twice
def do_twice(arg,val):
    arg(val)
    arg(val)
    
    
def print_twice(f):
    print(f)
    print(f)
           
    

string1 = "+ - - - + - - - +"
string2 = "|       |       |"

#deliverable
print(string1)
do_twice(print_twice,string2)
print(string1)
do_twice(print_twice,string2)
print(string1)