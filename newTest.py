from functools import reduce


students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

sorted_students = sorted(students)

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]

def add(x, y):
    return x + y

sum_of_numbers = []
result = {}

for grade in grades:
   sum_of_numbers.append(reduce(add, grade) / len(grade))


for i in range(len(students)):
    result[sorted_students[i]] = sum_of_numbers[i]


print(result)





