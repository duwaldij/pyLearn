command = ""
started= False
while True:
    command = input("> ").lower()
    if command =="start":
        if started:
            print("The car is already in motion")
        else:
            started = True
            print("Car Started")
    elif command =="stop":
        if not started:
            print("The car is already in rest")
        else:
            started = False
            print("The car is stopped")
    elif command =="help":
        print("""
start- to start the car
stop- to stop the car
exit- to quit the game
        """)
    elif command =="exit":
        break
    else:
        print("I dont understand")