
def fizzbuzz(value):

    if not (value % 3 + value % 5):
        return "fizbuzz"
    elif not (value % 3):
        return "fizz"
    elif not (value % 5):
        return "buzz"
    else:
        return value
        
my_value = fizzbuzz(15)  
