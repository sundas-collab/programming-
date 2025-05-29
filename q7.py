# Original tuple of student marks
student_marks = (65, 70, 75, 80, 85)

# I. Print the first and last elements of the tuple
print("First mark:", student_marks[0])
print("Last mark:", student_marks[-1])

# II. Unpack the tuple into separate variables
m1, m2, m3, m4, m5 = student_marks
print("\nUnpacked Marks:")
print("m1 =", m1)
print("m2 =", m2)
print("m3 =", m3)
print("m4 =", m4)
print("m5 =", m5)

# III. Create a new tuple with 5 marks added to each element
new_marks = tuple(mark + 5 for mark in student_marks)

# IV. Print both the original and the new tuples
print("\nOriginal Marks Tuple:", student_marks)
print("New Marks Tuple (+5):", new_marks)