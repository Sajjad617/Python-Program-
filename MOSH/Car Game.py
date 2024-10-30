command = ""
started = False
while True:
    command = input(">> ").lower()
    if command == "start":
        if started: # started = False, It won't the work
            print("car already started!")
        else:
            started = True # Started = True, It will the work
            print("car started...")
    elif command == "stop":
        if not started:
            print("car already stop")
        else:
            started = False
            print("car stopped")
    elif command == "help":
        print("""
        start - to start the car.
        stop - to stop the car.
        quit -  to quit.
        """)
    elif command == "quit":0808
        break
    else:
        print("I don't understand that!")
