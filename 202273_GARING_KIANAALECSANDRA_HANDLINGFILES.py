#!/usr/bin/env python
# coding: utf-8

# In[1]:


# NON-INTERACTIVE CODE CELL. YOU MAY RUN THIS CELL, BUT DO NOT EDIT IT.
# FOR DEMONSTRATION PURPOSES ONLY. DO NOT EDIT.

products = {
    "americano":{"name":"Americano","price":150.00},
    "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
    "cappuccino":{"name":"Cappuccino","price":170.00},
    "dalgona":{"name":"Dalgona","price":170.00},
    "espresso":{"name":"Espresso","price":140.00},
    "frappuccino":{"name":"Frappuccino","price":170.00},
}


# In[2]:


# CODE CELL
# PROBLEM 1

def get_product(code):
    return(products[code])


# In[3]:


# CODE CELL
# PROBLEM 2

def get_property(code, property):
    return(products[code][property])


# In[4]:


# CODE CELL
# PROBLEM 3

def main():
    order_dict = {}
    orderover = False
    grandtotal = 0

    try:
        while orderover == False:
            textinput = input(f'What is your order?\n"americano", "brewedcoffee", "cappuccino", "dalgona", "espresso", "frappuccino"\nPlease add a comma and then the quantity of your order\nIf your order is finished, type "/": ')


            if textinput == "/":
                orderover = True
            else:
                order_code,order_quant = textinput.split(",")

                if order_code not in products:
                    print("Invalid order. Please try again.")
                elif order_code not in order_dict:
                    order_dict[order_code] = {"name": products[order_code]["name"], 'subtotal': float(order_quant)*get_property(order_code, "price"), "quantity": float(order_quant)}
                elif order_code in order_dict:
                    order_dict[order_code]["quantity"] += float(order_quant)
                    order_dict[order_code]["subtotal"] += float(order_quant)*get_property(order_code, "price")
    except:
        print("Invalid input.")

    order_dict = dict( sorted(order_dict.items(), key=lambda x: x[0].lower()) )

    with open('receipt.txt', 'w') as receipt:
        receipt.write('''
==
CODE\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL
            ''')

        for key in order_dict:
            grandtotal += order_dict[key]["subtotal"]
            receipt.write(f'\n{key}\t\t{order_dict[key]["name"]}\t\t{order_dict[key]["quantity"]}\t\t\t{order_dict[key]["subtotal"]}')
        receipt.write(f'''\n\nTotal:\t\t\t\t\t\t\t\t\t{grandtotal}
==
            ''')



# In[ ]:
