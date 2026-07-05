while True:
    print("\n--- BMI CALCULATOR ---") 
    try:
        # 1. Prompt user for weight and height
        weight=float(input("Enter your weight in kg(e.g.,65.5):"))
        height=float(input("Enter your height in meters(e.g.,1.65):"))            
        # 2. Input validation: Reject negative values or zero
        if weight<=0 or height<=0:
            print("Error:Weight and height must be positive numbers!")            
        # 3. Calculate BMI using formula: weight / (height * height)
        bmi=weight/(height**2)       
        # 4. Display BMI value rounded to 2 decimal places
        print(f"\nYour BMI is:{bmi:.2f}")       
        # 5. Classify result into standard categories
        if bmi<18.5:
            print("Category: Underweight")
        elif 18.5<=bmi<=24.9:
            print("Category: Normal")
        elif 25<=bmi<=29.9:
            print("Category: Overweight")
        else:
            print("Category: Obese")            
    # Reject non-numeric input (letters/symbols)
    except ValueError:
        print("Error: Please enter valid numbers only!")
    # Option to run again
    again=input("\nDo you want to calculate another BMI? (y/n): ").strip().lower()
    if again!='y':
        print("Thank you! Goodbye.")
        break