def welcome_user(): 
  print ("Welcome to the Pet Care Advisor Chatbot! My name is Py")

def collect_user_info():
  print ("I can't wait to get to know you and your pet better!")
  name = input("What is your name? ")
  age = input("How old are you? ")
  print ("Prrfect! Nice to meet you, " + name+"!")
  print ("I see you are " + age + " years old.")
  return name, age

def collect_pet_info():
  pet_name = input("What's your pet's name? ")
  pet_type = input("What type of animal is your pet? ")
  pet_age = input("How old is your pet? ")
  print ("I see your pet's name is " + pet_name + ", it is a " + pet_type +"")
  return pet_name, pet_type 

def display_menu():
  print("How can I help you today?")
  print("1. Set a feeding reminder")
  print("2. Get health tips for your pet")
  print("3. Get training advice")
  print("4. Find pet-friendly places to visit")
  print("5. Exit")

def handle_choice (choice, pet_name, pet_breed):
  if choice=='5':
    print("Goodbye! Have a great day with your pet!")
  else:
    print("Sorry, I didn't understand that choice. Please try again.")

welcome_user()
user_name, user_age= collect_user_info()
pet_name, pet_type= collect_pet_info()
display_menu()
choice = input("Enter your choice")
handle_choice(choice, pet_name, pet_type)
