def movements():
    path = ["move forward", "move backward", "turn left", "turn right"]
    return path
def run_task1():
    print("moving....")
    path = movements()
    #print(f"{path[0]} for {path[1]} steps")
    #print(f"{path[2]} for {path[3]} steps")
    #print(f"{path[4]} for {path[5]} steps")
    #print(f"{path[6]} for {path[7]} steps")
    for item in range(0, len(path), 2):
        print(f"{path[item]}: {path[item+1]}")

