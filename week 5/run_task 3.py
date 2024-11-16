def directins():
    steps = ["move forward", "move backward", "turn left", "turn right"]
    return steps
def menu():
    print("select a direction")
    steps = directins()
    for index, directions in enumerate(steps):
        print(f"{index}: {directions}")
menu()