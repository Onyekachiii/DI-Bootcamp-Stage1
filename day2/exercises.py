#ex 1
my_fav_numbers = {1,2,5,6,13,17,19,22}
my_fav_numbers.add (23)
my_fav_numbers.add (27)
print (my_fav_numbers)
my_fav_numbers.remove (27)
print (my_fav_numbers)
friend_fav_numbers = {43,56,83,97}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print (our_fav_numbers)


#ex 3
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


#ex 5
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
