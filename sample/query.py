"""Command line interface to query the stock.
To iterate the source data you can use the following structure:
for item in warehouse1:
    # Your instructions here.
    # The `item` name will contain each of the strings (item names) in the list.
"""
from data import warehouse1, warehouse2
# YOUR CODE STARTS HERE
user_search = ""

user_name = input('What is your first name? ')

print(f'Hello {user_name.title()}')

print(f'Please choose from the menu:\n1. List items by warehouse.\n2. Search an item and place an order.\n3. Quit.')

picked_num = int(input('Please choose a number: '))

if picked_num == 1:
    print('Items from warehouse 1: ')
    for i in warehouse1:
        print(i)
        print('Items from warehouse 2: ')
        for j in warehouse2:
            print(j)

elif picked_num == 2:
    item_name = input('Enter an item name: ')
    w1 = warehouse1.count(item_name)
    w2 = warehouse1.count(item_name)
    w3 = w1 + w2
    print(f'Total amount of items in both warehouses: {w3} ')
    if w1 > 0 and w2 > 0:
        print('Location: Both warehouse')
        if w1 > w2:
            print(f'warehouse 1 has the highest number items: Total {w1}')
        else:
            print(f'warehouse 2 has the highest number items: Total {w2}')

    elif w1 > 0 and w2 == 0:
        print('Location: warehouse 1')
    elif w1 == 0 and w2 > 0:
        print('Location: warehouse 2')
    else:
        print('Not in stock')

    ans = input('Do you want to place an order for this item?: ')

    if ans == 'yes':
        num_amount = int(input('how many do you want?: '))
        if num_amount <= w3:
            print(f'The order has been placed! {item_name} and amount ordered {num_amount}')
    if ans == 'no':
        print(f'Have a nice day! {user_name}')


elif picked_num == 3:
    print(f'Have a nice day! {user_name}')

print(f'Thank you for your visit {user_name}')































# for items in warehouse1:
#     if



# Get the user name

# Greet the user

# Show the menu and ask to pick a choice

# If they pick 1
#
# Else, if they pick 2
#
# Else, if they pick 3
#
# Else

# Thank the user for the visit
