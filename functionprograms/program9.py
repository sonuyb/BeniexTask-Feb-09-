def check_attendance(roll_number):
    present_roll_numbers = [101, 102, 105, 107, 110]
    if roll_number in present_roll_numbers:
        return "Present"
    else:
        return "Absent"
roll_number =int(input('enter your roll number'))
attendance_status = check_attendance(roll_number)
print(f"Roll number {roll_number} is {attendance_status}")
