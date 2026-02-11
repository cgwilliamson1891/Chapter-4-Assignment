# COMP 163 - Intro to Programming
# Assignment: Chapter 4 - College Life Adventure Game
# Name: Chloe Williamson
# GitHub Username: cgwilliamson1891
# Date:
# Description:  [2-3 sentences describing your game's theme and objective] 
# AI Usage:

# --------------------------------
# Step 1: Foundation Setup
# --------------------------------


student_name = "Chloe Williamson"
current_gpa = 2.9
study_hours = 25
social_points = 50
stress_level = 50

print(f"Welcome, {student_name}!")
print(f"Starting GPA: {current_gpa}")
print(f"Study Hours: {study_hours}")
print(f"Social Points: {social_points}")
print(f"Stress Level: {stress_level}")

# --------------------------------------------
# Step 2: Course Planning Decision (GPA-Based)
# --------------------------------------------

print("\nChoose your course load:")
print("A - Light")
print("B - Standard")
print("C - Heavy")

choice = input("Enter A, B, or C: ")

if choice == "A": # Light Load
    study_hours -= 5
    stress_level -= 10
    # Light load is easier: lower GPA improces more, high GPA stay stable
    if current_gpa >= 3.5:
        current_gpa += 0.05 # high GPA: small gain, already strong 
    else:
        current_gpa += 0.1 # low GPA: can focus and improve
    print("You chose a light load. Less stress and study hours.")

elif choice == "B": # Standard Load
    study_hours += 5
    stress_level += 10
    #Balanced load: moderate improvement for all, still GPA-dependent
    if current_gpa >= 3.5:
        current_gpa += 0.1
    else:
        current_gpa += 0.05
    print("You took a standard load. Balanced stress and study levels.")

elif choice == "C": 
    study_hours += 10
    # High GPA students preform well: work ethic allows them to thrive
    if current_gpa >= 3.0:
        stress_level += 15
        current_gpa += 0.2
        print("You took a heavy load, but your high GPA proves you can manage.")
    else:
        # GPA too low: cant pick heavy load
        print("Your GPA is not high enough to take a heavy course load. PLease choose Light ot Standard.")
        choice = input("Enter A or B: ")

        # Re-run logic for light or Dtandard
        if choice == "A":
            study_hours -= 5
            stress_level -= 10
            if current_gpa >= 3.5:
                current_gpa += 0.05  
            else:
                current_gpa += 0.1 
            print("You chose a light load. Less stress and study hours.")

        elif choice == "B": 
            study_hours += 5
            stress_level += 10
    
            if current_gpa >= 3.5:
                current_gpa += 0.1
            else:
                current_gpa += 0.05
            print("You took a standard load. Balanced stress and study levels.")
        else:
            print("Invalid Input. No schedule changes made.") 

else:
    print("Invalid Input. No schedule changes made.")

# --------------------------------
# Step 3: Study Strategy Decision
# --------------------------------






