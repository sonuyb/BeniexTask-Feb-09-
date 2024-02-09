user_input = input("Enter the student's score: ")
score = float(user_input)
if 0 <= score <= 100:
    if score >= 90:
        print("Grade: A+")
    elif score >= 80:
                print("Grade: A")
    elif score >= 70:
        print("Grade: B+")
    elif score >= 60:
        print("Grade: B")
    elif score >= 50:
        print("Grade: C")
    else:
        print("Failed")
else:
    print("Invalid input. Please enter a score between 0 and 100.")