list = raw_input("enter the string:") 
def foo(x):
     print x * 5

 
def my_map_simple(fun, list):
     for item in list:
         fun(item)

 
my_map_simple(foo, list)
