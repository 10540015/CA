#!/usr/bin/env python
# coding: utf-8

# In[1]:


#A shopping basket contains a number of line items, for example: eggs, rice, flour; each with a specific quantity.
#A basket may also have one discount code, for example eggs20.
#The shop has a standard price list, as well as a set of currently valid discount codes, each of which confers a certain percentage discount for a list of eligible products.
#Produce a method which accepts a list of baskets, and outputs their values from highest to lowest.


# In[6]:


shopping_list = ["banana", "orange", "apple"]

stock = { "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = { "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}


def compute_bill(food):
    total = 0
    for item_food in food:
        for item_stock in stock:
            if item_stock == item_food:
                if stock[item_stock] > 0:
                    stock[item_stock] = stock[item_stock] - 1
                    total = total + prices[item_stock] 
    return total

food = ['banana', 'apple', 'orange', 'pear']
total =  compute_bill(shopping_list)
print(total)
if(total>0):
    if total<=5:
       disc = total*0.05
    elif total<=15:
        disc=total*0.12
    elif total<=25:
        disc=0.2 * total
    else:
         disc=0.3 * total

    print("Discount : ",disc)
    print("Net Pay  : ",total-disc)
else:
    print("Invalid Amount")


# In[ ]:




