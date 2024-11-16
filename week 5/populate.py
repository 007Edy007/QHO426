def directins():
    steps = ["move forward", "move backward", "turn left", "turn right"]
    return steps
def menu_and_input():
    print("select a direction")
    steps = directins()
    for index, directions in enumerate(steps):
        print(f"{index}: {directions}")
    while True:
        try:
            choice = int(input("enter a number: "))
            if 0 <= choice < len(steps):
                return steps[choice]
            else:
                print("invalid choice")
        except ValueError:
            print("invalid input")
def run_task4():
    route =[]
    print("working out escape route....")
    for _ in range(5):
        route.append(menu_and_input())
    print(f"escape route: {route}")
run_task4()