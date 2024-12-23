

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    number_of_items = int(skus[0])
    type_of_item = skus[1]
    
    if(type_of_item == 'C'):
        return number_of_items * 20
    
    if(type_of_item == 'D'):
        return number_of_items * 15
    
    if(type_of_item == 'A'):
        remainder = number_of_items % 3
        if(remainder == 0):
            return (number_of_items/3)*130
        else:
            round_low = number_of_items - remainder
            offer_return = round_low * 130 
            return (remainder * 50) + offer_return
        
    if(type_of_item == 'B'):
        remainder = number_of_items % 2
        if(remainder == 0):
            return (number_of_items/2)*45
        else:
            round_low = number_of_items - remainder
            offer_return = round_low * 45 
            return (remainder * 30) + offer_return
    
    return -1
