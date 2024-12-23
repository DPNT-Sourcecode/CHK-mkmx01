

# noinspection PyUnusedLocal
# skus = unicode string
from typing import Counter


def checkout(skus):
   items_with_prices = {"A" : 50,"B":30,"C":20,"D":15,"E":40}
   offers = {"A":[(5,200),(3,130)],"B":[(2,45)]}
   
   if not all(char in items_with_prices for char in skus):
    return -1

   nr_of_items = Counter(skus)
       
   total = 0
   for item,count in nr_of_items.items():
       if item in offers: 
           for count_number,count_price in sorted(offers[item],reverse=True):
               total += (count // count_number) * count_price
               total += (count % count_number) * items_with_prices[item]
       else:
            total += count * items_with_prices[item] 
            
   if "E" in nr_of_items and "B" in nr_of_items:
       free_b_item = nr_of_items["E"] // 2
       total -= free_b_item * items_with_prices["B"]
            
   return total




