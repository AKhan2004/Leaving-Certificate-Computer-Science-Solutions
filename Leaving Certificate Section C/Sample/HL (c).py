# Question 16(c)
# Examination Number:

def find_nth_largest(n, list_of_values): # (iii)
    list_of_values = sorted(set(list_of_values), reverse=True)
    return list_of_values[n - 1]

bmi_values = [24, 19, 33, 35, 27, 18, 15, 33, 35, 23, 32, 23]
o_count = 0 # (i)

for count in bmi_values:
    if count >= 30:
        o_count += 1

largest = 0
second_largest = 0

for i in bmi_values: # (ii)
    if i >= largest:
        largest = i
    elif i >= second_largest:
        second_largest = i

print("Obese:", o_count)
print("Largest:", largest)
print("Second Largest:", second_largest)
print(find_nth_largest(3, bmi_values))