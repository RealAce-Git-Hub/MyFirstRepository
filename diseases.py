disease1 = "Malaria"
disease2 = "Flu"
disease3 = "Cold"
disease4 = "Migrane"

temperature = float(input("What is your temperature in celsius?: "))
symptom1 = input("Enter your first symptom: ")
symptom2 = input("Enter your second symptom: ")

if (temperature >= 36.1) and (temperature <= 37.2):
    print("Your temperature is normal, you may not be sick.")

    if (symptom1 == "cough") and (symptom2 == "stuffy nose"):
        print("Your symptoms show that you might have a Cold.")

    elif (symptom1 == "headache") and (symptom2 == "dizziness"):
        print("Your symptoms show you might have a Migrane.")

elif (temperature > 37.2):
    print("Your temperature is above normal, you might be sick.")

    if (symptom1 == "headache") and (symptom2 == "nausea"):
        print("Your symptoms show that you might have Malaria.")

    elif (symptom1 == "cough") and (symptom2 == "sore throat"):
        print("Your symptoms show that you might have the Flu.")

else:
    print("Your temperature is below normal, please visit the doctor immediately.")