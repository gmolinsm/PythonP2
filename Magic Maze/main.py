moves = 0
lives = 3
path = str("SSNWES")
track = str("")
while True:
    command = str(input("You are in the magic maze. Which way to go? (N,S,E,W):"))
    track += command
    print(track)
    moves += 1
    if track == path:
        print("You have escaped the maze in", moves, "moves!")
        break
    else:
        if moves % 10 == 0:
            lives -= 1
            print("You have", lives, "lives left")
        if lives == 0:
            print("Game over")
            break
        if path.__contains__(track) and track.startswith("S"):
            continue
        else:
            print("Wrong move, starting over")
            track = str("")
