first = input('Ведите число: ')
second = input('Ведите число: ')
third = input('Ведите число: ')
if first == second == third:
    print(3)
elif first == second or first==third or second==third:
    print(2)
else:
    print(0)

