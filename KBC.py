# CHECKING USER CHOICE FOR THE GAME
print("1. Cricket \n2. Football")

# Taking user choice input
try:
    choice = int(input("Enter your choice (1 for Cricket, 2 for Football): "))
except ValueError:
    print("Invalid input! Please enter a number.")
    choice = 0

# CRICKET 
if choice == 1:
    print("Who is called the Cricket God in India?")
    ans1 = "Sachin Tendulkar"
    user1 = input("Guess the answer: ")
    
    # Strip and lower to handle capitalization safely
    if user1.strip().lower() == ans1.lower():
        print("You got it.")
        print("Hope you are enjoying. Moving to next Question\n")
        
        print("Who scored the highest runs in the IPL and hit a 15-ball 50 in the year 2026?")
        user2 = input("Guess the Cricketer's name: ")
        
        
        user2_clean = user2.strip().lower()
        if user2_clean == "vaibhav suryanshi" or user2_clean == "vaibhav sooryavanshi":
            print("You got it.")
            print("Thank You for Playing this game.")
            print("See You soon.")
        else:
            print("You failed. Game Over.")
    else:
        print("You failed try again.")

# --- FOOTBALL PATH ---
elif choice == 2:
    print("Who won the FIFA World Cup 2026?")
    ans1_fb = "Spain"
    user1_fb = input("Enter the Team name: ")
    
    if user1_fb.strip().lower() == ans1_fb.lower():
        print("You got it.")
        print("Hope you are enjoying. Moving to next Question\n")
        
        print("Who is the Colombian singer who sang 'Waka Waka'?")
        user2_fb = input("Guess the Singer's name: ")
        ans2_fb = "Shakira"
        
        if user2_fb.strip().lower() == ans2_fb.lower():
            print("You got it.")
            print("Thank You for Playing this game.")
            print("See You soon.")
        else:
            print("You failed. Game Over.")
    else:
        print("You failed try again.")

else:
    print("Wrong choice selected.")
