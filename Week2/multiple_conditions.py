print ("chose your type of adventure: scary, short, safe or long")
adventure = input()
if (adventure == "scary") or (adventure == "short"):
    print ("entering the dark forest")
elif (adventure == "safe") or (adventure == "long"):
    print("taking the safe rout")
else:
    print("nt sure wich rout to take")