from joblib import load

spamOrNotModel = load("spamOrNotModel.pkl")
while True:
    emailInput = input("Enter an email: ")
    prediction = spamOrNotModel.predict([emailInput])
    if(prediction == 0):
        print("This is not a spam email")
    else: 
        print("This is a spam email")