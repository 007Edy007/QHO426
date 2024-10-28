print("how many bars should be charged?")
bars = int(input())
start_charge = 0
while start_charge < bars:
    start_charge += 1
    print("charging")
    print(f"{start_charge} is charged")
else:
    print("fully charged")