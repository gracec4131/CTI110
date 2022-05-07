# create list
# 5/7/22
# cti-110 p2hw1 - total-purchase
# curtis grace
num = []
Sales_Tax = .07

item1 = float(input("Enter the price of item # 1: "))
item2 = float(input("Enter the price of item # 2: "))
item3 = float(input("Enter the price of item # 3: "))
item4 = float(input("Enter the price of item # 4: "))
item5 = float(input("Enter the price of item:# 5 "))

subtotal = float(item1 + item2 + item3 + item4 + item5)

total_sales_tax = float(subtotal * sales_tax)

total = subtotal + total_sales_tax

print('\nTotal = $', format(total, ',.2f'), sep='', end='\n\n')
