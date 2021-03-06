func_count_dic = {}
userA = {}
userB = {}


def check_fn_docs():
    '''
    A function check_fn_docs is defined to check whether the input function 
    has doctring length should be 50 characters.
    Input : function name
    Output : return nested function.
    '''
    char_count = 50
    def len_docs_check(func):
        '''
        nested function of check_fn_docs function.
        '''
        if len( func.__doc__ ) > char_count:
            return True
        else:
            return False
    return len_docs_check


def next_fibo_number():
    '''
    print the next fibonacci number
    Input : None
    Output : return nested function
    '''
    a, b, count = 0, 1, 0
    def print_next_number():
        '''
        Inner function of next_fibo_number function.
        '''
        nonlocal a, b, count
        count += 1
        if count == 1:
            return 0
        elif count == 2:
            return 1
        else:
            c = a + b
            a, b = b, c
            return b
    return print_next_number


def add(a, b):
    '''
    A function add which take two input parameters.
    And add them if it is number 
    or concatenate them if it is a string.
    Input: a, b two parameters
    Output: return a+b
    '''
    return a+b


def mul(a, b):
    '''
    A function mul which take two input parameters.
    And multiplies them if both are number
    or one parameter is string and second one is number then print string integer times
    Input: a, b two parameters
    Output: return a*b
    '''
    return a*b



def div(a, b):
    '''
    A function mul which take two input parameters.
    And multiplies them if both are number
    or one parameter is string and second one is number then print string integer times
    Input: a, b two parameters
    Output: return a/b
    '''
    return a/b


def function_counter(func):
    '''
    A function  to count the number of times others functions are called and store the same in a dictionary 
    Input : a function name
    Output : return nested function
    '''
    count = 0
    def start_count():
        '''
        Inner function of function_counter.
        An Implementation of closure.
        '''
        nonlocal count
        count += 1
        func_count_dic[func.__name__] = count
        return func_count_dic
    return start_count


def function_two_dict(func, dic):
    '''
    A function  to count the number of times others functions are called and store the same in a dictionary 
    Input : a function name
    Output : return nested function
    '''
    count = 0
    def inner():
        '''
        nner function of function_counter.
        An Implementation of closure.
        '''
        nonlocal count
        count += 1
        dic[func.__name__] = count
        return dic
    return inner
