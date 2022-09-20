import random


ties=0
player_win = 0
comp_win = 0



yes = ["y" , "yes" , "yah" , "yup" , "yep"]
no = ["nah" , "nope" , "no" ,"n"]
choice2 = ["nah" , "nope" , "no" ,"n" , "y" , "yes" , "yah" , "yup" , "yep"]
choices = ["rock" , "paper" , 'scissors']



print("Hello and welcome to this game of rock, paper, scissors!")

while True:

    user = input("Please enter your choice\n").lower()

    while user not in choices:
        user = input(f"This \"{user}\" doesn't match the choices! Please be sure to select rock, paper or scissors.\n")




    comp = random.choice(choices)

    print(F"user: {user}")
    print(F"comp: {comp}")

    if user == comp:
        tie = print("Oh no we tied, let's do another one.")
        ties += 1

    elif ((user=="rock" and comp=="scissors") or (user == "paper" and comp == "rock") or (user=="scissors" and comp=="paper")):
        win = print('You win congrats!')
        player_win += 1



    elif ((user=="scissors" and comp=="rock") or (user=="rock" and comp=="paper") or (user=="paper" and comp=="scissors")):
        lose = print("Damnit you lose! :(")
        comp_win += 1



    else: (print("This was not into the choices please restart!"))


    another_game = input("Would you like to play another game?\n").lower()

    if another_game == yes:
        pass


    while another_game not in choice2:


        another_game = input(f"Sorry \n\"{another_game}\" is not valid please insert yes or no.\n")

    print("Here is the results")

    if ties <= 1:
        print(f"We have {ties} tie")
    else:
        print(f"We have {ties} ties")



    if player_win <= 1:
        print(f"You have {player_win} win")
    else:
        print(f"You have {player_win} wins")



    if comp_win <= 1:
        print(f"I have {comp_win} win")
    else:
        print(f"I have {comp_win} wins")


    print(f"You're win ratio is {player_win / sum((player_win , comp_win , ties))}% with " f"{ties + player_win + comp_win}" " games played.")

    if another_game not in yes:
        print("Okay bye!")

        break





  #rock,paper,scissors
  #making a score
  #making a ratio
  #making a while loop
  #making a list
  #making plurals if there's more than 1 win , tie or lose.










