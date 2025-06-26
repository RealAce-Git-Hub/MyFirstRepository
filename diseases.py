disease1 = "malaria"
disease1 = "flu"
disease3 = "Cold"
disease4 = "Migrane"

tempurature = float(input("What is your tempurature in celsius?: "))
symptom1 = input("Enter symptoms 1: ")
symptom2 = input("Enter symptom 2: ")

if (tempurature >= 36.1) and (tempurature <= 37.2):
    print("Your tempurature is normal, you are not sick.")

elif (tempurature > 37.2):
    print("Your tempurate is above normal, you might be sick.")

    if (symptom1 == "headache") and (symptom2 == "nausea"):
        print("Your symptoms show that you might have Malaria.")
    
    elif (symptom1 == "cough") and (symptom2 == "sore throat"):
        print("Your symptoms show that you might have the Flu")