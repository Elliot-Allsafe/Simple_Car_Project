def car_fun():
    is_start = False
    while True:
        command = str(input("> "))
        valid = ["help", "stop", "start", "quit"]
        if command == valid[0] or command == valid[0].upper():
            print("help => to show valid commands.")
            print("start => to start the car.")
            print("stop => to stop the car.")
            print("quit => to exit the car.")
        elif command == valid[1]:
            if not is_start:
                print("Car is already Stopped...")
            else:
                print("Car Stopped...")
                is_start = False
        elif command == valid[2]:
            if is_start:
                print("Car already Started...")
            else:
                print("Car Started...")
                is_start = True
        elif command == valid[3]:
            print("Exiting the Car..")
            break
        else:
            print("Sorry I Don't UnderStand...")
            continue
