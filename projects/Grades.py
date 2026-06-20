# 1. A list of subjects and the marks you scored (out of 100)
marks = {
    "Math": 85,
    "Computer Science": 92,
    "Physics": 78,
    "English": 65
}

print("=== STUDENT MARK SHEET ===")
print("--------------------------")

# 2. A loop to go through each subject and print the score
for subject, score in marks.items():
    
    # 3. If/Else to decide if you passed or failed that subject
    if score >= 50:
        status = "PASSED"
    else:
        status = "FAILED"
        
    print(f"{subject}: {score}/100 -> [{status}]")

print("--------------------------")

# 4. Simple math to calculate the average mark
total_score = sum(marks.values())
number_of_subjects = len(marks)
average = total_score / number_of_subjects

print(f"Your Average Score is: {average}")
