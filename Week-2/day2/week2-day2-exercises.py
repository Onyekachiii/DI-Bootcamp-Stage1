# #ex 1
my_fav_numbers = {1,2,5,6,13,17,19,22}
my_fav_numbers.add (23)
my_fav_numbers.add (27)
print (my_fav_numbers)
my_fav_numbers.remove (27)
print (my_fav_numbers)
friend_fav_numbers = {43,56,83,97}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print (our_fav_numbers)


# #ex 3
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove ("Banana")
print (basket)
basket.append ("kiwi")
print(basket)
basket.insert (0, "Apples")
print(basket)
x = basket.count ("Apples")
print (x)
basket.clear ()
print (basket)


#ex 4
x = []
for i in range (3,12):
    x.append (i /2)
print (x)


# #ex 5
for number in range (1,21):
    if number % 2 == 0:
        print(number)
    
#ex 6
user_input = ""
while (user_input != "Stanley"):
     user_input = input ("enter your name ")
        
print ('succesful')


#ex 7
fruits_input = input ('Enter fruit: ')
fruits_list = fruits_input.split (' ')
#print (fruits_list)

search_keyword = ('Enter search keyword: ')

if search_keyword in fruits_list:
    print ('You chose one of your favorite fruits. Enjoy!')
else:
    print ('You chose a new fruit. I hope you enjoy!')


#ex 8
toppings = []
while True:
    topping = input("Enter a pizza topping (or 'quit' to exit): ")
    if topping == "quit":
        break
    else:
        toppings.append(topping)
        print("Adding", topping, "to your pizza.")

print("You have chosen the following toppings for your pizza:")
for topping in toppings:
    print("-", topping)

total_price = 10 + 2.5 * len(toppings)
print("The total price for your pizza is $", total_price)



# #ex 9
num_people = int(input("How many people are in your family?"))
total_cost = 0

for i in range(num_people):
    age = int(input("Enter the age of person {}: ".format(i+1)))
    
    if age < 3:
        ticket_cost = 0
    elif age >= 3 and age <= 12:
        ticket_cost = 10
    else:
        ticket_cost = 15
    
    total_cost += ticket_cost

print("The total cost for your family is $", total_cost)

teenagers = ["John", "Mary", "Alex", "Tom"]
final_list = []

for teenager in teenagers:
    age = int(input("Enter the age of {}: ".format(teenager)))
    
    if age >= 16 and age <= 21:
        final_list.append(teenager)

print("The final list of teenagers allowed to watch the movie is:", final_list)


#ex 10
sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")

finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    finished_sandwiches.append(sandwich)

for sandwich in finished_sandwiches:
    print("I made your " + sandwich)