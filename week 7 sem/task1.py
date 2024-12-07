def observe():
    observations = []
    for count in range(7):
        print("pleas enter an observation")
        observations.append(input())
    return observations
def run_task2():
    print("counting observations")
    observes = observe()
    observations_set = set()
    for observation in observes:
        data = (observation, observes.count(observation))
        observations_set.add(data)
    for data in observations_set:
        print(f"{data[0]} observed {data[1]} times")
run_task2()