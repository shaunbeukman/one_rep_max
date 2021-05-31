""" First get users weight and number of reps """

weight = int(input("Enter your weight in kg's: "))
reps = int(input("Enter number of reps: "))

""" Calculate the 1RM using the Brzycki Formula in a
function called one_rep_max """

def one_rep_max(weight, reps):
    while weight > 1:
        return weight / (1.0278 - 0.0278 * reps)
        weight += 1


""" Display the result in a string and rounded 1 decimal place """

print("Your one rep max is: " + str(round(one_rep_max(weight, reps),1)) + "kg")
    

    
