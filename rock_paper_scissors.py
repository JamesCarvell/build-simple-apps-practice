from random import choice
from time import sleep

rpc = ["rock", "paper", "scissors"]

done = False
wins = 0
losses = 0
ties = 0

while not done:
    user = input(f"{rpc[0]}, {rpc[1]}, or {rpc[2]}?\n>")
    if user == "done":
        print("bye!")
        done = True
        continue
    elif user not in rpc:
        print('that won\'t do. type "done" if you want out.')
        continue
    computer = choice(rpc)
    print(f"\n{rpc[0]}!"); sleep(0.8)
    print(f"{rpc[1]}!"); sleep(0.8)
    print(f"{rpc[2]}!"); sleep(0.8)
    print(f"\n{computer}!\n"); sleep(0.8)

    if user == computer:
        print(f"{user} ties {computer}.")
        ties += 1
    elif (user == rpc[0] and computer == rpc[2]) or \
    (user == rpc[1] and computer == rpc[0]) or \
    (user == rpc[2] and computer == rpc[1]):
        print(f"{user} beats {computer}!")
        wins += 1
    else:
        print(f"{computer} beats {user}...")
        losses += 1
    
    print(f"{wins} wins, {losses} losses, & {ties} ties.\n"); sleep(0.8)
