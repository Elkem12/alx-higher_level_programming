def print_reversed_list_integer(my_list=[]):
    reversed_list = []
    for item in my_list:
        reversed_list = [item] + reversed_list
    for item in reversed_list:
        print("{:d}".format(item))
