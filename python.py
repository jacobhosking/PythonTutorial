print("Welcome to the World of Warcraft")

name = input("Enter your heros name: ")

#The curly braces show where the inserted value should go.
#Way to insert a variable in a string
#Another way: print("Welcome", name, "to the World of Warcraft!")
intro_text = "Welcome {}, to the World of Warcraft!" .format(name)

print(intro_text)

#by default inputs are considered strings
#also works by using age = int(input("How old are you traveler"))
age = input("How old are you traveler: ")


#need to specify age as a int
if int(age) >=18:
    print("Welcome aboard adventurer. Gather your supplies and get ready!")

    #Use (f before string and {} with variable name to call variable during a input)
    ready_up = input(f"Are you ready to leave {name}? ").lower()
    if ready_up == "yes":
        print("Jump into the wagon and lets go.")

        first_encounter = input(f"{name} we have found a split in the road. Do you want to go left towards Ironforge or right towards Stormwind (Left/Right):").lower()
        if first_encounter == "left":
            print("You have headed toward Ironforge. ")

            #Ironforge encounter.

        else: 
            print("You have headed to Stormwind:")

            stormwind_encounter = input("We have found a pack of wild boars. (Attack/Runaway:)").lower()
            if stormwind_encounter == "attack":
                print("You have killed the boar")

    else: 
        print("We have no time to wait! We will have to leave you behind.")
 

else:
    print("You are too young adventurer. Come back when you are wiser.")

#Need to figure out error checking for invalid input



'''it = random.uniform(0, 10)
f hit <= 2:
    damage = 0.00
else:
    damage = (hit - 2) / 8'''

