#Welcome user: Implement the feature to welcome the user at the beginning of the conversation.
def welcome_user():
    print ("Welcome to the Pet Care Advisor Chatbot! My name is Py")

#Collect the user's name and age
def collect_users_information():
    print("I cant wait to get to know you and your pet better!")
    name= input("May I first have your name, please?")
    print("Prrfect! Nice to meet you {name} I hope I can help you take care of your pet")
    age= input("How old are you, {name}?")
    return name, age

#Collect user's dog information
def collect_pet_information():
    pet_name= input("What's your pet's name?")
    pet_breed= input(f"What breed is {pet_name}?")
    pet_age=input(f"How old is {pet_name}?")
    return pet_name, pet_breed, pet_age

#Ask the user how it can help them
def display_menu():
    print ("\nHow can I assist you today?")
    print("1. Set a feeding reminder")
    print("2. Get health tips for your pet")
    print("3. Get training advice")
    print("4. Find pet-friendly places")
    print("5. Exit")

#Include one menu option for exiting the conversation. This option should display a goodbye message and end your program.
def handle_choice(choice, pet_name, pet_breed):
    if choice== '5':
        print("Goodbye! Have a great day with your pet!")
    else:
        print("Sorry, I didn't understand that choice. Please try again.")
