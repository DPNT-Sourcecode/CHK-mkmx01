

# noinspection PyUnusedLocal
# skus = unicode string
from typing import Counter


def checkout(skus):
   items_with_prices = {"A" : 50,"B":30,"C":20,"D":15,"E":40}
   
   if not all(char in items_with_prices for char in skus):
    return -1

   nr_of_items = Counter(skus)
   
   if "E" in nr_of_items and "B" in nr_of_items:
       free_b_item = nr_of_items["E"] // 2
       nr_of_items["B"] = max(0,nr_of_items["B"]-free_b_item)
       
   total = 0
   for item,count in nr_of_items.items():
       if item == 'C':
           total += count * items_with_prices[item]
       if item == 'D':
           total += count * items_with_prices[item]
       if item == "A":
          total += a_item_offers(count)
       if item == "B":
          total += (count // 2) * 45
          total += (count % 2) * 30
       if item == "E":
           total += count * items_with_prices[item]
               
   return total


def a_item_offers(count: int):
    offers = [(5,200),(3,130)]
    total = 0
    if count >  2:
        for count_number,count_price in sorted(offers,reverse=False):
            total += (count // count_number) * count_price
            total += (count % count_number) * 50
    else:
        total += count * 50
    return total



