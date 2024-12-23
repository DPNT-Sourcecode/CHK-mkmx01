

# noinspection PyUnusedLocal
# skus = unicode string
from typing import Counter


def checkout(skus):
   items_with_prices = {"A" : 50,"B":30,"C":20,"D":15,"E":40,"F":10,"G":20,"H":10,"I":35,"J":60,"K":80,"L":90,"M":15,"N":40,"O":10,"P":50,
                        "Q":30,"R":50,"S":30,"T":20,"U":40,"V":50,"W":20,"X":90,"Y":10,"Z":50}
   offers = {"A":[(5,200),(3,130)],"B":[(2,45),],"H":[(10,80),(5,45)],"K":[(2,150)],"P":[(5,200)],"Q":[(3,80)],"V":[(3,130),(2,90)]}
   
   if not all(char in items_with_prices for char in skus):
    return -1

   nr_of_items = Counter(skus)
   
   if "E" in nr_of_items and "B" in nr_of_items and nr_of_items["E"] >=2:
       free_b_item = nr_of_items["E"] // 2
       nr_of_items["B"] = max(0,nr_of_items["B"]-free_b_item)
   
   if "F" in nr_of_items and nr_of_items["F"] >=3:
       free_f_item = nr_of_items["F"] // 3
       nr_of_items["F"] = nr_of_items["F"]-free_f_item
    
   if "N" in nr_of_items and "M" in nr_of_items and nr_of_items["N"] >=3:
       free_m_item = nr_of_items["N"] // 3
       nr_of_items["M"] = max(0,nr_of_items["M"]-free_m_item)
       
   nr_of_items = reduce_item(nr_of_items,"R","Q",3)
       
   total = 0
   for item,count in nr_of_items.items():
       if item in offers: 
           for count_number,count_price in sorted(offers[item],reverse=True):
               total += (count // count_number) * count_price
               count %= count_number
           total += count * items_with_prices[item]
       else:
            total += count * items_with_prices[item] 
        
   return total


def reduce_item(nr_of_items, main_item,reducable_item, initial_needed_ammount):
    if main_item in nr_of_items and reducable_item in nr_of_items and nr_of_items[main_item] >=initial_needed_ammount:
       free_item = nr_of_items[main_item] // initial_needed_ammount
       nr_of_items[reducable_item] = max(0,nr_of_items[reducable_item]-free_item)
    
    return nr_of_items

