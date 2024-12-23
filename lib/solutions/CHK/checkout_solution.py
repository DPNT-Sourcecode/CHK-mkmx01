

# noinspection PyUnusedLocal
# skus = unicode string
from typing import Counter


def checkout(skus):
   items = ["A","B","C","D","E"]
   if not all(char in items for char in skus):
    return -1

   nr_of_items = Counter(skus)
   total = 0
   for item,count in nr_of_items.items():
       if item == 'C':
           total += count * 20
       if item == 'D':
           total += count * 15
       if item == "A":
          total += (count // 3) * 130
          total += (count % 3) * 50
       if item == "B":
          total += (count // 2) * 45
          total += (count % 2) * 30
   return total
