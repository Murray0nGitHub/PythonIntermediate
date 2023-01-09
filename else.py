#You are making a digital menu to order food.
#The menu is stored as a list of items.
#Your program needs to take the index of the item as input and output the item name.
#In case the index is not valid, you should output "Item not found".
#In case the index is valid and the item name is output successfully, you should output "Thanks for your order".

#Sample Input
#2

#Sample Output
#Cheeseburger
#Thanks for your order
#Handle the cases when the input is out of range, as well as when it is not a number.


menu = ['Fries', 'Sandwich', 'Cheeseburger', 'Coffee', 'Soda']

try:
    n = int(input())
    print(menu[n])
    print("Thanks for your order")
except:
    print("Item not found")