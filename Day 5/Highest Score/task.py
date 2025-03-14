student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
# for i in range(len(student_scores)):
#     for j in range(len(student_scores)):
sums = 0
for score in student_scores:
    sums = sums + score
print(sums)
print(sum(student_scores))
max_score = 0
for m in student_scores:
    if m > max_score:
        max_score = m
print(max_score)
print(max(student_scores))



