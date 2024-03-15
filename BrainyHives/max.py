students = ['Enobong', 'Arinze', 'Kunle', 'Danjuma']
scores = [85, 92, 78, 95]
max_score = max(scores)
index = scores.index(max_score)
student_with_the_highest_score = students[index]

print(f"The student with the highest score is {student_with_the_highest_score} with a score of {max_score}.")