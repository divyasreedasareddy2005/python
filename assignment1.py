# Student Grade Tracker

# Step 1: Collect student info
student_id = int(input("Enter Student ID: "))
student_name = input("Enter Student Name: ")
attendance = int(input("Enter Attendance (%): "))

# Step 2: Collect scores
scores = []
while True:
    score = int(input("Enter a score/marks: "))
    scores.append(score)

    another = input("Do you want to enter another score? (yes/no): ").lower()
    if another != "yes":
        break

# Step 3: Calculate totals
total_score = sum(scores)
num_scores = len(scores)
average_score = total_score / num_scores if num_scores > 0 else 0

# Step 4: Grade calculation
if average_score >= 85:
    grade = "A"
elif average_score >= 70:
    grade = "B"
elif average_score >= 50:
    grade = "C"
else:
    grade = "FAIL"

# Step 5: Attendance check
if attendance < 75:
    attendance_status = "WARNING LOW ATTENDANCE"
else:
    attendance_status = "GOOD ATTENDANCE"

# Step 6: Award eligibility
if attendance_status == "GOOD ATTENDANCE" and grade == "A":
    award = "YES"
else:
    award = "NO"

# Step 7: Print Output
print("\n----- Student Report -----")
print(f"Student ID = {student_id}")
print(f"Student Name = {student_name}")
print(f"Attendance = {attendance}")
print(f"Total Score = {total_score}")
print(f"Average Score = {average_score}")
print(f"Number of Scores = {num_scores}")
print(f"Student Grade = {grade}")
print(f"Attendance Criteria = {attendance_status}")
print(f"Award Eligibility = {award}")
