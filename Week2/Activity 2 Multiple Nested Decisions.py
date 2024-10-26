print("Where should i look?")
location = input()
if location == "bedroom":
    print("where in the bedroom?")
    bed_location = input()
    if bed_location == "cupboard":
        print("found some mess but no phone")
    else:
        print ("other location")
elif location == "bathroom":
    print("where in the bathroom?")
    bath_location = input()
    if bath_location == "bathtub":
        print("found the rubber duck but no phone")
    else:
        print ("other location")
elif location == "living room":
    print ("where in the living room?")
    living_location = input()
    if living_location == "on the table":
        print ("yes! i found my phone!")
    else:
        print("other location")
else:
    print("try an other room")