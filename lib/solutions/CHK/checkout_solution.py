

# noinspection PyUnusedLocal
# skus = unicode string
from typing import Counter


def checkout(skus):
   items_with_prices = {"A" : 50,"B":30,"C":20,"D":15,"E":40}
   offers = {"A":[(5,200),(3,130)],"B":[(2,45)]}
   
   if not all(char in items_with_prices for char in skus):
    return -1

   nr_of_items = Counter(skus)
   
   if "E" in nr_of_items and "B" in nr_of_items and nr_of_items["E"] >=2:
       free_b_item = nr_of_items["E"] // 2
       nr_of_items["B"] = max(0,nr_of_items["B"]-free_b_item)
       
   total = 0
   for item,count in nr_of_items.items():
       if item in offers: 
           for count_number,count_price in sorted(offers[item],reverse=True):
               total += (count // count_number) * count_price
               print(count // count_number)
               print(count)
               print(count_number)
               print(count_price)
               print(total)
               count % count_number
           total += (count // count_number) * count_price
           count % count_number
           total += count * items_with_prices[item] 
       else:
            total += count * items_with_prices[item] 
        
   print(total) 
   return total

checkout("AAA")


