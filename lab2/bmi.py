def calculate_bmi(height, weight):

    print("Height = " , float(height))

    print("Weight = " , float(weight))
    
    bmi = weight/(height **2)
    print(f"BMI = {bmi:.3f}")
    if(bmi<18.5):
        print("You are underweight")
        return -1
    elif(25.0>=bmi>=18.5):
        print("You have a normal BMI")
        return 0
    elif(bmi>25):
        print("You are obese")
        return 1
if __name__ == "__main__":
    calculate_bmi(1.73,57)