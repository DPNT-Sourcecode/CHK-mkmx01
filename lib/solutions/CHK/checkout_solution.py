

# noinspection PyUnusedLocal
# skus = unicode string
from typing import Counter


def checkout(skus):
   items_with_prices = {"A" : 50,"B":30,"C":20,"D":15,"E":40}
   if not all(char in items_with_prices for char in skus):
    return -1

   nr_of_items = Counter(skus)
   total = 0
   for item,count in nr_of_items.items():
       if item == 'C':
           total += count * items_with_prices[item]
       if item == 'D':
           total += count * 15
       if item == "A":
          total += (count // 3) * 130
          total += (count % 3) * 50
       if item == "B":
          total += (count // 2) * 45
          total += (count % 2) * 30
       if item == "E":
           
   return total



