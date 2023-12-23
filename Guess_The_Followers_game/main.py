# This game is about guessing the number of followers of different social media accounts.
import random
from game_data import data
from art import logo, vs
 
def compare(): 
  score = 0  
  celebrity1 = random.choice(data)
  while True:
    celebrity2 = random.choice(data)
    while celebrity1 == celebrity2:
       celebrity2=random.choice(data)
      
    print(f"Compare A : {celebrity1['name']}, {celebrity1['description']} from {celebrity1['country']}")
    print(f"{vs}\n")
    print(f"Against B : {celebrity2['name']}, {celebrity2['description']} from {celebrity2['country']}\n")
    user_answer = input("Which has more follwers?").upper()
  
    if celebrity1["follower_count"] > celebrity2["follower_count"]:
      answer = "A"
    else :
      answer = "B"
    if user_answer == answer:
      score +=1
      print(f"\n{celebrity1['name']} has {celebrity1['follower_count']} while {celebrity2['name']} has {celebrity2['follower_count']} ")
      print(f"You are correct! Your score is {score}\n")
      celebrity1 = celebrity2
    else:
      print(f"{celebrity1['name']} has {celebrity1['follower_count']} while {celebrity2['name']} has {celebrity2['follower_count']} ")
      print(f"\nYou are wrong! Your score is {score}")
      print("Game over")
      return False

game_over = False
print(logo)
print("----***-----***---Welcome to the Higher Lower guessing game!---***-----***----")
while not game_over:
   user_choice = input("Do you want to play a game? ").lower()
   if user_choice == "y":
     compare()
   else:
     print("Okay maybe next Time!")
     game_over = True
