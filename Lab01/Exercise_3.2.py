# ABE 651 
# 1/17/2020
# Logan Heusinger
# EX 3.2 (3.4 from PDF book)
# Parts 1-4
#-------------------------------------------------------------#

def do_twice(arg,val):
    arg(val)
    arg(val)
    
def print_twice(f):
    print(f)
    print(f)
           
    
do_twice(print_twice,"spam")


