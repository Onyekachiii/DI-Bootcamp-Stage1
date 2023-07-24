print("Hello World "*4 + "I love Python "*4)


user_input=int(input("enter a month 1 - 12")) 
if user_input == 3 or user_input == 4 or user_input == 5:
    print("Spring")
elif user_input == 6 or user_input == 7 or user_input == 8:
    print("Summer")
elif user_input == 9 or user_input == 10 or user_input == 11:
    print("Autumn")
elif user_input == 12 or user_input == 1 or user_input == 2:
    print("Winter")
    
my_text="""Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
           sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
           Ut enim ad minim veniam, quis nostrud exercitation ullamco 
           laboris nisi ut aliquip ex ea commodo consequat. 
           Duis aute irure dolor in reprehenderit in voluptate velit 
           esse cillum dolore eu fugiat nulla pariatur. 
           Excepteur sint occaecat cupidatat non proident, 
           sunt in culpa qui officia deserunt mollit anim id est laborum."""
print(len(my_text))