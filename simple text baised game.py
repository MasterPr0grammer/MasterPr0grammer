def play_again():
  print("\nDo you want to play again? (y or n)")

  # convert the player's input to lower_case
  answer = input(">").lower()

  if "y" in answer:
    # if player typed "yes" or "y" start the game from the beginning
    start()
  else:
    # if user types anything besides "yes" or "y", exit() the program
    exit()

# game_over function accepts an argument called "reason"
def game_over(reason):
  # print the "reason" in a new line (\n)
  print("\n" + reason)
  print("Game Over!")
  # ask player to play again or not by activating play_again() function
  play_again()

def amougus_room():
  # some prompts
  print("\nYou are now in a sus room... the amougus room")
  print("The imposter is in this room somewhere. You need to vote them out of the room")
  print("Who would you like to vote out?")
  print("1). Vote out Pink")
  print("2). Vote out Red")
  print("3). Vote out Black")
  print("4). Vote out Yellow")
  # take input()
  answer = input(">")

  if answer == "1":
    # wrong answer
    game_over("You voted out a crewmate! Everyone thinks your sus and vote you out")
  elif answer == "2":
    # the player won the game
    print("That was the imposter! The crewmates let you through.")
    diamond_room()
  elif answer == "3":
    # wrong answer
    game_over("You voted out the only black crewmate! Everyone thinks your racist and vote you out")
  elif answer == "4":
    # wrong answer
    game_over("You voted out a crewmate! Everyone thinks your sus and vote you out")
  else:
    # call game_over() with "reason"
    game_over("Go and learn how to type a number.")

# diamond room
def diamond_room():
  # some prompts
  print("\nYou are now in a room filled with diamonds!")
  print("And there is a door too!")
  print("What would you do? (1 or 2)")
  print("1). Take some diamonds and go through the door.")
  print("2). Just go through the door.")

  # take input()
  answer = input(">")

  if answer == "1":
    # the player is dead, call game_over() function with the "reason"
    game_over("They were cursed diamonds! The moment you touched it, the building collapsed, and you die!")
  elif answer == "2":
    # the player won the game
    print("\nNice, you're are an honest man! Congrats you win the game!")
    # activate play_again() function
    play_again()
  else:
    # call game_over() with "reason"
    game_over("Go and learn how to type a number.")

# monster room
def monster_room():
  # some prompts
  # '\n' is to print the line in a new line
  print("\nNow you entered the room of a monster!")
  print("The monster is sleeping.\nBehind the monster, there is another door. What would you do? (1 or 2)")
  print("1). Go through the door silently.")
  print("2). Kill the monster and show your courage!")
  print("3). Start dancing with the monster and make a new friend.")
  # take input()
  answer = input(">")

  if answer == "1":
    # lead him to the diamond_room()
    diamond_room()
  elif answer == "2":
    # the player is dead, call game_over() with "reason"
    game_over("The monster was hungry, he/it ate you.")
  elif answer == "3":
    # made a friend of the monster
    print("\nYou made the monster cry, it has never been treated so nice in its life.")
    diamond_room()
    # 420 snoop dog room, instant win
  elif answer == "420":
   game_over("AYYYYY YOU AUTOMATICLY WIN BECAUSE OF YOUR SWAGGER, OUT THERE LOOKING LIKE SNOOP DOG")
  else:
    # game_over() with "reason"
    game_over("Go and learn how to type a number.")

# bear room
def bear_room():
  # give some prompts
  # '\n' is to print the line in a new line
  print("\nThere is a bear here.")
  print("Behind the bear is another door.")
  print("The bear is eating tasty honey!")
  print("What would you do? (1 or 2)")
  print("1). Take the honey.")
  print("2). Taunt the bear.")
  print("3). Share honey with bear.")
  # take input()
  answer = input(">")

  if answer == "1":
    # the player is dead!
    game_over("The bear killed you.")
  elif answer == "2":
    # lead him to the diamond_room()
    print("\nYour Good time, the bear moved from the door. You can go through it now!")
    diamond_room()
    # 69 instant win room
  elif answer == "3":
    print("\nThe bear thinks it was a bit sus that you shared honey with him but he's happy for your hospitality.")
    amougus_room()
  elif answer == "69":
    game_over("AYYYYY YOU AUTOMATICLY WIN BECAUSE OF YOUR SWAGGER")
  else:
    # else call game_over() function with the "reason" argument
    game_over("Don't you know how to type a number?")

def start():
  # give some prompts.
  print("\nYou are standing in a dark room.")
  print("There is a door to your left and right, which one do you take? (l or r)")

  # convert the player's input() to lower_case
  answer = input(">").lower()

  if "l" in answer:
    # if player typed "left" or "l" lead him to bear_room()
    bear_room()
  elif "r" in answer:
    # else if player typed "right" or "r" lead him to monster_room()
    monster_room()
  else:
    # else call game_over() function with the "reason" argument
    game_over("Don't you know how to type something properly?")


# start the game
start()
