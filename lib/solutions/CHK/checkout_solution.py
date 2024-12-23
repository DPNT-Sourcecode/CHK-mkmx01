

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
               count % count_number
           total += count * items_with_prices[item]  
       else:
            total += count * items_with_prices[item] 
        
            
   return total


def deploy_a_solution(nr_of_items):
   total = 0 
   if nr_of_items >=5:
       total += (nr_of_items // 5) * 200 
       remaining_number = nr_of_items % 5
       total += total_based_offer(remaining_number,3,130,50)
   else:
       total += total_based_offer(remaining_number,3,130,50)
   return total


def total_based_offer(nr_of_items,offer_nr,offer_price,price_wo_offer):
    total = 0
    percentage=nr_of_items % offer_nr
    if percentage == 0:
        total += (nr_of_items // offer_nr) * offer_price 
        remaining_number = nr_of_items % offer_nr
        total += remaining_number * price_wo_offer
    else: 
        total += nr_of_items * price_wo_offer
    return total

