def pattern():
    sequences ={
        "Short":3,
        "medium":2,
        "long":1
    }
    return sequences
def display_keys(data):
    print("Keys:")
    for key in data:
        print(key)
    print()
def display_values(data):
    print("Values: ")
    for value in data.values():
        print(value)
    print()
def display_pairs(data):
    print("Pairs:")
    for key, value in data.items():
        print(f"{key}:{value}")
    print()
def run():
    data = pattern()
    display_keys(data)
    display_values(data)
    display_pairs(data)
run()
